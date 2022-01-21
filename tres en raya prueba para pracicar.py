
cuadricula = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }

a = []

for key in cuadricula:
    a.append(key)

def juego1(board):
    print(board['7'] +"  " + '|' + board['8'] +"  " + '|' + board['9'])
    print('---+---+---')
    print(board['4'] +"  " + '|' + board['5'] +"  " + '|' + board['6'])
    print('---+---+---')
    print(board['1'] +"  " + '|' + board['2'] +"  " + '|' + board['3'])


def juego():

    inicio = 'X'
    referencia = 0


    for i in range(10):
        juego1(cuadricula)
        print("turno " + inicio )

        move = input()        

        if cuadricula[move] == ' ':
            cuadricula[move] = inicio
            referencia += 1
        else:
            print("no esta disponible")
            continue



        
        if referencia >= 5:

            if cuadricula['7'] == cuadricula['5'] == cuadricula['3'] != ' ': 
                juego1(cuadricula)
                print("\njuego finalizo.\n")                
                print(inicio + " usted ha ganado felicidades")
                break
            elif cuadricula['1'] == cuadricula['5'] == cuadricula['9'] != ' ': 
                juego1(cuadricula)
                print("\njuego finalizo.\n")                
                print(inicio + " usted ha ganado felicidades")
                break 
            elif cuadricula['1'] == cuadricula['4'] == cuadricula['7'] != ' ': 
                juego1(cuadricula)
                print("\njuego finalizo.\n")                
                print(inicio + " usted ha ganado felicidades")
                break
            elif cuadricula['2'] == cuadricula['5'] == cuadricula['8'] != ' ': 
                juego1(cuadricula)
                print("\njuego finalizo.\n")                
                print(inicio + " usted ha ganado felicidades")
                break
            elif cuadricula['3'] == cuadricula['6'] == cuadricula['9'] != ' ': 
                juego1(cuadricula)
                print("\njuego finalizo.\n")                
                print(inicio + " usted ha ganado felicidades")
                break 
            elif cuadricula['7'] == cuadricula['8'] == cuadricula['9'] != ' ': 
                juego1(cuadricula)
                print("\njuego finalizo.\n")                
                print(inicio + " usted ha ganado felicidades")                
                break
            elif cuadricula['4'] == cuadricula['5'] == cuadricula['6'] != ' ': 
                juego1(cuadricula)
                print("\njuego finalizo.\n")                
                print(inicio + " usted ha ganado felicidades")
                break
            elif cuadricula['1'] == cuadricula['2'] == cuadricula['3'] != ' ': 
                juego1(cuadricula)
                print("\njuego finalizo.\n")                
                print(inicio + " usted ha ganado felicidades")
                break      
        if referencia == 9:
            print("\njuego finalizo.\n")                
            print("ustedes empataron ")
        if inicio =='X':
            inicio = 'O'
        else:
            inicio = 'X'        
    
   
    final = input("quiere seguir (si/no)")
    if final == "si" or final == "no":  
        for key in a:
            cuadricula[key] = " "

        juego()

if __name__ == "__main__":
    juego()