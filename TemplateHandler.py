import os
from datetime import datetime
from jinja2 import Environment, FileSystemLoader


class TemplateHandler(object):
    
    """The goal os this class is to manipulate templates and generate it's 
    outputs """

    TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), 'templates')

    def __init__(self):
        super(TemplateHandler, self).__init__()
        self._set_template_engine()
        self._set_filters()

    def _datetimeformat_filter(self, value, format='%Y-%m-%d %H:%M:%S'):
        return value.strftime(format)


    def _set_template_engine(self):
        loader = FileSystemLoader(self.TEMPLATE_DIR)
        self.template_engine = Environment(loader=loader)

    def _set_filters(self):
        self.template_engine.filters.update({
            'datetimeformat': self._datetimeformat_filter
        })

    def _get_template(self, *args, **kwargs):
        template = self.template_engine.get_template(*args, **kwargs)
        return template

    def main(self, *args, **kwargs):
        template = self._get_template('barchart.html')
        template_data = {
            "former": {
                "name": "Judite Aparecida",
                "email": "judite.aparecida@email.com"
            },
            "created_at": datetime.now(),
            "REPORT_NAME": "Relatorio Semanal",
            "DATE_INI": "2016-07-01",
            "DATE_END": "2016-08-01",
            "CHART_NAME": "% de alunos que acessaram a plataforma",
            "IMG": {
                "src": "{TMPL_DIR}/assets/sample/output.png".format(TMPL_DIR=self.TEMPLATE_DIR),
                "width": "100%",
                "title": "Numero de alunos que acessaram a plataforma",
            }
        }
        rendered = template.render(**template_data)
        return rendered

if __name__ == '__main__':
    rendered = TemplateHandler().main()
    open('ab.html', 'w').write(rendered)