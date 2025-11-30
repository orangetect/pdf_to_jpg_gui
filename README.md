# PDF to JPG Converter

🌐 Languages:  
[English](README_EN.md) | [中文](README.md)


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

![image](https://github.com/orangetect/pdf_to_jpg_gui/blob/main/assets/124050.png)


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
| `2,4,8`     | 指定页      |
| `3,6-10,12` | 混合组合     |
| `all`       | 全部页      |

---

## 📦 打包成 EXE

```bash
pyinstaller -F -w -i icon.ico -n "PDF转图片工具" pdf_to_jpg_gui.py
```

> 如果提示 `Icon input file not found`，请确认 `icon.ico` 是否存在。

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

发布页内容可包含：

### 🆕 版本更新内容（示例）

* 新增：自定义页码批量导出
* 优化：大 PDF 文件解析速度
* 修复：某些 PDF 无法导出的问题
* 新增：自动输出目录检测

### 📥 下载内容

* `PDF转图片工具.exe` —— Windows 64 位独立版本
* `Source code.zip` —— 源码包
* `Source code.tar.gz`

### ⚠️ 注意事项

* 不需要安装 Python
* 建议在 Windows 10/11 上运行
* 如果杀毒软件误报，属于正常现象（PyInstaller 打包常见）

---

## 📄 开源协议

本项目采用 **MIT License**

---

## 👨‍💻 作者

**orangetect**
GitHub: [https://github.com/orangetect](https://github.com/orangetect)

欢迎提交 Issue 或 PR！
如果对你有帮助，请点亮 ⭐Star！
