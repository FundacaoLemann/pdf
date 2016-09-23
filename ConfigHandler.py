import os
import json
from JinjaBaseClass import JinjaBaseClass


class ConfigHandler(JinjaBaseClass):

    """The goal of this class is to manipulate templates and generate it's
    outputs """

    #TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), 'report_definitions')

    def __init__(self, config_name, global_config_path):
        super(ConfigHandler, self).__init__()
        self.config_name = config_name
        if global_config_path == '':
            self.global_config_path = os.path.join(os.path.dirname(__file__), 'report_definitions', self.config_name, 'config.json')
        else:
            self.global_config_path = global_config_path

    def __repr__(self):
        return "<ConfigHandler object: '{}'>".format(self.config_name)


    def _get_template_rendered(self, data, *args, **kwargs):
        template = self._get_template(self.global_config_path)
        rendered = template.render(**data)
        return rendered

    def _get_config_data(self, date):
        date_ini = self._get_date_timedelta(date, -7)
        date_end = self._get_date_timedelta(date, 0)
        data = {
            "REPORT_CODE": self.config_name,
            "REF_DATE": date_end,
            "DATE_INI": date_ini,
            "DATE_END": date_end,
            "REF_DATE_NODASH": date_end.strftime('%Y%m%d'),
        }
        return data


    def get_configs(self, date):
        data = self._get_config_data(date)
        result = self._get_template_rendered(data)
        return result

    def get_configs_json(self, date):
        return json.loads(self.get_configs(date))
