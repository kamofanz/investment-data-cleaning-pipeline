import fitz
import pandas as pd
import re
from pathlib import Path

# Create folders
Path("data").mkdir(exist_ok=True)
Path("output").mkdir(exist_ok=True)

pdf_path = Path("data/sample_report.pdf")

# Create sample PDF if missing
if not pdf_path.exists():
    print("Creating sample_report.pdf...")
    doc = fitz.open()
    page = doc.new_page()
    text = """
    INVESTMENT REPORT - Q2 2026
    2026-01-15 | ETF | SATRIX 40 | R 15,000.00
    2026-02-10 | SHARE | Naspers | R 23,500.50
    2026-03-05 | BOND | RSA R2030 | R 10,000.00
    2026-04-20 | ETF | S&P 500 | R 18,250.75
    TOTAL: R 66,751.25
    """
    page.insert_text((50, 50), text)
    doc.save(str(pdf_path))
    print(f"Created {pdf_path}")

# Read PDF
print(f"Reading {pdf_path}...")
doc = fitz.open(str(pdf_path))
full_text = ""
for p in doc:
    full_text += p.get_text() + "\n"

# PROPER CLEANING with regex
pattern = r"(\d{4}-\d{2}-\d{2})\s*\|\s*([^|]+)\s*\|\s*([^|]+)\s*\|\s*R\s*([\d,]+\.\d{2})"
matches = re.findall(pattern, full_text)

cleaned_data = []
for date, inv_type, asset, amount in matches:
    cleaned_data.append({
        "Date": date,
        "Type": inv_type.strip(),
        "Asset": asset.strip(),
        "Amount": float(amount.replace(",", ""))
    })

df = pd.DataFrame(cleaned_data)

# Save
output_path = Path("output/cleaned_data.xlsx")
df.to_excel(output_path, index=False)

print(f"✅ Clean file saved to: {output_path}")
print(df)
print(f"\nTotal Investments: R {df['Amount'].sum():,.2f}")