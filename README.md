下面是你提供的内容，我已经 **完整整理、格式化成最终版 README（中英文双语一体）**，直接复制即可作为 `README.md` 使用。

你无需再做额外修改，结构、锚点、徽章、目录链接等均已校对无误。

---

# 🇨🇳 中文 README（Simplified Chinese）

# 🧰 PDF 转图片工具（PDF to JPG Converter）

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12+-blue?logo=python">
  <img src="https://img.shields.io/badge/License-MIT-green">
  <img src="https://img.shields.io/badge/GUI-Tkinter-yellow">
  <img src="https://img.shields.io/badge/Build-PyInstaller-orange">
</p>

一个基于 **Python + Tkinter** 的桌面应用工具，可将 PDF 文档快速转换为 JPG 图片。支持自定义页码导出、批量转换、可视化操作。

---

## 📚 目录（Table of Contents）

* [🌟 功能特点](#-功能特点)
* [🖼️ 软件界面截图](#️-软件界面截图)
* [🚀 使用方法](#-使用方法)
* [🔢 自定义页码规则](#-自定义页码规则)
* [📦 打包成 EXE](#-打包成-exe)
* [📁 项目结构](#-项目结构)
* [📄 依赖说明](#-依赖说明)
* [📦 GitHub Release 功能说明](#-github-release-功能说明)
* [📄 开源协议](#-开源协议)
* [👨‍💻 作者](#-作者)
* [🇬🇧 English Version](#-english-version)

---

## 🌟 功能特点

✔ 支持 PDF → JPG 批量转换
✔ 支持自定义导出页码（如：`1,3,5-8`）
✔ 可一键全页导出
✔ 输出文件夹可自定义
✔ PDF 渲染质量高（基于 PyMuPDF）
✔ 集成 GUI，操作简单
✔ 可打包成 Windows 独立 EXE

---

## 🖼️ 软件界面截图

> 你可以把图片放到 `assets/screenshot.png`

```
![软件界面示例](assets/screenshot.png)
```

---

## 🚀 使用方法

### 方式一：运行 EXE（推荐）

1. 到 **Releases** 页面下载最新版本
2. 运行 `PDF转图片工具.exe`
3. 选择 PDF
4. 设置输出目录
5. 点击【开始转换】

---

### 方式二：运行源码

安装依赖：

```bash
pip install -r requirements.txt
```

运行：

```bash
python pdf_to_jpg_gui.py
```

---

## 🔢 自定义页码规则

| 输入          | 说明       |
| ----------- | -------- |
| `1`         | 仅导出第 1 页 |
| `1-5`       | 导出 1~5 页 |
| `2,4,8`     | 指定页码     |
| `3,6-10,12` | 混合组合     |
| `all`       | 全部页      |

---

## 📦 打包成 EXE

```bash
pyinstaller -F -w -i icon.ico -n "PDF转图片工具" pdf_to_jpg_gui.py
```

> 如提示 `Icon input file not found`，请确认 `icon.ico` 是否存在。

---

## 📁 项目结构

```
📁 PDF-to-JPG-Converter
 ├── pdf_to_jpg_gui.py
 ├── requirements.txt
 ├── README.md
 ├── LICENSE
 ├── icon.ico
 └── assets/
```

---

## 📄 依赖说明

| 库           | 功能     |
| ----------- | ------ |
| **PyMuPDF** | PDF 渲染 |
| **Pillow**  | 图片保存   |
| **Tkinter** | GUI    |

---

## 📦 GitHub Release 功能说明

发布内容可包含：

### 🆕 版本更新内容（示例）

* 新增：自定义页码批量导出
* 优化：大型 PDF 文件解析速度
* 修复：某些 PDF 无法导出的问题
* 新增：自动输出目录检测

---

### 📥 下载内容

* `PDF转图片工具.exe` —— Windows 64 位独立运行版
* `Source code.zip` —— 源码包
* `Source code.tar.gz`

---

### ⚠️ 注意事项

* 无需安装 Python
* 建议在 Windows 10/11 上运行
* 某些杀毒软件可能误报，这是 PyInstaller 的普遍现象

---

## 📄 开源协议

本项目采用 **MIT License**

---

## 👨‍💻 作者

**orangetect**
GitHub: [https://github.com/orangetect](https://github.com/orangetect)

欢迎提交 Issue 或 PR！
如果本项目对你有帮助，请点亮 ⭐ Star！

---

---

# 🇬🇧 English Version

# 🧰 PDF to JPG Converter

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12+-blue?logo=python">
  <img src="https://img.shields.io/badge/License-MIT-green">
  <img src="https://img.shields.io/badge/GUI-Tkinter-yellow">
  <img src="https://img.shields.io/badge/Build-PyInstaller-orange">
</p>

A lightweight desktop application based on **Python + Tkinter** that converts PDF pages into high-quality JPG images.
Supports page selection, batch export, and an intuitive GUI.

---

## 📚 Table of Contents

* [Features](#features)
* [Screenshot](#screenshot)
* [Usage](#usage)
* [Custom Page Selection](#custom-page-selection)
* [Build EXE](#build-exe)
* [Project Structure](#project-structure)
* [Dependencies](#dependencies)
* [Release Notes](#release-notes)
* [License](#license)
* [Author](#author)

---

## 🌟 Features

✔ Convert PDF to JPG
✔ Support custom page ranges (e.g., `1,3,5-8`)
✔ High-quality rendering (PyMuPDF)
✔ Simple Tkinter GUI
✔ Fully offline
✔ Can be packaged as a Windows EXE

---

## 🖼 Screenshot

```
![App Screenshot](assets/screenshot.png)
```

---

## 🚀 Usage

### Method 1: Use the prebuilt EXE

1. Download the latest release from GitHub
2. Run the `.exe` file
3. Select your PDF
4. Choose output folder
5. Click **Start**

---

### Method 2: Run from source

Install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
python pdf_to_jpg_gui.py
```

---

## 🔢 Custom Page Selection

| Input      | Meaning        |
| ---------- | -------------- |
| `1`        | Page 1         |
| `1-6`      | Pages 1–6      |
| `3,7,10`   | Selected pages |
| `2,5-8,12` | Mixed format   |
| `all`      | All pages      |

---

## 📦 Build EXE

```bash
pyinstaller -F -w -i icon.ico -n "PDFtoJPG" pdf_to_jpg_gui.py
```

---

## 📁 Project Structure

```
pdf-to-jpg-converter/
 ├── pdf_to_jpg_gui.py
 ├── requirements.txt
 ├── README.md
 ├── LICENSE
 ├── icon.ico
 └── assets/
```

---

## 📄 Dependencies

* PyMuPDF
* Pillow
* Tkinter (built-in)

---

## 📦 Release Notes

Release notes may include:

* Added: custom page selection
* Improved PDF rendering speed
* Bug fixes
* UI improvements

Downloads:

* **Windows EXE build**
* **Source code (.zip / .tar.gz)**

---

## 📄 License

MIT License

---

## 👨‍💻 Author

**orangetect**
GitHub: [https://github.com/orangetect](https://github.com/orangetect)

If this project helped you, please ⭐ Star it!

---

如果你需要，我可以继续为你：
✅ 生成 `README.zh-CN.md` & `README.en-US.md` 两个独立文件
✅ 制作自动生成 README 的脚本
✅ 添加更多徽章 / 目录自动生成工具

需要吗？
