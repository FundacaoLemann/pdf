import pandas as pd
from ContentChartHandler import ContentChartHandler
from ContentTableHandler import ContentTableHandler
from datetime import datetime


class ContentHandler(object):
    
    """Gets a CSV file_path as input"""
    
    def __init__(self, report_code, configs):
        super(ContentHandler, self).__init__()
        self._configs = configs


    def get_tables(self):
        tables = self._configs['TABLES']
        results = []
        for table_configs in tables:
            result = ContentTableHandler(**table_configs).get_table()
            table_configs.update(result)
            results.append(table_configs)
        return results
        pass


    def get_charts(self):
        charts = self._configs['CHARTS']
        results = []
        for chart_configs in charts:
            file_path = ContentChartHandler(**chart_configs).get_plot_image()
            chart_configs.update({"img_src": file_path})
            results.append(chart_configs)
        return results


    def get_data(self):
        self._configs['CHARTS'] = self.get_charts()
        self._configs['TABLES'] = self.get_tables()
        self._configs['CREATED_AT'] = datetime.now()
        return self._configs