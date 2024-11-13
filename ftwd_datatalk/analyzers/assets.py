# Import third-party modules
from datatalk.analyzer import DataAnalyzer
import xlsxwriter

# Import local modules
from ftwd_datatalk.filesystem import get_config
from ftwd_datatalk.fuzzydict import FuzzyDict


class AssetsDataAnalysis(DataAnalyzer):

    def __init__(self):
        self.config = get_config("assets")
        self.excel_header = self.config.excel_header
        self.project_prod_keys = self.config.project_prod_keys
        self.non_project_main_keys = self.config.non_project_main_keys

        self.person_day_count = 0
        self.no_project_days_count = 0
        self.project_prod_day_count = 0
        self.work_day_key = self.config.work_day_key

    def get_key(self, value):

        return self.get_key(value["任务名称"])

    def calculate_person_days(self, value):
        self.person_day_count += float(value[self.work_day_key])

    def calculate_project_days(self, value):
        if "np-" in value["任务名称"]:
            self.no_project_days_count += float(value[self.work_day_key])

    def calculate_project_prod_days(self, value):
        for key in self.project_prod_keys:
            if key in value["任务名称"].lower():
                self.project_prod_day_count += float(value[self.work_day_key])

    def analyse_data(self, datas):
        for data in datas:
            for item in data:
                item = FuzzyDict(item)
                self.calculate_person_days(item)
                self.calculate_project_days(item)
                self.calculate_project_prod_days(item)
        return self.get_results()

    def get_results(self):
        self.excel_header["总投入人天"] = self.person_day_count
        self.excel_header["项目人天"] = round(self.person_day_count - self.no_project_days_count, 4)
        self.excel_header["项目占比"] = "{:.2f}%".format(round(self.excel_header["项目人天"] / self.person_day_count, 4) * 100)
        self.excel_header["非项目人天"] = self.no_project_days_count
        self.excel_header["非项目占比"] = "{:.2f}%".format(
            round(self.excel_header["非项目人天"] / self.person_day_count, 4) * 100)
        self.excel_header["项目制作人天"] = self.project_prod_day_count
        self.excel_header["项目制作占比"] = "{:.2f}%".format(
            round(self.excel_header["项目制作人天"] / self.excel_header["项目人天"], 4) * 100)
        self.excel_header["项目管理人天"] = self.excel_header["项目人天"] - self.excel_header["项目制作人天"]
        self.excel_header["项目管理占比"] = "{:.2f}%".format(
            round(self.excel_header["项目管理人天"] / self.excel_header["项目人天"], 4) * 100)
        return self.excel_header

    def save(self, output_file):
        workbook = xlsxwriter.Workbook(output_file)
        worksheet = workbook.add_worksheet()
        for row_num, row_data in enumerate(self.excel_header.items()):
            worksheet.write_column(0, row_num, row_data)
        workbook.close()
