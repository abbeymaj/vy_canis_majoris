# Import packages
import pytest
import pandas as pd
from src.utils import create_dataframe
from src.components.fetch_data import FetchData
from src.components.transform_landing_layer_data import TransformLandingLayerData

# Verifying that the data can be transformed into a pandas dataframe
def test_dataframe_creation():
    fetch = FetchData()
    cols, rows = fetch.fetch_data()
    df = create_dataframe(rows, cols)
    assert df is not None
    assert df.shape[0] > 0
    assert df.shape[1] > 0
    assert df.columns.tolist() == cols

# Verifying that the data is ready to be loaded into the landing layer
def test_transform_data():
    fetch = FetchData()
    cols, rows = fetch.fetch_data()
    transform = TransformLandingLayerData(rows, cols)
    df = transform.transform_landing_data()
    assert isinstance(df, pd.DataFrame)
    assert df is not None
    assert df.shape[0] > 0
    assert df.shape[1] > 0
    assert df.columns.to_list() == ['Date', 'Magnitude_Adj']
    