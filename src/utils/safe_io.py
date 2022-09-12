import pandas as pd

from ..custom_types import DataFrame
from ..utils.env import ENV


def load_data(data_name: str) -> DataFrame:
    source = ENV.CONFIG['source']['data'][data_name]
    filetype = source['filetype']
    location = source['location']
    kwargs = ENV.CONFIG['source']['filetype'][filetype]['kwargs'] \
        | source.get('kwargs', {})

    if filetype == 'csv':
        df: DataFrame = pd.read_csv(location, **kwargs)
        return df

    raise ValueError(f'{filetype} filetype not defined')
