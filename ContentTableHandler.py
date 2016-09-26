import pandas as pd


class ContentTableHandler(object):
    
    """Gets a CSV file_path as input"""
    """"""
    
    def __init__(self, title, src, **kwargs):
        super(ContentTableHandler, self).__init__()
        self.title = title
        self.src = src
        self._get_dataframe()
        self._get_dataframe_sum()
    

    def _get_dataframe(self):
        self.DF = pd.read_csv(self.src, delimiter='|')
        return self.DF

    def _get_dataframe_sum(self):
        self.DF_SUM = pd.DataFrame(data=self.DF.sum())
        return self.DF_SUM

    def _get_df_html(self, df, **kwargs):
        html_out = df.to_html(**kwargs).replace('border="1"','border="0"')
        return html_out

    def _get_table_html(self):
        result = self._get_df_html(self.DF, index=False, classes='table table-striped detailed')
        return result

    def _get_table_meta_html(self):
        result = self._get_df_html(self.DF_SUM, header=False, classes='table meta-info')
        return result


    def get_table(self, ):
        result = {
            'meta': self._get_table_meta_html(),
            "html": self._get_table_html(),
        }
        return result
