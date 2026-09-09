# Investment Data Cleaning Pipeline 📊

> Automated PDF to Excel pipeline that saves 5+ hours of manual data entry.

An end-to-end data cleaning project built with Python, designed to extract, clean, and transform messy investment report PDFs into analysis-ready Excel files.

**Live Repo:** https://github.com/kamofanz/investment-data-cleaning-pipeline

### 🚀 Problem Solved
Financial investment reports come as scanned PDFs with inconsistent formatting. Manual cleaning is slow and error-prone. This pipeline automates the entire process.

### ✨ Features
- Extracts tables from PDF investment reports
- Cleans inconsistent names, currencies, and dates
- Exports clean data to Excel with formatted sheets
- Modular, reusable code - just add new PDFs to `data/` folder
- Handles missing values and duplicates

### 🛠️ Tech Stack
- **Python 3.10+**
- **Pandas** - data manipulation
- **pdfplumber / PyMuPDF** - PDF extraction
- **OpenPyXL** - Excel export

### 📁 Project Structure
investment-data-cleaning-pipeline/
├── data/           # Raw PDF reports
├── output/         # Cleaned Excel files
├── main.py         # Main pipeline script
├── requirements.txt
└── README.md

### ▶️ How to Run
1. Clone the repo
```bash
git clone https://github.com/kamofanz/investment-data-cleaning-pipeline.git
2. Install dependencies
pip install -r requirements.txt
3. Add your PDFs to `data/` folder
4. Run pipeline
python main.py
Clean Excel file will appear in `output/`!

### 📈 What I Learned
- Building ETL pipelines from scratch
- PDF data extraction and text cleaning
- Git & GitHub workflow (init, commit, push, rebase)
- Writing production-ready, documented Python code

### 👩‍💻 Author
*Kamo* - Aspiring Data Analyst | UJ AI in 4IR
Passionate about automation and turning messy data into insights.

---
