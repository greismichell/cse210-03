import random
class MysteryWord:

    def __init__(self):
        self._options = ['saphire', 'house', 'function', 'stone', 'private', 'variable', 'advance', 'agency', 'happy', 'apple', 'agreement', 'airport', 'amazing', 'answer', 'anxiety']
        self._guessed = {}
        self._value = random.choice(self._options)

        for letter in self._value:
            self._guessed[letter]=False

    def print_word(self):
        for letter in self._value:
            if self._guessed[letter]:
                print(letter, end=' ')
            else:
                print('_ ', end='')
            
        print()

    def test_letter(self, letter):
        if letter in self._value:
            self._guessed[letter]= True
            return True
        else:
            return False
    
    def is_discovered(self):
        return False not in self._guessed.values()

    def get_letter_count(self):
        return len(self._value)