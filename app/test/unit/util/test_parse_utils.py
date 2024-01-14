from app.src.util.parse_utils import get_float_value_from_string_value

import pytest

test_data = [
    (None, None),
    ("", None),
    (" ", None),
    ("a", None),
    ("-", None),
    ("0", 0.0),
    ("00101", 101.0),
    ("-00101", -101.0),
    ("0.0", 0.0),
    ("00101.0", 101.0),
    ("-00101.0", -101.0),
    ("a1", 1.0),
    ("1a", 1.0),
    ("0.1a", 0.1),
    ("-a1", 1.0),
    ("-1.23a", -1.23),
]


@pytest.mark.parametrize("input_value,expected_value", test_data)
def test_get_float_value_from_string_value_returns_expected_value_given_input_value(
    input_value, expected_value
):
    assert get_float_value_from_string_value(input_value) == expected_value
