# PDF to JPG Converter

🌐 Read this in other languages: [中文](README.md)

...


# 🇬🇧 English Version

# 🧰 PDF to JPG Converter

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12+-blue?logo=python">
  <img src="https://img.shields.io/badge/License-MIT-green">
  <img src="https://img.shields.io/badge/GUI-Tkinter-yellow">
  <img src="https://img.shields.io/badge/Build-PyInstaller-orange">
</p>

A lightweight desktop application based on **Python + Tkinter** that converts PDF pages into high-quality JPG images.
Supports page selection, batch export, and is easy to use via GUI.

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

✔ Convert PDFs to JPG images
✔ Supports custom page ranges (e.g., `1,3,5-8`)
✔ High-quality PDF rendering
✔ Easy-to-use Tkinter GUI
✔ Fully offline
✔ Can be packaged into a Windows EXE

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
| `1-6`      | Pages 1 to 6   |
| `3,7,10`   | Specific pages |
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

* New feature: custom page selection
* Improved PDF rendering speed
* Bug fixes
* UI improvements

Downloads:

* **EXE build**
* **Source code (.zip / .tar.gz)**

---

## 📄 License

MIT License

---

## 👨‍💻 Author

**orangetect**
GitHub: [https://github.com/orangetect](https://github.com/orangetect)

If this project helped you, please give it a ⭐ Star!
