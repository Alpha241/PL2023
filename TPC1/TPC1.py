
def main():
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

    distDoencaSexo(sexo,temDoenca)

        
            

            
    
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


def distDoencaSexo(sexo,temDoenca):
    total_pacientes=len(sexo)
    total_homens = 0
    total_mulheres = 0
    doenca_homens = 0
    doenca_mulheres = 0

    for i in range(total_pacientes):
        if sexo[i] == 'M' and int(temDoenca[i]) == 1:
            total_homens += 1
        elif sexo[i] == 'M':
            doenca_homens += 1
        elif sexo[i] == 'F' and int(temDoenca[i]) == 1:
            doenca_mulheres += 1
        elif sexo[i] == 'F':
            total_mulheres += 1

    proporcao_doencas_homens = doenca_homens / total_homens
    proporcao_doencas_mulheres = doenca_mulheres / total_mulheres

    print(doenca_homens)
    print(f"Total pacientes : {total_pacientes}")
    print(f"Total de homens: {total_homens}")
    print(f"Total de mulheres: {total_mulheres}")
    print(f"Proporção de homens com a doença: {proporcao_doencas_homens:.2%}")
    print(f"Proporção de mulheres com a doença: {proporcao_doencas_mulheres:.2%}")



main()












