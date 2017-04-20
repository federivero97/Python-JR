def sheep(filename):
    line = [line.rstrip('\n') for line in open(filename)]
    #Inicializo lista de Boleanos donde cada uno señala si el número de indice ya aparecio.
    digits = [False,False,False,False,False,False,False,False,False,False]
    for x in range(1,int(line[0])):             #Habrá T casos, donde T=line[0]
        for z in range(10):         
            digits[z] = False                   #Restauro los números a False
        for y in range(1,201): 
            number = int(line[x])*(y)   
            if (False in digits):       
                for z in range(10):     
                    if not digits[z]:
                        if str(z) in str(number):
                            digits[z] = True
            if not(False in digits):
                print("Case#" + str(x) + ": "+ str(number))     # Si estan todos los números output:"Case#X: N*y"
                break
        if (False in digits):
            print("Case#" + str(x) + ": IMSOMNIA")  #Si no estan todos los números output:"IMSOMNIA"


if __name__ == '__main__':
    sheep("c-input.in")