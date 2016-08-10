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
        template = self._get_template('default.html')
        template_data = {
            "former": {
                "name": "Judite Aparecida",
                "email": "judite.aparecida@email.com"
            },
            "created_at": datetime.now(),
            "REPORT_NAME": "Relatorio Semanal Khan",
            "DATE_INI": "2016-07-01",
            "DATE_END": "2016-08-01",
            "charts": [
                {
                    "title": "% de alunos que acessaram a plataforma",
                    "src": "{TMPL_DIR}/assets/sample/output.png".format(TMPL_DIR=self.TEMPLATE_DIR),
                    "width": "100%",
                },
                {
                    "title": "lorem ipsum bl a bklas",
                    "src": "{TMPL_DIR}/assets/sample/output.png".format(TMPL_DIR=self.TEMPLATE_DIR),
                    "width": "100%",
                }
            ],
            "tables": [
                {
                    "title": "Lorem Some cool title",
                    'meta': '<table border="0" class="dataframe table meta-info">\n  <tbody>\n    <tr>\n      <th>turma</th>\n      <td>CARMELIALOFF 4B 2016CARMELIALOFF 4C 2016CARMEL...</td>\n    </tr>\n    <tr>\n      <th>total_alunos</th>\n      <td>71</td>\n    </tr>\n    <tr>\n      <th>usuarios</th>\n      <td>5</td>\n    </tr>\n    <tr>\n      <th>dominam_5_hab</th>\n      <td>2</td>\n    </tr>\n    <tr>\n      <th>inativos</th>\n      <td>65</td>\n    </tr>\n  </tbody>\n</table>',
                    "html": '<table border="0" class="dataframe table table-bordered detailed">\n  <thead>\n    <tr style="text-align: right;">\n      <th>turma</th>\n      <th>total_alunos</th>\n      <th>usuarios</th>\n      <th>dominam_5_hab</th>\n      <th>inativos</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>CARMELIALOFF 4B 2016</td>\n      <td>22</td>\n      <td>2</td>\n      <td>1</td>\n      <td>19</td>\n    </tr>\n    <tr>\n      <td>CARMELIALOFF 4C 2016</td>\n      <td>22</td>\n      <td>3</td>\n      <td>1</td>\n      <td>19</td>\n    </tr>\n    <tr>\n      <td>CARMELIALOFF 5A 2016</td>\n      <td>27</td>\n      <td>0</td>\n      <td>0</td>\n      <td>27</td>\n    </tr>\n  </tbody>\n</table>',
                }
            ]
        }
        rendered = template.render(**template_data)
        return rendered

if __name__ == '__main__':
    rendered = TemplateHandler().main()
    open('ab.html', 'w').write(rendered)