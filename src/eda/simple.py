import matplotlib.pyplot as plt
from ..base import BaseFigure
from ..utils.env import ENV


class Simple(BaseFigure):
    complexity = 'simple'

    def run(self):
        self.get_stats()
        self.histogram()

    def histogram(self):
        if histograms := self._get_figure_config('histogram'):
            for column, kwargs in histograms.items():
                min_max = (self.df.loc[:, column].quantile(.025),
                           self.df.loc[:, column].quantile(.975))
                plt.figure(figsize=ENV.FIGURE_SIZE)
                plt.hist(self.df.loc[:, column].clip(
                    *min_max), density=True, **kwargs)
                plt.xlabel(column)

                if self.save_figure:
                    figure_path = self._get_figure_path(column, 'histogram')
                    plt.savefig(figure_path)
                else:
                    plt.show()

    def get_stats(self):
        print(self.df.isna().sum())
