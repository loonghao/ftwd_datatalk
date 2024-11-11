# Import third-party modules
from datatalk.analyzer import DataAnalyzer
import xlsxwriter


class AssetsDataAnalysis(DataAnalyzer):

    to_excel = {
        "总投入人天": "",
        "项目人天": "",
        "项目占比": "",
        "非项目人天": "",
        "非项目占比": "",
        "项目制作人天": "",
        "项目制作占比": "",
        "项目管理人天": "",
        "项目管理占比": "",

    }
    project_prod_keys = ["srf", "mod", "scan"]
    non_project_main_keys = ["com", "common"]

    def __init__(self):
        self.person_day_count = 0
        self.no_project_days_count = 0
        self.project_prod_day_count = 0


    def calculate_person_days(self, value):
        self.person_day_count += float(value["正常工时"])

    def calculate_project_days(self, value):
        if "np-" in value["任务名称"]:
            self.no_project_days_count += float(value["正常工时"])


    def calculate_project_prod_days(self, value):
        for key in self.project_prod_keys:
            if key in value["任务名称"]:
                self.project_prod_day_count += float(value["正常工时"])

    def analyse_data(self, datas):
        for data in datas:
            for item in data:
                print(item)
                self.calculate_person_days(item)
                self.calculate_project_days(item)
                self.calculate_project_prod_days(item)
        return self.get_results()

    def get_results(self):
        self.to_excel["总投入人天"] = self.person_day_count
        self.to_excel["项目人天"] = round(self.person_day_count - self.no_project_days_count, 4)
        self.to_excel["项目占比"] = "{:.2f}%".format(round(self.to_excel["项目人天"] / self.person_day_count, 4) * 100)
        self.to_excel["非项目人天"] = self.no_project_days_count
        self.to_excel["非项目占比"] = "{:.2f}%".format(round(self.to_excel["非项目人天"] / self.person_day_count, 4) * 100)
        self.to_excel["项目制作人天"] = self.project_prod_day_count
        self.to_excel["项目制作占比"] = "{:.2f}%".format(round(self.to_excel["项目制作人天"] / self.to_excel["项目人天"], 4) * 100)
        self.to_excel["项目管理人天"] = self.to_excel["项目人天"] - self.to_excel["项目制作人天"]
        self.to_excel["项目管理占比"] = "{:.2f}%".format(round(self.to_excel["项目管理人天"] / self.to_excel["项目人天"], 4) * 100)
        print(self.to_excel)
        return self.to_excel


    def save(self, output_file):
        workbook = xlsxwriter.Workbook(output_file)
        worksheet = workbook.add_worksheet()
        for row_num, row_data in enumerate(self.to_excel.items()):
            worksheet.write_column(0, row_num, row_data)
        workbook.close()
