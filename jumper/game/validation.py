class Validation:
    def __init__(self, prompt):

        self._prompt = prompt
        self._valid_inputs = ['a','b','c','d','e','f', 'g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    

    def get_input(self):
        while True:
            answer = input(self._prompt).lower()
            if answer in self._valid_inputs:
                return answer
            else:
                print('Invalid Input.')
        

   