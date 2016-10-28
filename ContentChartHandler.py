import matplotlib
matplotlib.use('Agg')
import pandas as pd
import numpy as np
import tempfile


class ContentChartHandler(object):

    """We will generate the charts from here :)"""

    def __init__(self, src, x_label, y_label, **kwargs):
        super(ContentChartHandler, self).__init__()
        self.src = src
        self.x_label = x_label
        self.y_label = y_label


    def get_plot_image(self, **kwargs):

        output = tempfile.mkstemp(suffix='.png')[1]

        # TODO: use read_gbq()
        try:
            df = pd.read_csv(self.src, delimiter='|', encoding = 'utf-8', index_col=[0], header=0)
        except Exception as e:
            if isinstance(e, IOError):
                exception = IOError("{}. Please make sure we are using absolute paths".format(e.message))
            raise exception


        # generate the plot
        params = {
            'kind': 'bar',
            'ylim': (0, 100),
            'legend': False,
            'figsize': (14, 7),
            'grid': True,
            'color': "#339966",
            'rot': 90
        }

        plot = df.plot(**params)

        # annotate the values above the bars
        for idx, label in enumerate(list(df.index)):
            for acc in df.columns:
                value = np.round(df.ix[idx][acc], decimals=2)
                plot.annotate(value, (idx, value), xytext=(0, 15), textcoords='offset points')

        # set the labels
        plot.set_ylabel(self.y_label)
        plot.set_xlabel(self.x_label)

        # draw reference line
        plot.axhline(85, color='g', linestyle='--', lw=1)
        plot.axhline(50, color='r', linestyle='-', lw=1)

        # export chart
        fig = plot.get_figure()
        fig.tight_layout()
        fig.savefig(output)

        return output

