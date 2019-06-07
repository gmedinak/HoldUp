import os

# Verbosit was included in the docs, but it works fine without it???
from symspellpy.symspellpy import SymSpell

class SpellChecker:
    # maximum edit distance per dictionary precalculation
    max_edit_distance_dictionary = 2
    prefix_length = 7
    term_index = 0  # column of the term in the dictionary text file
    count_index = 1 # column of the term frequency in the dictionary text file
    # max edit distance per lookup (per single word, not per whole input string)
    max_edit_distance_lookup = 2
    dictionary_filename = "frequency_dictionary_en_82_765.txt"

    def __init__(self):
        # create object
        self.sym_spell = SymSpell(self.max_edit_distance_dictionary,
                               self.prefix_length)
        # load dictionary
        dictionary_path = os.path.join(os.path.dirname(__file__),
                                    self.dictionary_filename)

        if not self.sym_spell.load_dictionary(dictionary_path, self.term_index,
                                        self.count_index):
            print("Dictionary file not found")
            return

    def suggest(self, input_term):
        """
        lookup suggestions for multi-word input strings (supports compound
        splitting & merging)
        """
        suggestions = self.sym_spell.lookup_compound(input_term,
                                                  self.max_edit_distance_lookup)
        if(debug):
            # display suggestion term, edit distance, and term frequency
            for suggestion in suggestions:
                print("{}, {}, {}".format(suggestion.term,suggestion.distance,
                                        suggestion.count))
        return [suggestion.term for suggestion in suggestions]

    def suggest_with_debug(self, input_term):
        """
        an array of the suggested term, edit distance, and term frequency
        """
        suggestions = self.sym_spell.lookup_compound(input_term,
                                                self.max_edit_distance_lookup)
        return [[s.term, s.distance, s.count] for s in suggestions]

def main():
    # An example of how to use the spellchecker.
    spellchecker = SpellChecker()
    print(spellchecker.suggest_with_debug("whereis th elove hehad dated forImuch of thepast who "))
    print(spellchecker.suggest_with_debug("couqdn'tread in sixtgrade and ins pired him"))


def do_spelling_grammar():
    pass

if __name__ == "__main__":
    main()