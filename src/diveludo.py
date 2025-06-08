import random

def divenludo():
    print("Bonvenon al la divenludo!")
    print("Mi pensas pri nombro inter 1 kaj 1000. Provu diveni ĝin.")
    
    nombro = random.randint(1, 1000)
    provoj = 0
    
    while True:
        provo = input("Via diveno: ")
        
        # Kontroli ĉu la enigo estas entjero
        if not provo.isdigit():
            print("Bonvolu enmeti validan nombron.")
            continue
        
        diveno = int(provo)
        provoj += 1
        
        if diveno < nombro:
            print("Tro malalta! Provu pli grandan nombron.")
        elif diveno > nombro:
            print("Tro alta! Provu pli malgrandan nombron.")
        else:
            print(f"Gratulojn! Vi divenis la nombron {nombro} post {provoj} provoj.")
            break

if __name__ == "__main__":
    divenludo()
