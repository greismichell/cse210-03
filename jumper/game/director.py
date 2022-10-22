from game.parachute import Parachute
from game.mystery_word import MysteryWord

class Director:
    def start_game(self):
        parachute = Parachute()
        mystery_word = MysteryWord()
        print('The secret word has', mystery_word.get_letter_count(),'letters, try to guess it letter by letter before you die:\n')
        mystery_word.print_word()
        parachute.deploy()

        while parachute.is_working():
            if  mystery_word.guess_letter():
                if mystery_word.is_discovered():
                    print('you won!')
                    break
            else:
                print('wrong letter, try again!\n')
                parachute.fail()
            mystery_word.print_word()
            parachute.deploy()
        print('Game Over!')

