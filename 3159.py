def identifica(letra, teclas):
    for i in letra:
        for j in range(len(teclas)):
            if i in teclas[j]:
                return teclas[j][-1], teclas[j].index(i) + 1
teclas = [['1'], ['a', 'b', 'c', '2'], ['d', 'e', 'f', '3'], ['g', 'h', 'i', '4'], ['j', 'k', 'l', '5'], ['m', 'n', 'o', '6'],
        ['p', 'q', 'r', 's', '7'], ['t', 'u', 'v', '8'], ['w', 'x', 'y', 'z', '9'], [' ','0']]

for i in range(int(input())):
    ant = -1
    palavra = input().strip()
    for l in palavra:
        num, local = identifica(l.lower(), teclas)
        
        if l.isupper():
            print("#", end="")
        elif ant == num:
            if ant != -1: 
                print("*", end="")
            
        print(f"{str(num)}" * int(local), end="")
        
        ant = num
        
    print()
