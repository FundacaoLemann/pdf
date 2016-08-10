import pandas as pd

class ContentHandler(object):
	
	"""docstring for ContentHandler"""
	
	def __init__(self, file_path):
		super(ContentHandler, self).__init__()
		self.DF = self._get_dataframe(file_path)
		self.DF_SUM = self._get_dataframe_sum()
	
	def _get_dataframe(self, file_path):
		df = pd.read_csv(file_path, delimiter='|')
		return df

	def _get_dataframe_sum(self):
		df_sum = pd.DataFrame(data=self.DF.sum())
		return df_sum

	def _get_df_html(self, df, **kwargs):
		html_out = df.to_html(**kwargs).replace('border="1"','border="0"')
		return html_out

	def get_table_html(self):
		df_html = self._get_df_html(self.DF, index=False, classes='table table-striped detailed')
		df_sum_html = self._get_df_html(self.DF_SUM, header=False, classes='table meta-info')
		return locals()


# print ContentHandler('./data_sample.table.csv').get_table_html()
