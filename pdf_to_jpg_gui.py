import os
import fitz  # PyMuPDF
import platform
import subprocess
import threading
import tkinter as tk
from tkinter import filedialog, messagebox, ttk


# ===== 工具函数 =====
def parse_page_selection(selection, total_pages):
    selection = selection.strip().lower().replace("，", ",")
    pages = set()

    if selection in ["", "all"]:
        return list(range(1, total_pages + 1))
    if selection == "odd":
        return [i for i in range(1, total_pages + 1) if i % 2 == 1]
    if selection == "even":
        return [i for i in range(1, total_pages + 1) if i % 2 == 0]

    for part in selection.split(","):
        part = part.strip()
        if "-" in part:
            start, end = part.split("-")
            if start.isdigit() and end.isdigit():
                pages.update(range(int(start), int(end) + 1))
        elif part.isdigit():
            pages.add(int(part))

    return sorted([p for p in pages if 1 <= p <= total_pages])


def open_folder(path):
    """打开输出文件夹"""
    try:
        if platform.system() == "Windows":
            os.startfile(path)
        elif platform.system() == "Darwin":
            subprocess.Popen(["open", path])
        else:
            subprocess.Popen(["xdg-open", path])
    except Exception as e:
        print(f"⚠️ 无法打开文件夹：{e}")


def pdf_to_images(pdf_path, output_dir, dpi=200, page_selection=None, progress_callback=None):
    """将 PDF 转为 JPG 图片"""
    os.makedirs(output_dir, exist_ok=True)
    pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]
    pdf_document = fitz.open(pdf_path)
    total_pages = len(pdf_document)

    if not page_selection:
        page_selection = list(range(1, total_pages + 1))

    for idx, page_number in enumerate(page_selection, start=1):
        try:
            page = pdf_document.load_page(page_number - 1)
            pix = page.get_pixmap(dpi=dpi)
            image_filename = f"{pdf_name}_page_{page_number}.jpg"
            image_path = os.path.join(output_dir, image_filename)
            pix.save(image_path)
        except Exception as e:
            print(f"⚠️ 第 {page_number} 页导出失败：{e}")

        if progress_callback:
            progress_callback(idx / len(page_selection) * 100)

    pdf_document.close()
    open_folder(output_dir)


# ===== 图形界面 =====
class PDFConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("📄 PDF 转 JPG 图片工具")
        self.root.geometry("500x400")
        self.root.resizable(False, False)

        self.pdf_path = None
        self.output_dir = None

        # === 文件选择 ===
        tk.Label(root, text="选择 PDF 文件：").pack(anchor="w", padx=15, pady=(15, 0))
        frame = tk.Frame(root)
        frame.pack(fill="x", padx=15)
        self.file_entry = tk.Entry(frame, width=50)
        self.file_entry.pack(side="left", fill="x", expand=True)
        tk.Button(frame, text="浏览...", command=self.select_pdf).pack(side="right", padx=5)

        # === 输出目录 ===
        tk.Label(root, text="输出目录：").pack(anchor="w", padx=15, pady=(10, 0))
        output_frame = tk.Frame(root)
        output_frame.pack(fill="x", padx=15)
        self.output_entry = tk.Entry(output_frame, width=50)
        self.output_entry.pack(side="left", fill="x", expand=True)
        tk.Button(output_frame, text="浏览...", command=self.select_output_dir).pack(side="right", padx=5)
        
        # 默认输出目录提示
        self.output_entry.insert(0, "默认：PDF文件同目录下的output_images文件夹")

        # === 页码选择 ===
        tk.Label(root, text="导出页码（支持 1,3,5-8,10 / all / odd / even）：").pack(anchor="w", padx=15, pady=(10, 0))
        self.page_entry = tk.Entry(root)
        self.page_entry.pack(fill="x", padx=15)

        # === 分辨率设置 ===
        tk.Label(root, text="图片分辨率 (DPI)：").pack(anchor="w", padx=15, pady=(10, 0))
        self.dpi_entry = tk.Entry(root)
        self.dpi_entry.insert(0, "200")
        self.dpi_entry.pack(fill="x", padx=15)

        # === 进度条 ===
        tk.Label(root, text="转换进度：").pack(anchor="w", padx=15, pady=(10, 0))
        self.progress = ttk.Progressbar(root, length=460, mode="determinate")
        self.progress.pack(padx=15, pady=5)

        # === 状态显示 ===
        self.status_label = tk.Label(root, text="等待操作...", fg="gray")
        self.status_label.pack(padx=15, pady=5)

        # === 开始按钮 ===
        tk.Button(root, text="开始转换", command=self.start_conversion, bg="#4CAF50", fg="white", height=2).pack(fill="x", padx=15, pady=10)

    def select_pdf(self):
        path = filedialog.askopenfilename(title="选择 PDF 文件", filetypes=[("PDF 文件", "*.pdf")])
        if path:
            self.pdf_path = path
            self.file_entry.delete(0, tk.END)
            self.file_entry.insert(0, path)
            
            # 自动设置默认输出目录
            default_output = os.path.join(os.path.dirname(path), "output_images")
            self.output_entry.delete(0, tk.END)
            self.output_entry.insert(0, default_output)

    def select_output_dir(self):
        directory = filedialog.askdirectory(title="选择输出目录")
        if directory:
            self.output_dir = directory
            self.output_entry.delete(0, tk.END)
            self.output_entry.insert(0, directory)

    def start_conversion(self):
        pdf_path = self.file_entry.get().strip()
        output_dir = self.output_entry.get().strip()
        dpi = int(self.dpi_entry.get().strip() or "200")
        selection = self.page_entry.get().strip()

        if not pdf_path or not os.path.exists(pdf_path):
            messagebox.showerror("错误", "请先选择一个有效的 PDF 文件！")
            return

        # 处理输出目录
        if not output_dir or output_dir == "默认：PDF文件同目录下的output_images文件夹":
            output_dir = os.path.join(os.path.dirname(pdf_path), "output_images")
        elif not os.path.exists(output_dir):
            try:
                os.makedirs(output_dir, exist_ok=True)
            except Exception as e:
                messagebox.showerror("错误", f"无法创建输出目录：{e}")
                return

        pdf_document = fitz.open(pdf_path)
        total_pages = len(pdf_document)
        pdf_document.close()

        pages = parse_page_selection(selection, total_pages)
        if not pages:
            messagebox.showerror("错误", "页码选择无效！")
            return

        self.status_label.config(text=f"正在转换（共 {len(pages)} 页）...", fg="blue")
        self.progress["value"] = 0

        # 多线程防止 GUI 卡顿
        threading.Thread(target=self.convert_thread, args=(pdf_path, output_dir, dpi, pages)).start()

    def convert_thread(self, pdf_path, output_dir, dpi, pages):
        pdf_to_images(pdf_path, output_dir, dpi=dpi, page_selection=pages, progress_callback=self.update_progress)
        self.status_label.config(text="✅ 转换完成！图片已保存并打开目录。", fg="green")

    def update_progress(self, value):
        self.progress["value"] = value
        self.root.update_idletasks()


# ===== 主程序入口 =====
if __name__ == "__main__":
    root = tk.Tk()
    app = PDFConverterApp(root)
    root.mainloop()