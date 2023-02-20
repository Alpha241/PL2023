
def main():
    idade = dict()
    sexo = dict()
    tensao = dict()
    colesterol = dict()
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
                colesterol[key] = paciente[3]
                batimento[key] = paciente[4]
                temDoenca[key] = paciente[5]
                key += 1

    distNivelColestrol(colesterol,temDoenca)

        
            

            
    
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


def distDoencaIdade(idade,temDoenca):
    total_doentes = 0
    conta_idade = dict()
    conta_idade = {'[30-34]': 0, '[35-39]': 0, '[40-44]': 0, '[45-49]': 0, '[50-54]': 0, '[55-59]': 0, '[60-64]': 0, '[65-69]': 0, '[70+]': 0}
    
    for key in idade:
        idade_paciente = int(idade[key])
        if idade_paciente >= 30 and idade_paciente < 35:
            faixa_etaria='[30-34]'
        elif idade_paciente >= 35 and idade_paciente < 40:
            faixa_etaria='[35-39]'
        elif idade_paciente >= 40 and idade_paciente < 45:
            faixa_etaria='[40-44]'
        elif idade_paciente >= 45 and idade_paciente < 50:
            faixa_etaria='[45-49]' 
        elif idade_paciente >= 50 and idade_paciente < 55:
            faixa_etaria='[50-54]'
        elif idade_paciente >= 55 and idade_paciente < 60:
            faixa_etaria='[55-59]'
        elif idade_paciente >= 60 and idade_paciente < 65:
            faixa_etaria='[60-64]'
        elif idade_paciente >= 65 and idade_paciente < 70:
            faixa_etaria='[65-69]' 
        else:
            faixa_etaria='[70+]'
        
        if int(temDoenca[key]) == 1:
            conta_idade[faixa_etaria] += 1
            total_doentes += 1

    
    print('Distribuição de doença por faixa etária:')
    for faixa_etaria in conta_idade:
        proporcao = conta_idade[faixa_etaria]/total_doentes
        print(f'{faixa_etaria}: {proporcao:.2%}')

def distNivelColestrol(colesterol,temDoenca):
    conta_colesterol = {}
    pacientes =  len(colesterol)

    for i in range(pacientes):
        nivel_colesterol = int(int(colesterol[i]) / 10) * 10
        if nivel_colesterol not in conta_colesterol:
            conta_colesterol[nivel_colesterol] = {"total":0, "doentes": 0}
        conta_colesterol[nivel_colesterol]["total"] += 1
        if temDoenca[i] == "1":
            conta_colesterol[nivel_colesterol]["doentes"] += 1
    
    for nivel, valores in conta_colesterol.items():
        proporcao = valores["doentes"] / valores["total"]
        print(f"Nível de colesterol {nivel}-{nivel+9}:")
        print(f"Total de pacientes: {valores['total']}")
        print(f"Total de pacientes com doença: {valores['doentes']}")
        print(f"Proporção de pacientes com doença: {proporcao:.2%}")




main()












