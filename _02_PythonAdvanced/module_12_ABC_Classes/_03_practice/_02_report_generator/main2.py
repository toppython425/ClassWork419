from classes2 import PDFReportGenerator, ExcelReportGenerator, HTMLReportGenerator

if __name__ == '__main__':
    pdf_gen = PDFReportGenerator()
    pdf_content = pdf_gen.generate_report('Sales data')
    pdf_gen.save_report('sales_report')
    print()

    excel_gen = ExcelReportGenerator()
    excel_content = excel_gen.generate_report('Inventory List')
    excel_gen.save_report('inventory_report')
    print()

    html_gen = HTMLReportGenerator()
    html_content = html_gen.generate_report('User Statistics')
    html_gen.save_report('user_stats')
    print()
