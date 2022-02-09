import random 


class Jumper:
    words = ["car", "soldier", "helicopter","plane","gold","tea","table","clock","armchair","lamp","pot","bicycle","scooter"
    ,"pan","wifi","book","picture","fish","pet","helmet","shoe","wall","raincoat","umbrella","camera","water","phone","radio",
    "toy","cotton","cosmetics","toaster","mocrowave","mixer","blender","clothes","lamp"]
    unknown_word = random.choice(words)
    my_letters = []

    def __init__(self, turns=6):
        self.turns = turns
# replace espaces with the guessed leters
    def met1(self):
        write = ''
        for i in self.unknown_word:
            if i in self.my_letters:
                write = write + i
            else:
                write =write + '*'
        return write
# print information to users
    def met2(self):
        print(self.met1())
        print(f'remainig chances: {self.turns}')
       
# add leter to my leters and decrease turn in -1 when user fails
    def met3(self, guess):
                
        if  len(guess) == 1:
            
            self.my_letters.append(guess)
            if guess in self.unknown_word:
                print('right')
            else:
                print('wrong')
                self.turns =self.turns - 1
                    
        self.met2()
# it is trye when my_lettersis same as unknoe_word
    def met4(self):
        for i in self.unknown_word:
            if i not in self.my_letters:
                return False
        return True
# print yo win or lost when ser is entering a leter   
    def met5(self):
        
        while self.turns > 0:
            guess = input('try a new letter:   ')
            
            self.met3(guess)
            if self.met4():
                return print('YOU WON!')
        print('YOU LOST')
        
if __name__ == '__main__':
    game = Jumper()
    game.met5()