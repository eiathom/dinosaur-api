import sys

from app.src.api import (
    get_largest_dinosaur_species_by_name_by_length_in_metres,
    get_dinosaur_names_anagrams_list,
)

if __name__ == "__main__":
    if sys.argv[1] == "largest":
        print(get_largest_dinosaur_species_by_name_by_length_in_metres())
    elif sys.argv[1] == "anagrams":
        print(get_dinosaur_names_anagrams_list())
