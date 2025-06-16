# 🖼️ OCR to JSON Web App

A web application where users can upload images (JPG, PNG) or PDF files and extract readable text using Optical Character Recognition (OCR). 
The extracted text is returned in JSON format. Built using Python (Flask), Tesseract OCR, and Pillow, the app also features a minimal, modern UI with image preview and animated background.

---

### 🛠 Tech Stack

**Backend:** Python, Flask  
**OCR Engine:** Tesseract OCR  
**Image Handling:** Pillow  
**Frontend:** HTML, CSS, JavaScript  
**Deployment:** Gunicorn (server) + Render (hosting)

---

### ✨ Features

- Upload image or PDF files from local device  
- Preview uploaded image in small left panel  
- Extracts and displays text content as JSON  
- Clean, user-friendly interface with animated background  
- Fully deployable on cloud platforms like Render  
- Works locally on Windows with custom Tesseract path

---

### 💻 Local Development

Clone the repository and run it locally using the steps below:

```bash
git clone https://github.com/yourusername/ocr-json-parser.git
cd ocr-json-parser
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
