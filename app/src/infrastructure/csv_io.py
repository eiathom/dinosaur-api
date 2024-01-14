from typing import Union, Any
from pandas import read_csv as csv_reader, DataFrame


# TODO: `options` should be a verifiable class
def get_data_from_csv(
    csv_file_location: Union[str, Any], options: dict = None
) -> Union[DataFrame, None]:
    try:
        return csv_reader(
            csv_file_location,
            usecols=options["columns"] if options and options["columns"] else None,
            converters=options["convert"] if options and options["convert"] else None,
        )
    except Exception as exception:
        # TODO: decide on logging library
        print(
            f"unable to read csv_file_location: '{csv_file_location}' with options: '{options}' because of: '{str(exception)}"
        )
    return None
