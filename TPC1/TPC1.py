

def main():
    readfile()



def readfile():
    idade = dict()
    sexo = dict()
    tensao = dict()
    colestrol = dict()
    batimento = dict()
    temDoenca = dict()

    with open('myheart.csv', 'r') as file:
        lines = file.readlines()[1:]
        for line in lines:
            
    
