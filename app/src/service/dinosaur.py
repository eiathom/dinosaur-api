from collections import defaultdict
from typing import List
from pandas import DataFrame


def get_dinosaur_names_according_to_maximum_length_of_dinosaur(
    data_frame: DataFrame,
    name_column_name: str,
    length_column_name: str,
) -> List[str]:
    if data_frame is not None:
        try:
            max_length = data_frame[length_column_name].max()
            return data_frame[data_frame[length_column_name] == max_length][
                name_column_name
            ].tolist()
        except Exception as exception:
            # TODO: decide on logging library
            print(
                f"unable to find dinosaur names given name column: '{name_column_name}' and length column: '{length_column_name}' because of: '{str(exception)}"
            )
    return []

def get_dinosaur_names_anagrams(
    data_frame: DataFrame,
    name_column_name: str,
) -> List[List[str]]:
    if data_frame is not None:
        try:
            anagrams = defaultdict(list)
            for name in data_frame[name_column_name]:
                key = "".join(sorted(name))
                anagrams[key].append(name)
            return [items for items in anagrams.values() if len(items) > 1]
        except Exception as exception:
            # TODO: decide on logging library
            print(
                f"unable to find dinosaur names given name column: '{name_column_name}' because of: '{str(exception)}"
            )
    return []
