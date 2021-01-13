import random

def menu():
    
    print('Type "play" to play the game, "exit" to quit: ')
    menue = input()
    while menue != "play" and menue != "exit":
        print('Type "play" to play the game, "exit" to quit: ')
        menue = input()
    if menue == "play":
        play()
    elif menue == "exit":
        exit(1)
    
        
        
def play():
    a = ['python', 'java', 'kotlin', 'javascript']

    b = random.choice(a)
    c = len(b)
    d = "-" * c
    e = 8
    g = list(d)
    h = set()

    while e != 0 and "-" in g:
        if e >= 1:
            print(d)
        g = list(d)
        f = input("Input a letter: ")
        if len(f) != 1:
            print("You should input a single letter")
            print()
        elif f.islower() == False:
            print("Please enter a lowercase English letter")
            print()
        elif f in h:        
            print("You've already guessed this letter")
            print()
        elif f not in b:
            e -= 1
            print("That letter doesn't appear in the word")
            if e >= 1:
                print()
            h.add(f)
        elif f in b:
            for i in range(len(b)):
                if f == b[i]:
                    g[i] = f
                    d = ''.join(g)
                    h.add(f)
                    if "-" not in g:
                        print(d)
                        print(f"You guessed the word {b}!")
                        print("You survived!")
                    if e >= 1 and "-" in g:
                        print()            
    if "-" in g:
        print("You lost!")  
    menu()           

        
print("""H A N G M A N
""")
menu()

                
