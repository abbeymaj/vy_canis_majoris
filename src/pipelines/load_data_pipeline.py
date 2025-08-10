# Importing packages
import sys
import pandas as pd
import sqlite3
from src.components.fetch_data import FetchData
from src.components.transform_landing_layer_data import TransformLandingLayerData
from src.components.load_landing_layer import LoadLandingLayer

# Running the pipeline to load the data
if __name__ == '__main__':
    
    # Fetching the data from the AAVSO website
    data = FetchData()
    cols, rows = data.fetch_data()
    
    # Transforming the data before loading
    transform = TransformLandingLayerData(rows=rows, cols=cols)
    df = transform.transform_landing_data()
    
    # Loading the transformed data into the database table
    load = LoadLandingLayer()
    load.load_landing_layer(df=df)
    
