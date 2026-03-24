# 🔐 Binary Secret Communicator

A lightweight web application built with **Python** and **Streamlit** to explore the relationship between human language and machine-level data (0s and 1s).

## 🚀 Overview
Ever wondered how your name looks inside the memory of an **Apple M1 chip**? This tool translates any text (English, Chinese, or Estonian) into its underlying **Binary** and **Hexadecimal** representations.

### Key Features:
- **Text to Binary:** Convert strings like "刘炜" or "Tallinn" into 0b... sequences.
- **Binary to Text:** Decode raw binary strings back into human-readable characters.
- **Unicode Mapping:** Visualizes how different characters require different memory sizes.

## 🛠️ Tech Stack
- **Language:** Python 3.x
- **Framework:** [Streamlit](https://streamlit.io/)
- **Encoding:** Unicode (UTF-8)

## 📖 How it Works
Computers don't understand "A" or "刘". They use a "lookup table" called **Unicode**:
1. The character **'A'** is mapped to the number **65**, which is `0b1000001`.
2. The character **'刘'** is mapped to the number **21016**, which is `0b101001000011000`.

This app acts as the "microscope" to see those raw bits in action.

## 🚦 Quick Start
If you want to run this locally on your Mac:
1. Clone the repo.
2. Install requirements: `pip install streamlit`
3. Run the app: `streamlit run app.py`

---
*Created as part of my journey into AI and Computer Architecture.*
