import click
from PdfGenerator import PdfGenerator

@click.group(help="PDF Reports Generator")
def cli():
    return True

@cli.command()
@click.argument('report_code')
@click.argument('date')
@click.option('--global_config', '-gc', default='')
@click.pass_context
def generate(ctx, report_code, date, global_config):
	pdf = PdfGenerator(report_code, date, global_config)
	pdf.generate()
	output = pdf.get_output_file()
	click.echo("The pdf file was exported to {}".format(output))



if __name__ == '__main__':
    cli()
