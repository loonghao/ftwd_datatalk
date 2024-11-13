# Import built-in modules
import os
from tempfile import mkdtemp

# Import third-party modules
import click
from datatalk.core import DataTalk

# Import local modules
from ftwd_datatalk.analyzers.annual import AnnualDataAnalysis
from ftwd_datatalk.analyzers.assets import AssetsDataAnalysis
from ftwd_datatalk.exporters.annual import AnnualDataExporter
from ftwd_datatalk.exporters.assets import ExcelExporter
from ftwd_datatalk.extractors.excel import ExcelDataExtractor
from ftwd_datatalk.filesystem import get_config_file


@click.group()
def cli():
    click.echo("Welcome to FTWD DataTalk!")
    click.echo("Please use the 'assets' or 'annual' commands.")
    click.echo(f"Loading config from {get_config_file()}")


@cli.command("assets")
@click.argument("excel_files", nargs=-1)
def assets(excel_files):
    output = mkdtemp("datatalk")
    excel_extractor = ExcelDataExtractor(files=excel_files)
    project_data_analysis = AssetsDataAnalysis()
    export = ExcelExporter(output_path=output)

    api = DataTalk(extractor=excel_extractor,
                   analyzer=project_data_analysis,
                   exporter=export)
    api.run()
    os.startfile(output)


@cli.command("annual")
@click.argument("excel_files", nargs=-1)
def annual(excel_files):
    output = mkdtemp("datatalk")
    excel_extractor = ExcelDataExtractor(files=excel_files)
    project_data_analysis = AnnualDataAnalysis()
    export = AnnualDataExporter(output_path=output)

    api = DataTalk(extractor=excel_extractor,
                   analyzer=project_data_analysis,
                   exporter=export)
    api.run()
    os.startfile(output)
