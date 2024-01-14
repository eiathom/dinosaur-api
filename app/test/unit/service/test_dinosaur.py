from pandas import DataFrame
from app.src.service.dinosaur import (
    get_dinosaur_names_according_to_maximum_length_of_dinosaur,
)


def get_test_data_frame(
    name_column_name_value: str, length_column_name_value: str
) -> DataFrame:
    return DataFrame(
        [
            [
                f"{name_column_name_value}",
                "herbivorous",
                "Early Jurassic 199-189 million years ago",
                "South Africa",
                "sauropod",
                f"{length_column_name_value}",
                "celestae",
            ]
        ],
        columns=["name", "diet", "period", "lived_in", "type", "length", "species"],
    )


def test_get_dinosaur_names_according_to_maximum_length_of_dinosaur():
    expected_name_value = "sample"
    length_value = "8.0m"
    data_frame = get_test_data_frame(expected_name_value, length_value)
    assert get_dinosaur_names_according_to_maximum_length_of_dinosaur(
        data_frame, "name", "length"
    ) == [expected_name_value]
