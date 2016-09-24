import os
import click
from PdfGenerator import PdfGenerator


@click.group()
def cli():
    """
    "PDF Reports Generator"
    """
    pass


class Context(object):

    def __init__(self):
        self.home = os.getcwd()


pass_context = click.make_pass_decorator(Context, ensure=True)


@cli.command()
@click.argument('report_code')
@click.argument('date')
@pass_context
def generate(ctx, report_code, date):
    """
    The reports are generated inside a folder with the 'report_code' as \
    folder name.
    """
    params = {
        'report_code': report_code,
        'date': date,
        'path': ctx.home
    }
    pdf = PdfGenerator(**params)
    pdf.generate()
    output = pdf.get_output_file()
    click.echo("The pdf file was exported to {}".format(output))


if __name__ == '__main__':
    cli()
