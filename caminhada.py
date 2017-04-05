import sys,time,os
from random import randint

def slow_type(t):
        for l in t:
            sys.stdout.write(l)
            sys.stdout.flush()
            time.sleep(0.05)
def fast_type(t):
        for l in t:
            sys.stdout.write(l)
            sys.stdout.flush()
            time.sleep(0.001)    

def clear():
    time.sleep(1)
    os.system('clear')    


Decisao1=0
Decisao2=0

clear()

while True:

    achar = randint(1,15)
            
    slow_type(""" 
   Você decide:
   1 - Andar
   0 - Dormir""")
    Decisao1 = int(input("""
    <> """))
    
    if Decisao1 == 0:
        slow_type("""
        Boa noite!
        Esperamos que você volte!
        """)
        break

    else:
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
        if achar >= 1 and achar <= 5:
            Decisao2 = 1
        
        #Loja
        if achar ==  6:
        	slow_type("""

        	Voce pode:
        	1 - Ir a Loja
        	0 - Comtimuar andando""")
        	D1 = int(input("""
        	 <> """))
        	if D1 == 1:
        		Decisao2 = 2
        	if D1 == 0:
        		Decisao2 = 0


        #Enfermaria
        if achar ==  7:
            slow_type("""

        	Voce pode:
        	1 - Ir a Enfermaria
        	0 - Comtimuar andando""")
            D2 = int(input("""
             <> """))
            if D2 == 1:
                Decisao2 = 3
            if D2 == 0:
                Decisao2 = 0

        #Batalha+Loja+Enfermaria
        if achar ==  8:
        	slow_type("""

        	Voce pode:
        	1 - Ir a Loja
        	2 - Ir a Enfermaria
        	0 - Comtimuar andando""")
        	D3 = int(input("""
        	 <> """))
        	if D3 == 1:
        		Decisao2 = 2
        	if D3 == 2:
        		Decisao2 = 3
        	if D3 == 0:
        		Decisao2 = 0


        if achar >=9 and achar <=15:
            slow_type("""
                  Você não Achou nada
            """)
            
        #Decisao
        if Decisao2 == 0:
        	continue
        if Decisao2 == 1:
            import batalha
        if Decisao2 == 2:
            import loja
        if Decisao2 == 3:
            import enfermaria



	   

















        
