import logging
import io
import os
from weasyprint import HTML
from TemplateHandler import TemplateHandler
from ContentHandler import ContentHandler
from ConfigHandler import ConfigHandler


weasyprint_logger = logging.getLogger('weasyprint')
weasyprint_logger.setLevel(logging.ERROR)


class PdfGenerator(object):

    """
    The goal is to generate the pdf given a 'report_name' and a date reference
    """

    def __init__(self, report_code, date, **kwargs):
        super(PdfGenerator, self).__init__()
        self.report_code = report_code
        self.date = date
        self._KWARGS = kwargs
        self._config = self._get_config()
        self.html_temp_file = self._get_output_filepath('.html')
        self.pdf_temp_file = self._get_output_filepath('.pdf')
        self._template = TemplateHandler(self.report_code)
        self._content = ContentHandler(self.report_code, self._config)
        self.logger = logging.getLogger(__name__)
        self.logger.info('starting report generator for {}...'.format(
            self.report_code))

    def __repr__(self):
        return '<PdfGenerator object ({}, {})>'.format(
            self.report_code,
            self.date)

    def _get_output_filepath(self, extension):
        filename = "{}{}".format(self._config.get('REPORT_NAME'), extension)
        filepath = os.path.join(self.report_path, filename)
        return filepath

    def _get_root_path(self):
        path = None
        if 'path' in self._KWARGS.keys():
            path = self._KWARGS.get('path')
        else:
            path = os.path.join(os.path.dirname(__file__))
        assert path is not None, "Somehow the root_path is not set"
        return path

    def _get_config(self):
        params = {
            'config_name': self.report_code,
            'date': self.date
        }

        if 'global_config' in self._KWARGS.keys() and \
                self._KWARGS.get('global_config') is not None:
            params.update({
                'global_configs_file': self._KWARGS.get('global_config')
                })

        configs = ConfigHandler(**params).get_configs_json()

        configs.update({'ROOT_PATH': self.root_path})

        return configs

    @property
    def root_path(self):
        return self._get_root_path()

    @property
    def report_path(self):
        result = os.path.join(self.root_path, self.report_code)
        return result

    def ensure_report_dir(self):
        if os.path.isdir(self.report_path):
            return True
        else:
            os.makedirs(self.report_path)
            return True

    def generate(self):
        # ensure the report dir
        self.ensure_report_dir()

        self.logger.info('getting data...')
        data = self._content.get_data()

        self.logger.info('applying data into template...')
        html_content = self._template._get_template_rendered(data)

        self.logger.info('writing the html file...')
        io.open(self.html_temp_file, 'w', encoding='utf-8').write(html_content)

        self.logger.info('exporting the html file to pdf...')
        weasy_html = HTML(self.html_temp_file)
        weasy_html.write_pdf(self.pdf_temp_file)

        return True

    def get_html_file(self):
        return self.html_temp_file

    def get_output_file(self):
        return self.pdf_temp_file
