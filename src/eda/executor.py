from .simple import Simple
from ..utils.env import ENV
from ..utils.safe_io import load_data
from ..utils.utils import add_columns


def execute():
    for data_name, eda_info in ENV.CONFIG['eda'].items():
        df = load_data(data_name)
        if extra_columns := eda_info.get('extra_columns'):
            df = add_columns(df, extra_columns)

        Simple(df, data_name, True).run()
