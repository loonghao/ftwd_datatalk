# Import built-in modules
from typing import IO
from typing import Iterator

# Import third-party modules
from datatalk.extractor import DataExtractor
import python_calamine


class ExcelDataExtractor(DataExtractor):

    def __init__(self, files):
        self.files = files

    @staticmethod
    def iter_excel_calamine(file: IO[bytes]) -> Iterator[dict[str, object]]:
        workbook = python_calamine.CalamineWorkbook.from_path(file)
        for sheet_name in workbook.sheet_names:
            rows = iter(workbook.get_sheet_by_name(sheet_name).to_python())
            headers = list(map(str, next(rows)))
            for row in rows:
                yield dict(zip(headers, row))

    def extract_data(self):
        for excel_file in self.files:
            yield self.iter_excel_calamine(excel_file)
