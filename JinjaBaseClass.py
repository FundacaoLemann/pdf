from datetime import datetime, timedelta
from jinja2 import Environment, FileSystemLoader

class JinjaBaseClass(object):

    """docstring for JinjaBaseClass"""

    def __init__(self, datetimeformat='%Y%m%d', *args, **kwargs):
        super(JinjaBaseClass, self).__init__()
        self._set_template_engine()
        self._set_filters()
        self._DT_FORMAT = datetimeformat
        assert self.TEMPLATE_DIR

    def _datetimeformat_filter(self, value, format_in=None, format_out='%Y-%m-%d %H:%M:%S'):
        if format_in:
            value = datetime.strptime(value, format_in)
        return value.strftime(format_out)


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

    def _get_date_timedelta(self, dateStr, days, *args, **kwargs):
        dt = datetime.strptime(dateStr, self._DT_FORMAT) + timedelta(days=days)
        return dt

    def _get_date_timedelta_str(self, *args, **kwargs):
        dt_str = self._get_date_timedelta(*args, **kwargs).strftime(self._DT_FORMAT)
        return dt_str
