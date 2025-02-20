from abc import ABC, abstractmethod


class ReportGenerator(ABC):
    @abstractmethod
    def generate_report(self, data):
        pass

    @abstractmethod
    def save_report(self, filename):
        pass


class PDFReportGenerator(ReportGenerator):
    def generate_report(self, data):
        return f'PDF Report Content: {data}'

    def save_report(self, filename):
        print(f'Saving PDF Report to {filename}.pdf')


class ExcelReportGenerator(ReportGenerator):
    def generate_report(self, data):
        return f'Excel Report Content: {data}'

    def save_report(self, filename):
        print(f'Saving Excel Report to {filename}.xlsx')


class HTMLReportGenerator(ReportGenerator):
    def generate_report(self, data):
        return f'<html><body>{data}</body></html>'

    def save_report(self, filename):
        print(f'Saving HTML Report to {filename}.html')
