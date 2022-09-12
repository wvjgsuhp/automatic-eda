from typing import Optional
from .utils.env import ENV
from .custom_types import DataFrame, FigureConfig
from .utils.utils import get_figure_path


class BaseFigure:
    complexity: str

    def __init__(self, df: DataFrame, data_name: str, save_figure: bool = False):
        self.df = df
        self.data_name = data_name
        self.config = ENV.CONFIG['eda'][data_name].get(self.complexity)
        self._assert_config()

        self.save_figure = save_figure

    def run(self):
        pass

    def _get_figure_config(self, figure_type: str) -> Optional[FigureConfig]:
        if self.config is None or not self.config.get(figure_type):
            return None
        return self.config.get(figure_type)

    def _get_figure_path(self, column: str, figure_type: str) -> str:
        figure_name = f'{self.data_name}_{column}_{self.complexity}_{figure_type}.png'
        figure_path = get_figure_path(figure_name)
        return figure_path

    def _assert_config(self):
        if not self.config:
            raise ValueError(f'simple config not set for {self.data_name}')
