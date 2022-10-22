from game.parachute import Parachute
from game.mystery_word import MysteryWord
from game.validation import Validation

class Director:
    def start_game(self):
        parachute = Parachute()
        mystery_word = MysteryWord()
        valid_letter = Validation('guess the letter [a-z]: ')
        print('The secret word has', mystery_word.get_letter_count(),'letters, try to guess it letter by letter before you die:\n')
        mystery_word.print_word()
        parachute.deploy()

        while parachute.is_working():
            letter = valid_letter.get_input()
            print()
            if  mystery_word.test_letter(letter):
                if mystery_word.is_discovered():
                    print('you won!')
                    mystery_word.print_word()
                    break
            else:
                print('wrong letter, try again!\n')
                parachute.fail()
            mystery_word.print_word()
            parachute.deploy()
        print('Game Over!')

