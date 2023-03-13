import re 
import json


def listas (file):
    padrao = re.compile(r"(\w+)(?:\{(\d+)\})?,")
    msg =  open(file,'r')
    informacoes = padrao.findall(msg)

    for campo, n_colunas in informacoes:
        if n_colunas:
            print(f"{campo} abrange {n_colunas} colunas")
        else:
             print(f"{campo} abrange 1 coluna")



listas("alunos.csv")