"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    """Finds random words from a dictionary.

    >>> word_finder = WordFinder("words.txt")
    235886 words read

    >>> word_finder.random()
    volupt

    >>> word_finder.random()
    undefined

    >>> word_finder.random()
    tampala
    """
    def __init___(self, path):
        self.path = path
        dict_file = open(path)
        self.words = self.parse(dict_file)
        print(f"{len(self.words)} words read")
    
    def parse(self, dict_file):
        """Parse dict_file -> list of words."""

        return [w.strip() for w in dict_file]

    def random(self):
        """Return random word."""

        return random.choice(self.words)

class SpecialWordFinder(WordFinder):
    """WordFinder based on original WordFinder class that excludes blank lines and comments."""

    def parse(self, dict_file):
        """Parse dict_file -> list of words, skipping blanks/comments."""

        return [w.strip() for w in dict_file
                if w.strip() and not w.startswith("#")]

    
    

