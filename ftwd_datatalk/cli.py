# Import third-party modules
import click
from datatalk.core import DataTalk

# Import local modules
from ftwd_datatalk.analyzers.annual import AnnualDataAnalysis
from ftwd_datatalk.analyzers.assets import AssetsDataAnalysis
from ftwd_datatalk.exporters.annual import YearDataExporter
from ftwd_datatalk.exporters.assets import ExcelExporter
from ftwd_datatalk.extractors.excel import ExcelDataExtractor


@click.group()
def cli():
    pass


@cli.command("assets")
@click.option("--excel", type=click.Path(exists=True), multiple=True)
@click.option("--output", type=click.Path())
def assets(excel, output):
    excel_extractor = ExcelDataExtractor(files=excel)
    project_data_analysis = AssetsDataAnalysis()
    export = ExcelExporter(output_path=output)

    api = DataTalk(extractor=excel_extractor,
                   analyzer=project_data_analysis,
                   exporter=export)
    api.run()


@cli.command("annual")
@click.option("--excel", type=click.Path(exists=True), multiple=True)
@click.option("--output", type=click.Path())
def annual(excel, output):
    excel_extractor = ExcelDataExtractor(files=excel)
    project_data_analysis = AnnualDataAnalysis()
    export = YearDataExporter(output_path=output)

    api = DataTalk(extractor=excel_extractor,
                   analyzer=project_data_analysis,
                   exporter=export)
    api.run()
