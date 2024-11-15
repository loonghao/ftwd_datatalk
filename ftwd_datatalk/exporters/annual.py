# Import third-party modules
import xlsxwriter

# Import local modules
from ftwd_datatalk.exporters.assets import ExcelExporter
from ftwd_datatalk.filesystem import get_config


class AnnualDataExporter(ExcelExporter):
    output_name = get_config("annual").output_name

    def export_data(self, data):
        print("export data to excel file: {}".format(self.file_path))
        workbook = xlsxwriter.Workbook(self.file_path)
        worksheet = workbook.add_worksheet()
        worksheet.write_row(0, 0, data[0].keys())
        for row_num, row_data in enumerate(data, 1):
            for col_num, (key, value) in enumerate(row_data.items()):
                worksheet.write(row_num, col_num, value)
        workbook.close()
