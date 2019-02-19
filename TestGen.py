#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

#Numero de posibles opciones (a,b,c,d) = 4
numOpciones = 4
#Palabra para encontrar las soluciones
WORD = "RESPUESTAS"
#Ruta por defecto
RUTA = ''

def esPrinPreg(n):
    return n.startswith("a.") or n.startswith("b.") or n.startswith("c.") or n.startswith("d.") or n.startswith("a)") or n.startswith("b)") or n.startswith("c)") or n.startswith("d)") or n.startswith("A.") or n.startswith("B.") or n.startswith("C.") or n.startswith("D.") or n.startswith("A)") or n.startswith("B)") or n.startswith("C)") or n.startswith("D)") or len(n)<2
def esOtraPreg(n):
    return n[0].isdigit() and (n[1]=='.' or n[1]==')')

def iniciaTest():
    num = input("Que tema desea examinar")
    archivocarga = RUTA+"{}.txt".format(num)
    f = open(archivocarga ,encoding="utf8")
    os.system('cls')

    archivo = f.readlines()
    sols = {}
    guardasol = False
    soluciones=[]
    for n in archivo :
        if WORD in n :
            guardasol = True
        elif guardasol and len(n)>2:
            soluciones.append(n)


    for s in soluciones:
        num  = ((s[0:2]).strip())
        resp = ((s[2:]).strip())
        sols[str(num).replace(".","").replace("-","")] = (resp.replace(")","").replace(".","").replace("-","")).strip()

    
    esPregunta=False
    esRespuesta=False
    preguntas = []
    respuestas = []
    preg = ""
    resp = ""

    for n in archivo:
        
        if not esRespuesta and ((n[0].isdigit()) and len(n)>10 )or esPregunta:
            preg+=n.replace('\n',' ')
            esPregunta = True
            if ":" in n or "?" in n or esPrinPreg(archivo[(archivo.index(n)+1)]) or len(n)<10:
                esPregunta = False
        else:
            preguntas.append(preg) 
            preg = ""

        if esPrinPreg(n) or esRespuesta: 
            resp+=n.replace('\n',' ')
            
            esRespuesta=True
            

            if len(n)<4 or (archivo.index(n)+1)== len(archivo) or n.strip().endswith('.') or esPrinPreg(archivo[(archivo.index(n)+1)]) or esOtraPreg(archivo[(archivo.index(n)+1)]):
                esRespuesta = False
                respuestas.append(resp)
                resp= ""
        
    finalres = {}
    preguntas = list(filter(None, preguntas))
    respuestas = [s for s in respuestas if len(s)>3]
    

    fin = False
    for i in range(0,len(preguntas)):
        
        if not fin:
            print(preguntas[i]+"\n\n")
            r = respuestas[:numOpciones]
            for n in r:
                print(n+"\n")
                respuestas.remove(n)
            usuario = ''
            while (usuario not in ['a','b','c','d']):
                usuario = input("Adivina la respuesta\n")
                
            if usuario.lower() == sols[str(i+1)].lower():
                print("Respuesta correcta")
                finalres[str(i+1)]=1
            else:
                print("ERROR, la respuesta era {}".format(sols[str(i+1)]))
                finalres[str(i+1)]=0
            print("\n\n\n")

            usuario = input("Si quiere seguir introduzca intro\nSi quiere salir introduzca s")
            
            if (usuario.lower())=="s":
                fin = True
            
            os.system('cls')

    print("Resumen del test")
    for key, value in finalres.items():
        print(key,end=" ")
        if value==0:
            print("Fallada")
        else:
            print("Acertada")


    print("Numero de preguntas respondidas: {}\nAciertos totales: {}\n\n\n".format(len(finalres),sum(finalres.values())))


if __name__ == "__main__":
    playing= True
    while playing:
        iniciaTest()
        res = ''
        while (res not in ['1','2']):
            res = input("Desea realizar otro test?\n1-Si\n2-No\n")
        if (res)=='2': playing=False 

    print("Hasta la próxima")