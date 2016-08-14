import os
import logging
from JinjaBaseClass import JinjaBaseClass


class TemplateHandler(JinjaBaseClass):

    """The goal of this class is to manipulate templates and generate it's
    outputs """

    TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), 'templates')

    def __init__(self, template_name):
        super(TemplateHandler, self).__init__()
        self.template_name = template_name
        self.logger = logging.getLogger(__name__)

    def __repr__(self):
        return "<TemplateHandler object: '{}'>".format(self.template_name)

    def _get_template_rendered(self, data, *args, **kwargs):
        template = self._get_template('{}/index.html'.format(self.template_name))
        data.update({'ROOT': self.TEMPLATE_DIR})
        rendered = template.render(**data)
        return rendered
