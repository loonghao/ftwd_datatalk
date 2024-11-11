# Import built-in modules
import os.path

# Import third-party modules
from datatalk.exporter import DataExporter
import xlsxwriter


class ExcelExporter(DataExporter):
    output_name = "数据分析报告.xlsx"

    def __init__(self, output_path: str):
        os.makedirs(output_path, exist_ok=True)
        self.file_path = os.path.join(output_path, self.output_name)

    def export_data(self, data):
        print("export data to excel file: {}".format(self.file_path))
        workbook = xlsxwriter.Workbook(self.file_path)
        worksheet = workbook.add_worksheet()
        for row_num, row_data in enumerate(data.items()):
            worksheet.write_column(0, row_num, row_data)
        workbook.close()
