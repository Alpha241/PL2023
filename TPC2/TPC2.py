import sys

def main():


    while True:
        res = 0
        txt = input("Introduza o texto (fim para terminar): ")
        txt = txt.upper().strip().replace(' ','')
        txt = txt.split('=')[0]
        pos_off = txt.find("OFF")
        pos_on = txt.find("ON", pos_off)
        if pos_off >= 0 and pos_on >= 0:
            txt = txt[:pos_off] + txt[pos_on + len("ON"):]

        if 'FIMf' == txt:
            break
        
        for caractere in txt:
            if caractere.isdigit():
                res += int(caractere)            
    
        print(res)

    
main()