"""Word Finder: finds random words from a dictionary."""
from random import randint

class WordFinder:
    """
    >>> wf = WordFinder("simple.txt")

    >>> wf.random() in ["carrot", "fart", "deez"]
    True

    """
    def __init__(self, filepath):
        self.file = open(filepath, "r")
        self.words = generate_words(self.file)
        print(f"{len(self.words)} words read")

    
    def random(self):
        randnum = randint(0, len(self.words) - 1)
        return self.words[randnum]
    


        

def generate_words(file):
    lst = []
    for line in file:
        lst.append(line)

    return lst

class SpecialWordFinder(WordFinder):
    def __init__(self, filepath):
        super().__init__(filepath)
        self.words = special_generate_words(self.file)


def special_generate_words(file):
    lst = []
    for line in file:
        if line[0] != '#' or line[0] != ' ':
            lst.append(line)

    return lst