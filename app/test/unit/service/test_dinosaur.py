from typing import List

from pandas import DataFrame
from app.src.service.dinosaur import (
    get_dinosaur_names_according_to_maximum_length_of_dinosaur,
    get_dinosaur_names_anagrams,
)


def get_test_data_frame(data_values: List[dict]) -> DataFrame:
    all_items = []
    for item in data_values:
        all_items.append(
            [
                item["name_column_name_value"],
                "herbivorous",
                "Early Jurassic 199-189 million years ago",
                "South Africa",
                "sauropod",
                item["length_column_name_value"],
                "celestae",
            ]
        )
    return DataFrame(
        all_items,
        columns=["name", "diet", "period", "lived_in", "type", "length", "species"],
    )


def test_get_dinosaur_names_according_to_maximum_length_of_dinosaur():
    expected_name_value = "sample"
    length_value = "8.0m"
    data_input = [
        {
            "name_column_name_value": expected_name_value,
            "length_column_name_value": length_value,
        }
    ]
    data_frame = get_test_data_frame(data_input)
    assert get_dinosaur_names_according_to_maximum_length_of_dinosaur(
        data_frame, "name", "length"
    ) == [expected_name_value]


def test_get_dinosaur_names_anagrams():
    expected_name_value_first = "sample"
    expected_name_value_second = expected_name_value_first[::-1]
    data_input = [
        {
            "name_column_name_value": expected_name_value_first,
            "length_column_name_value": "21.0m",
        },
        {
            "name_column_name_value": expected_name_value_second,
            "length_column_name_value": "21.0m",
        },
        {
            "name_column_name_value": "not_the_same",
            "length_column_name_value": "21.0m",
        },
    ]
    assert get_dinosaur_names_anagrams(
        get_test_data_frame(data_input),
        "name",
    ) == [[expected_name_value_first, expected_name_value_second]]
