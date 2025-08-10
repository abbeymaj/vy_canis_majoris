# Importing packages
import pytest
import sqlite3
from src.components.config_entity import DataBaseConfig
from src.components.fetch_data import FetchData
from src.components.transform_landing_layer_data import TransformLandingLayerData
from src.components.load_landing_layer import LoadLandingLayer

# Verifying that the connection is available to the database
def test_connect_to_database():
    db_config = DataBaseConfig()
    df_path = db_config.db_path
    conn = sqlite3.connect(df_path)
    assert conn is not None

# Verifying that the data can be retrieved from the database
def test_retrieve_data_from_db():
    db_config = DataBaseConfig()
    df_path = db_config.db_path
    conn = sqlite3.connect(df_path)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM lnd_cma')
    data = cursor.fetchall()
    assert data is not None

# Verifying that the data can be loaded into the database
def test_load_data():
    fetch = FetchData()
    cols, rows = fetch.fetch_data()
    transform = TransformLandingLayerData(rows, cols)
    df = transform.transform_landing_data()
    load = LoadLandingLayer()
    load.load_landing_layer(df)
    