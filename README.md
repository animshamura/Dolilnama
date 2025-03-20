
# 📜 Dolilnama - AI Land Document Proofreader

## 🌟 Project Overview
Land documents are the backbone of ownership, security, and legacy. A single mistake can lead to disputes, delays, or even loss of assets. **Dolilnama** is here to change that. 

Dolilnama is an **AI-powered land document proofreader** that ensures your legal papers are flawless, accurate, and legally sound. From detecting grammatical errors to highlighting critical legal entities such as **names, locations, dates, and organizations**, Dolilnama safeguards your documents with cutting-edge **Natural Language Processing (NLP) and AI models**.

🔹 **Precision-driven proofreading** for legal documents  
🔹 **AI-backed legal term extraction** to prevent costly mistakes  
🔹 **User-friendly, intuitive interface** for effortless document review  

Your land, your legacy—**Dolilnama protects what matters most.**

---

## 🚀 Features
✅ **Seamless document upload** (PDF/DOCX)  
✅ **AI-powered grammar and legal accuracy checks**  
✅ **Named Entity Recognition (NER) for legal terms**  
✅ **Clean, responsive web interface** for ease of use  

---

## 🔧 Installation Guide
### 1️⃣ Install pip (if not installed)
Ensure `pip` is installed with:
```bash
python -m ensurepip --default-pip
```
Upgrade to the latest version:
```bash
pip install --upgrade pip
```

### 2️⃣ Install Required Dependencies
Ensure you have **Python 3.7+** installed, then run:
```bash
pip install flask spacy transformers PyPDF2 python-docx
python -m spacy download en_core_web_sm
```

---

## 📂 Project Structure
```
/dolilnama
│── app.py               # Main Python script
│── /templates           # HTML templates
│   │── index.html       # Upload page
│   └── result.html      # Proofreading result page
│── /uploads (auto-created)  # Stores uploaded files
│── requirements.txt     # Dependencies
```

---

## 🎯 How to Run Dolilnama
1️⃣ **Navigate to the project directory:**
   ```bash
   cd dolilnama
   ```

2️⃣ **Run the Flask app:**
   ```bash
   python app.py
   ```

3️⃣ **Open the web interface:**
   Visit **http://127.0.0.1:5000/** in your browser.

4️⃣ **Upload your document** and let Dolilnama ensure it is error-free and legally sound.

---

## 🔮 Future Enhancements
🚀 **Real-time error highlighting** directly in the document  
📂 **Downloadable, AI-corrected document files**  
📜 **Expanded legal document support (leases, deeds, etc.)**  

---

## 📜 License
Dolilnama is **open-source** and free to use. Your contributions help us build a future where legal document errors are a thing of the past! ✨

