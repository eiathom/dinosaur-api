import re

REGULAR_EXPRESSION_TO_MATCH_ON_DIGIT_TYPES = r"[-+]?\d*\.?\d+|\d+"


def get_float_value_from_string_value(value: str) -> float:
    """
    Attempt to return a float value from a string value.
    """
    if value is not None:
        match = re.search(REGULAR_EXPRESSION_TO_MATCH_ON_DIGIT_TYPES, value)
        if match:
            try:
                return float(match.group())
            except ValueError:
                # TODO: decide on logging library
                print(f"value: '{value}' threw exception on parse to float")
                return None
    return None
