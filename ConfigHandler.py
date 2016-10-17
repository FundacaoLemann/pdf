import os
import json
from JinjaBaseClass import JinjaBaseClass


class ConfigHandler(JinjaBaseClass):

    """The goal of this class is to manipulate templates and generate it's
    outputs """

    TEMPLATE_DIR = os.path.join(
        os.path.dirname(__file__), 'report_definitions')

    def __init__(self, config_name, date, *args, **kwargs):
        super(ConfigHandler, self).__init__()
        self.config_name = config_name
        self._KWARGS = kwargs
        self.date = date
        self._global_configs = self._get_global_configs()
        self._global_configs_file = self._get_global_configs_file()

    def __repr__(self):
        return "<ConfigHandler object: '{}'>".format(self.config_name)

    def _get_global_configs(self):
        result = None
        if 'global_configs' in self._KWARGS.keys() or\
                'global_configs_file' in self._KWARGS.keys():
            result = True
        return result

    def _get_global_configs_file(self):
        result = None
        if self._global_configs:
            if 'global_configs_file' in self._KWARGS.keys():
                result = self._KWARGS.get('global_configs_file')
            else:
                result = "{}_global{}".format(self.config_name, '.json')
        return result

    def _get_template_rendered(self, file, data, *args, **kwargs):
        template = self._get_template(file)
        rendered = template.render(**data)
        return rendered

    def _get_config_data(self,):
        date_ini = self._get_date_timedelta(self.date, -7)
        date_end = self._get_date_timedelta(self.date, 0)
        data = {
            "REPORT_CODE": self.config_name,
            "REF_DATE": date_end,
            "DATE_INI": date_ini,
            "DATE_END": date_end,
            "REF_DATE_NODASH": date_end.strftime('%Y%m%d'),
        }
        return data

    def get_specific_configs(self):
        file = "{}{}".format(self.config_name, '.json')
        data = self._get_config_data()
        result = self._get_template_rendered(file, data)
        return result

    def get_global_configs(self):
        file = self._get_global_configs_file()
        # TODO: allow the user to set the global_config instead of impose
        # the standard '{report_code}_global.json'
        # if os.path.isfile(self._global_configs): # this throwing exception
        #     file = os.path.basename(self._global_configs)
        data = self._get_config_data()
        result = self._get_template_rendered(file, data)
        return result

    def get_configs_json(self):
        configs = dict()

        if self._global_configs:
            global_configs = json.loads(self.get_global_configs())
            configs.update(global_configs)

        specific_configs = json.loads(self.get_specific_configs())
        configs.update(specific_configs)

        return configs
