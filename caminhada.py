import sys,time,os
from random import randint
import tkinter as tk
import json



def slow_type(t):
        for l in t:
            sys.stdout.write(l)
            sys.stdout.flush()
            time.sleep(0.000000000065)
def fast_type(t):
        for l in t:
            sys.stdout.write(l)
            sys.stdout.flush()
            time.sleep(0.001)    

def clear():
    time.sleep(1)
    os.system('clear')



def exec_inspermon():
    x = os.system('python inspermons.py')
    return x

def exec_enfermaria():
    x = os.system('python enfermaria.py')
    return x

def exec_batalha():
    x = os.system('python batalha.py')
    return x






with open("inspermons_amigos.json","r") as inspermons_amigos:
    inspermons_amigos = json.load(inspermons_amigos)
with open("insperdex.json","r") as insperdex:
    insperdex = json.load(insperdex)





nome="nome"
vida="vida"
vida_maxima="vida_maxima"
poder="poder"
defesa="defesa"
nome_poder="nome_poder"
xp="xp"
nivel="nivel"





Decisao1=0
Decisao2=0




clear()

slow_type("""
    Olá amigo!

    Bem vindo ao mundo de Insper!!

    Esse mundo é habitado por criaturas chamadas de INSPERMONS!""")

clear()

slow_type("""
    
    Para algumas pessoas os Inspermons são animais de estimação

    Outros usam eles para lutar

    Seu Inspermon primário é o {}""".format(inspermons_amigos[0][0][nome]))

clear()

slow_type("""
    Um mundo de sonhos e aventuras com Inspermons o espera!
    
   !!! Vamos !!!""")
    

    
    
    



while True:

    achar = randint(1,13)

    clear()
            
    slow_type(""" 
   Você decide:
   1 - Caminhar
   2 - Inspermons
   3 - Insperdex
   0 - Dormir""")
    Decisao1 = int(input("""
    <> """))
    
    if Decisao1 == 0:
        

        slow_type("""
        Boa noite!
        Esperamos que você volte!

""")
        break

    if Decisao1 == 1:
        clear()
        slow_type("""
               <>Você decidiu caminhar<>""")
    
     
        fast_type("""

                  ....................         
                  ...oooO.............         
                  ..(    ).... Oooo...         
                  ...\  (.....(    )..         
                  ....\_)..... )  /...         
                  ............ (_/....         
                  .. oooO ............         
                  ..(    )....Oooo....         
                  ...\  (.....(    )..         
                  ....\_)..... )  /...         
                  .............(_/....         
                  ....................         
            """ )

        #Batalha
        if achar >= 1 and achar <= 6:
            Decisao2 = 1
        


        #Enfermaria
        if achar ==  7 and achar <=  9:
            slow_type("""

        	Voce pode:
        	1 - Ir a Enfermaria
        	0 - Continuar andando""")
            D3 = int(input("""
                <> """))
            if D3 == 1:
                Decisao2 = 2
            if D3 == 0:
                Decisao2 = 0


        if achar >=10 and achar <=13:
            slow_type("""
                  Você não Achou nada
""")
            
        #Decisao
        if Decisao2 == 0:
        	continue
        if Decisao2 == 1:
            exec_batalha()
        if Decisao2 == 2:
            exec_enfermaria()


    if Decisao1 == 2:
        exec_inspermon()


    if Decisao1 == 3:
        clear()
        slow_type("""
    Estes são todos os inspermon com quem lutou
    Se desejar ver a especificação de algum deles
    Digite o seu número
            
""")

        z=1
        s=0
        for i in insperdex:

            print("""        {0} - {1}""".format(z, insperdex[s][nome]))
            z+=1
            s+=1
        m=int(input("         <>"))

        if m == 0:
            break

        else:
            clear()
            migo=insperdex[m-1]
            print("""



            Nome:{0}
            Nivel:{1}
            Vida:{2}
            Nome do Ataque:{3}
            Força do Ataque:{4}
            Força da Defesa:{5}""" .format(migo[nome], migo[nivel], migo[vida],migo[nome_poder],migo[poder],migo[defesa]))

            input("""

                    
                    Aperte Enter para sair""")















        
