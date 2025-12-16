import pytest
import pandas as pd
from Data_Configuration import Data_Config

csv_path = "C:\\Users\\jackp\\Documents\\Python\\EE551\\Project\\nsrdb_2024.csv" #Path to sample NSRDB CSV file for testing

@pytest.fixture
def data_config():
    """
    Fixture to create a Data_Config instance.
     Returns:
        Data_Config: An instance of the Data_Config class.
    """
    return Data_Config(csv_path) #Use instance to pass through configure_sample method to ensure data was configured properply

def test_configure_sample_not_empty(data_config):
    """
    Test that the configured sample is not empty.
    """
    df = data_config.configure_sample()
    assert not df.empty

def test_configure_sample_columns(data_config):
    """
    Test that the configured sample contains the 'GHI' column.
    """
    df = data_config.configure_sample()
    assert 'GHI' in df.columns

def test_configure_sample_no_nans(data_config):
    """
    Test that the configured sample does not contain NaN values.
    """
    df = data_config.configure_sample()
    assert not df.isna().values.any()
