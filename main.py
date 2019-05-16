import parts_of_speech
import spelling_grammar
import named_entity
import vectorization
import n_grams

import fileinput


def import_data_as_tuples():
    # returns a tuple of strings from the given file
    data_as_list = []
    for line in fileinput.input():
        data_as_list.append(line)
    return tuple(data_as_list)

if __name__ == "__main__":
    raw_data = import_data_as_tuples()
    # print(raw_data)
    # example call from one of our modules...
    named_entity_data = named_entity.do_named_entity()
