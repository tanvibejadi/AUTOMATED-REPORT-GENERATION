import csv
from fpdf import FPDF
import statistics

def read_data(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data = [{"Name": row["Name"], "Score": int(row["Score"])} for row in reader]
    return data

def analyze_data(data):
    scores = [item["Score"] for item in data]
    summary = {
        "Total Students": len(data),
        "Average Score": round(statistics.mean(scores), 2),
        "Highest Score": max(scores),
        "Lowest Score": min(scores),
    }
    return summary

class PDFReport(FPDF):
    def header(self):
        self.set_font("Arial", "B", 16)
        self.cell(0, 10, "AUTOMATED REPORT GENERATION", border=False, ln=True, align='C')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", align='C')

    def add_summary(self, summary):
        self.set_font("Arial", "", 12)
        self.cell(0, 10, "Summary Statistics:", ln=True)
        for key, value in summary.items():
            self.cell(0, 10, f"{key}: {value}", ln=True)
        self.ln(10)

    def add_table(self, data):
        self.set_font("Arial", "B", 12)
        self.cell(90, 10, "Name", 1)
        self.cell(40, 10, "Score", 1)
        self.ln()

        self.set_font("Arial", "", 12)
        for row in data:
            self.cell(90, 10, row["Name"], 1)
            self.cell(40, 10, str(row["Score"]), 1)
            self.ln()

def generate_pdf_report(data, summary, filename):
    pdf = PDFReport()
    pdf.add_page()
    pdf.add_summary(summary)
    pdf.add_table(data)
    pdf.output(filename)

if __name__ == "__main__":
    data = read_data("data.csv")
    summary = analyze_data(data)
    generate_pdf_report(data, summary, "report.pdf")
    print("Report generated: report.pdf")
