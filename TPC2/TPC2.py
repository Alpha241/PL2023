import sys
import re

def main():


    while True:
        res = 0
        txt = input("Introduza o texto (fim para terminar): ")
        status = False
        if 'fim' == txt:
            break
        
        txt = txt.upper().strip().replace(' ','')
        for caractere in txt:
            if caractere.isdigit() and status is False:
                res += int(caractere)
            if caractere == '=' and status is False:
                print(res)
            #if txt[caractere:caractere+2] == "ON":
                #status = False
            #if txt[caractere:caractere+3] == "OFF":
                #caractere = caractere + 3
        
        print(res)
            
        

        
    

main()