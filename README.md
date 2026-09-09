# Investment Data Cleaning Pipeline 📊

> Automated PDF → Excel pipeline that saves 5+ hours of manual data entry per report.

An end-to-end ETL project that extracts, cleans, and transforms messy investment report PDFs into analysis-ready Excel files.

**Portfolio:** https://kamofanz.github.io

---

### 🚀 The Problem

Financial investment reports come as scanned PDFs with inconsistent formatting. Manual cleaning is slow and error-prone.

### 💡 The Solution

**PDFs in `data/` → `python main.py` → Clean Excel in `output/`**

1. Extracts tables from PDFs
2. Cleans names, currencies, dates
3. Removes duplicates & handles missing values
4. Exports formatted Excel with openpyxl

### ✨ Features

- Extracts tables from PDF investment reports
- Cleans inconsistent names, currencies, and dates
- Handles missing values and duplicates
- Exports to formatted Excel
- Modular - just add new PDFs to `data/`

### 🛠️ Tech Stack

- Python 3.10+
- pandas - data cleaning
- pdfplumber / PyMuPDF - PDF extraction
- openpyxl - Excel export

### 📁 Project Structure
data/           # Raw PDFs
output/         # Cleaned Excel
main.py         # Pipeline
requirements.txt


### ▶️ How to Run

```bash
git clone https://github.com/kamofanz/investment-data-cleaning-pipeline.git
cd investment-data-cleaning-pipeline
pip install -r requirements.txt
python main.py
```

Before vs After
Before: 50-page PDF with messy tables → manual copy-paste
After: output/cleaned_report.xlsx with:
Sheet 1: Cleaned transactionsSheet 2: Summary by investment type
What I Learned
Building ETL pipelines from scratchPDF data extraction and text cleaningUsing pandas for real-world validationGit & GitHub workflowWriting production-ready Python code🔮 Next Steps
Add CLI args for pathsAdd logging and testsAuto-detect currencyStreamlit dashboard
Author
Kamo Fanz - Python Developer | UJ AI in 4IR
Portfolio: https://kamofanz.github.io
GitHub: https://github.com/kamofanz
Location: Cape Town, South Africa
