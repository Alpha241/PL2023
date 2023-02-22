import sys
import re

def main():


    while True:
        res = 0
        txt = input("Introduza o texto (fim para terminar): ")
        if 'fim' == txt:
            break
        
        for caractere in txt:
            if caractere.isdigit():
                res += int(caractere) 
        print(res)
        
    

main()