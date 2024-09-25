class Anagram:
    def __init__(self, word):
        """Initializes the Anagram instance with a single word."""
        self.word = word

    def match(self, word_list):
        """Returns a list of words that are anagrams of the initialized word."""
        sorted_word = sorted(self.word)
        return [word for word in word_list if sorted(word) == sorted_word]
