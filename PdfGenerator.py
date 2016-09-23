from weasyprint import HTML
import tempfile
import logging
from TemplateHandler import TemplateHandler
from ContentHandler import ContentHandler
from ConfigHandler import ConfigHandler


weasyprint_logger=logging.getLogger('weasyprint')
weasyprint_logger.setLevel(logging.ERROR)


class PdfGenerator(object):

    """
    The goal is to generate the pdf given a 'report_name' and a date reference
    """

    def __init__(self, report_code, date, global_config):
        super(PdfGenerator, self).__init__()
        self.html_temp_file = tempfile.mkstemp(suffix='.html')[1]
        self.pdf_temp_file = tempfile.mkstemp(suffix='.pdf')[1]
        self.report_code = report_code
        self.date = date
        self.global_config = global_config
        self._config = ConfigHandler(self.report_code, self.global_config).get_configs_json(
            self.date)
        self._template = TemplateHandler(self.report_code)
        self._content = ContentHandler(self.report_code, self._config)
        self.logger = logging.getLogger(__name__)
        self.logger.info('starting report generator for {}...'.format(
            self.report_code))

    def __repr__(self):
        return '<PdfGenerator object ({}, {})>'.format(self.report_code,
            self.date)


    def generate(self):
        self.logger.info('getting data...')
        data = self._content.get_data()

        self.logger.info('applying data into template...')
        html_content = self._template._get_template_rendered(data)

        self.logger.info('writing the html file...')
        open(self.html_temp_file, 'w').write(html_content)

        self.logger.info('exporting the html file to pdf...')
        weasy_html = HTML(self.html_temp_file)
        weasy_html.write_pdf(self.pdf_temp_file)

        return True

    def get_html_file(self):
        return self.html_temp_file

    def get_output_file(self):
        return self.pdf_temp_file

