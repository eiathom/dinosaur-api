from typing import List
import os
from app.src.service.dinosaur import (
    get_dinosaur_names_according_to_maximum_length_of_dinosaur,
    get_dinosaur_names_anagrams,
)
from app.src.infrastructure.csv_io import get_data_from_csv
from app.src.util.parse_utils import get_float_value_from_string_value

DEFAULT_CSV_DATA_FILE_LOCATION = "./data/dinosaurs.csv"
CSV_DATA_FILE_LOCATION = os.environ.get(
    "CSV_DATA_FILE_LOCATION", DEFAULT_CSV_DATA_FILE_LOCATION
)


def get_float_value_from_length(value: str) -> float:
    processed_value = get_float_value_from_string_value(value)
    if processed_value is None:
        return 1.0
    return processed_value


def get_largest_dinosaur_species_by_name_by_length_in_metres() -> List[str]:
    data_frame = get_data_from_csv(
        CSV_DATA_FILE_LOCATION,
        {
            "columns": ["name", "length"],
            "convert": {
                "length": get_float_value_from_length,
            },
        },
    )
    return get_dinosaur_names_according_to_maximum_length_of_dinosaur(
        data_frame, "name", "length"
    )


def get_dinosaur_names_anagrams_list() -> List[List[str]]:
    data_frame = get_data_from_csv(
        CSV_DATA_FILE_LOCATION,
        {
            "columns": ["name"],
            "convert": None,
        },
    )
    return get_dinosaur_names_anagrams(data_frame, "name")
