# Import packages
import pytest
import pandas as pd
from src.utils import create_dataframe
from src.components.fetch_data import FetchData
from src.components.transform_landing_layer_data import TransformLandingLayerData

# Creating a dataframe as a module for multiple unit tests
@pytest.fixture(scope="module")
def test_dataframe():
    """Create dataframe once for all tests in this module."""
    fetch = FetchData()
    cols, rows = fetch.fetch_data()
    df = create_dataframe(rows, cols)
    return df, cols

# Creating a transform dataframe as a module for multiple unit tests
@pytest.fixture(scope="module")
def transform_data():
    fetch = FetchData()
    cols, rows = fetch.fetch_data()
    transform = TransformLandingLayerData(rows, cols)
    df_transformed = transform.transform_landing_data()
    return df_transformed

# Verifying that the dataframe was created correctly
def test_dataframe_is_not_none(test_dataframe):
    df, cols = test_dataframe
    assert df is not None

# Verifying that the dataframe has rows
def test_dataframe_has_rows(test_dataframe):
    df, cols = test_dataframe
    assert df.shape[0] > 0

# Verifying that the dataframe has columns
def test_dataframe_has_columns(test_dataframe):
    df, cols = test_dataframe
    assert df.shape[1] > 0

# Verifying that the dataframe has the correct columns
def test_dataframe_columns_match(test_dataframe):
    df, cols = test_dataframe
    assert df.columns.tolist() == cols

# Verifying that the dataframe is a pandas dataframe
def test_dataframe_is_pandas_dataframe(transform_data):
    df = transform_data
    assert isinstance(df, pd.DataFrame)

# Verifying that the transformed dataframe is not None
def test_transformed_dataframe_is_not_none(transform_data):
    df = transform_data
    assert df is not None

# Verifying that the tranformed dataframe has rows
def test_transformed_dataframe_has_rows(transform_data):
    df = transform_data
    assert df.shape[0] > 0

# Verifying that the dataframe has columns
def test_transformed_dataframe_has_columns(transform_data):
    df = transform_data
    assert df.shape[1] > 0

# Verifying that the dataframe has the correct columns
def test_transformed_dataframe_columns_match(transform_data):
    df = transform_data
    assert df.columns.to_list() == ['Date', 'Magnitude_Adj']

# Verifying that the Date feature is an object feature
def test_date_feature_is_object(transform_data):
    df = transform_data
    assert isinstance(df['Date'][0], object)
    