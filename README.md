 

# 🧾 Multi-Language Invoice Extractor

This project is a **Streamlit web application** powered by **Google Gemini (Generative AI)** that extracts and analyzes information from invoice images in multiple languages.

## 🚀 Features

* 📂 Upload invoice images in **JPG, JPEG, or PNG** formats.
* 🌍 Supports invoices written in **multiple languages**.
* 🤖 Uses **Google Gemini 2.5 Flash** model for intelligent invoice analysis.
* 🖼️ Displays uploaded invoice image inside the app.
* 💬 Ask **custom questions** about the invoice (e.g., *"What is the total amount?"*, *"Who is the supplier?"*).
* 📊 Extracts structured details like invoice number, date, customer info, and totals.

## ⚙️ Tech Stack

* **Python**
* **Streamlit** – for building the interactive web app
* **PIL (Pillow)** – for image handling
* **Google Generative AI (Gemini API)** – for invoice understanding

## 📖 How It Works

1. Upload an invoice image.
2. The app displays the uploaded image.
3. Enter a custom question or prompt related to the invoice.
4. The app sends the invoice + prompt to **Gemini AI**.
5. Gemini extracts and returns the relevant information.

## ▶️ Run 

```bash


# Run the app
streamlit run app.py
```

## 🔑 API Key Setup

* Get a Google Gemini API Key from [Google AI Studio](https://ai.google.dev/).
* Replace `"AIza"` in the code with your actual API key.

## 📌 Example Use Cases

* Extracting total amount, tax, and due date from invoices.
* Translating invoice details from different languages.
* Automating expense tracking for businesses.
 
