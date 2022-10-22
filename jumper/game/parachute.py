
from game.style import Adding


class Parachute:

    def __init__(self):
        self._fail_count = 0
        self._max_fail_count = 4

    def deploy(self):
        print('\n')
        if self._fail_count == 0:
            print('     ___')
            print('    /___\\')
            print('    \\   /')
            print('     \ /')
            print('      O')
            print(Adding.YELLOW + '     /|\\' + Adding.ENDC)
            print(Adding.GREEN + '     / \\' + Adding.ENDC)
            print()
            print()
            print()
            print()
            print()
            print(Adding.CYAN + '~~~~~~~~~~~~~' + Adding.ENDC )
            print('\n')
        if self._fail_count==1:
            print('    /___\\')
            print('    \\   /')
            print('     \ /')
            print('      O')
            print(Adding.YELLOW + '     /|\\' + Adding.ENDC)
            print(Adding.GREEN + '     / \\' + Adding.ENDC)
            print()
            print()
            print()
            print()
            print(Adding.CYAN + '~~~~~~~~~~~~~' + Adding.ENDC )
            print('\n')
        if self._fail_count==2:
            print('    \\   /')
            print('     \ /')
            print('      O')
            print(Adding.YELLOW + '     /|\\' + Adding.ENDC)
            print(Adding.GREEN + '     / \\' + Adding.ENDC)
            print()
            print()
            print()
            print(Adding.CYAN + '~~~~~~~~~~~~~' + Adding.ENDC )
            print('\n')
        if self._fail_count ==3:
            print('     \ /')
            print(Adding.YELLOW + '     \\' + Adding.ENDC + 'O' + Adding.YELLOW + '/')
            print(Adding.YELLOW + '      |' + Adding.ENDC)
            print(Adding.GREEN + '     / \\' + Adding.ENDC)
            print(Adding.CYAN + '~~~~~~~~~~~~~' + Adding.ENDC )
            print('\n')
        if self._fail_count == 4:
            print(Adding.YELLOW + '     \\'+ Adding.ENDC+ 'O' + Adding.YELLOW +'/')
            print(Adding.CYAN + '~~~~~~~~~~~~~' + Adding.ENDC )
            print('\n')

    def fail(self):
        self._fail_count += 1
    
    def is_working(self):
        return self._fail_count < self._max_fail_count
