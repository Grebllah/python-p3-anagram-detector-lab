class Anagram:
    def __init__(self, chosen_word):
        self.chosen_word = chosen_word
    def match(self, matches):
        anagrams = []
        # loop through the matches, a list of strings, then for each string, make a sorted list of all the letters. compare this to the sorted list of the chosen words letters.
        for match in matches:
            match_list = [*match]
            if sorted(match_list) == sorted([*self.chosen_word]):
                anagrams.append(match)
        return anagrams
