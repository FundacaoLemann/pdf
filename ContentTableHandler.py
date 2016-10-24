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

    def _prettify_header(self, df):
        """
        This method receives a DataFrame and prettifies its header
        """
        header = df.columns
        rename = {}
        for column in header:
            rename[column] = (column.title().replace('_',' '))
        df.rename(columns=rename, inplace=True)

        return df

    def _get_dataframe(self):
        try:
            self.DF = pd.read_csv(self.src, delimiter='|')
        except Exception as e:
            if isinstance(e, IOError):
                exception = IOError("{}. Please make sure we are using absolute paths".format(e.message))
            raise exception

        self.DF = self._prettify_header(self.DF)

        return self.DF

    def _get_dataframe_sum(self):

        columns_types = self.DF.dtypes
        num_cols = []
        for index, value in columns_types.iteritems():
            if value != 'object':
                num_cols.append(index)
        df_sum = self.DF[num_cols].sum()

        self.DF_SUM = pd.DataFrame(data=df_sum)
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
