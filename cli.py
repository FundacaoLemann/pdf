import click
from PdfGenerator import PdfGenerator

@click.group(help="PDF Reports Generator")
def cli():
    return True

@cli.command()
@click.argument('report_code')
@click.argument('date')
@click.pass_context
def generate(ctx, report_code, date):
	pdf = PdfGenerator(report_code, date)
	pdf.generate()
	output = pdf.get_output_file()
	click.echo("The pdf file was exported to {}".format(output))


if __name__ == '__main__':
    cli()
