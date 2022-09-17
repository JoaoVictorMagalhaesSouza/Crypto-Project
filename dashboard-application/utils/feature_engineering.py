import pandas as pd
from copy import deepcopy
class FeatureEngineering():

    def __init__(self, input_data: pd.DataFrame):
        self.data = deepcopy(input_data)
