from fpdf import FPDF
from datetime import datetime

class Invoice(FPDF):
    def header(self):
        self.set_font("Helvetica", "B", 20)
        self.set_text_color(40, 116, 166) # Tech Blue
        self.cell(0, 10, "DOMINION TECH SOLUTIONS", ln=True, align="C")
        self.set_font("Helvetica", "", 10)
        self.set_text_color(0, 0, 0)
        self.cell(0, 5, "Quality Laptops for University Students", ln=True, align="C")
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()} | Generated on {datetime.now().strftime('%Y-%m-%d')}", align="C")

def create_invoice(customer, item, price):
    pdf = Invoice()
    pdf.add_page()
    
    # Customer Details
    pdf.set_font("Helvetica", "B", 12)
    pdf.cell(0, 10, f"INVOICE FOR: {customer}", ln=True)
    pdf.set_font("Helvetica", "", 11)
    pdf.cell(0, 10, f"Date: {datetime.now().strftime('%d %B, %Y')}", ln=True)
    pdf.ln(5)

    # Table Header
    pdf.set_fill_color(230, 230, 230)
    pdf.set_font("Helvetica", "B", 11)
    pdf.cell(140, 10, "Description", border=1, fill=True)
    pdf.cell(50, 10, "Amount (GHS)", border=1, fill=True, ln=True)

    # Table Body
    pdf.set_font("Helvetica", "", 11)
    pdf.cell(140, 10, item, border=1)
    pdf.cell(50, 10, f"{price:,.2f}", border=1, ln=True)

    # Total
    pdf.ln(5)
    pdf.set_font("Helvetica", "B", 12)
    pdf.cell(140, 10, "TOTAL DUE:", align="R")
    pdf.cell(50, 10, f"GHS {price:,.2f}", ln=True)

    # Thank you note
    pdf.ln(20)
    pdf.set_font("Helvetica", "I", 10)
    pdf.multi_cell(0, 5, "Thank you for choosing Dominion Tech Solutions! \nAll laptops come with a standard warranty. \nContact: +233 (Your Number)")

    filename = f"Invoice_{customer.replace(' ', '_')}.pdf"
    pdf.output(filename)
    print(f"\n[✔] Success: {filename} has been created!")

if __name__ == "__main__":
    print("--- Dominion Tech Invoice Generator ---")
    c_name = input("Customer Name: ")
    l_item = input("Laptop Model & Specs: ")
    l_price = float(input("Final Price (GHS): "))
    
    create_invoice(c_name, l_item, l_price)