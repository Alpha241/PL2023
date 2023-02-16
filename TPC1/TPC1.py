
def main():
    readfile()



def readfile():
    idade = dict()
    sexo = dict()
    tensao = dict()
    colestrol = dict()
    batimento = dict()
    temDoenca = dict()
    
    #define a chave do dicionário
    key = 0

    with open('myheart.csv', 'r') as file:
        lines = file.readlines()[1:]
        for line in lines:
            paciente = line.strip().split(",")
            if validaDados(paciente) == True:
                idade[key] = paciente[0]
                sexo[key] = paciente[1]
                tensao[key] = paciente[2]
                colestrol[key] = paciente[3]
                batimento[key] = paciente[4]
                temDoenca[key] = paciente[5]
                key += 1
        
        
            

            
    
def validaDados(lista):
    if int(lista[0]) < 0:
        return False
    elif lista[1] != 'M' and lista[1] != 'F':
        return False
    elif int(lista[2]) <= 0:
        return False
    elif int(lista[3]) <= 0:
        return False
    elif int(lista[4]) <= 0:
        return False
    elif int(lista[5]) != 0 and int(lista[5]) != 1:
        return False
    else:
        return True
    

main()