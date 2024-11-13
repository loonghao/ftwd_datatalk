# Import third-party modules
from datatalk.analyzer import DataAnalyzer

# Import local modules
from ftwd_datatalk.filesystem import get_config


class AnnualDataAnalysis(DataAnalyzer):

    def __init__(self):
        self.config = get_config("assets")
        self.excel_header = self.config.excel_header

    def analyse_data(self, datas):
        all_data = []
        for index, data in enumerate(datas, 1):
            for item in data:
                item["月份"] = index
                all_data.append(item)
        return all_data
