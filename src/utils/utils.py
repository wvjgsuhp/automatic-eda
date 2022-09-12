import numpy as np
import os
import yaml

from .env import ENV
from ..custom_types import DataFrame, ExtraColumns


def parse_config(config_file: str = 'config.yaml'):
    with open(config_file, 'r') as f:
        config = yaml.safe_load(f.read())
    ENV.CONFIG = config


def create_output_paths():
    for location in ENV.CONFIG['output'].values():
        os.makedirs(location['location'], exist_ok=True)


def get_figure_path(figure_name: str) -> str:
    return os.path.join(ENV.CONFIG['output']['figure']['location'], figure_name)


def add_columns(df: DataFrame, extra_columns: ExtraColumns) -> DataFrame:
    for extra_column in extra_columns:
        first_column = df.loc[:, extra_column['columns'][0]]
        second_column = df.loc[:, extra_column['columns'][1]]
        if extra_column['method'] in ('divide', '/'):
            new_column = np.where(
                first_column != 0, first_column / second_column, np.nan)
        elif extra_column['method'] in ('minus', '-'):
            new_column = first_column - second_column
        elif extra_column['method'] in ('sum', '+', 'plus'):
            new_column = df.loc[:, extra_column['columns']].sum(axis=1)
        else:
            raise ValueError(f'{extra_column["method"]} is not defined')

        df[extra_column['name']] = new_column

    return df
