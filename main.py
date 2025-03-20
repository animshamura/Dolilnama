import re
import docx
import spacy
import os
from flask import Flask, request, render_template
from PyPDF2 import PdfReader
from transformers import pipeline

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def extract_text_from_docx(file_path):
    doc = docx.Document(file_path)
    return "\n".join([para.text for para in doc.paragraphs])

def extract_text_from_pdf(file_path):
    reader = PdfReader(file_path)
    return "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])

def proofread_text(text):
    grammar_checker = pipeline("text2text-generation", model="facebook/bart-large-cnn")
    proofread_text = grammar_checker(text, max_length=1024, do_sample=False)[0]['generated_text']
    return proofread_text

def extract_legal_entities(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    entities = {ent.label_: ent.text for ent in doc.ents if ent.label_ in ["PERSON", "GPE", "DATE", "ORG"]}
    return entities

def process_land_document(file_path, file_type):
    if file_type == "docx":
        text = extract_text_from_docx(file_path)
    elif file_type == "pdf":
        text = extract_text_from_pdf(file_path)
    else:
        raise ValueError("Unsupported file type")
    
    proofread_text_content = proofread_text(text)
    legal_entities = extract_legal_entities(proofread_text_content)
    
    return proofread_text_content, legal_entities

@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        file = request.files["file"]
        if file:
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)
            file_type = file.filename.split(".")[-1]
            proofread_text_content, legal_entities = process_land_document(file_path, file_type)
            return render_template("result.html", text=proofread_text_content, entities=legal_entities)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
