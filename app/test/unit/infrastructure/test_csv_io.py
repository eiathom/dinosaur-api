from app.src.infrastructure.csv_io import get_data_from_csv
from io import StringIO


def create_test_data(name_column: str, length_column: str):
    return f"""
name,diet,period,lived_in,type,length,species
{name_column},herbivorous,Early Jurassic 199-189 million years ago,South Africa,sauropod,{length_column},celestae
"""


def test_get_data_from_csv_returns_valid_dataframe_given_default_call():
    name_column = "aardonyx"
    length_column = "8.0m"
    data_frame = get_data_from_csv(
        StringIO(create_test_data(name_column, length_column))
    )
    assert data_frame is not None
    assert len(data_frame) == 1
    assert data_frame.at[0, "length"] == length_column
    assert data_frame.at[0, "name"] == name_column
