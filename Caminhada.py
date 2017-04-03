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


Decisao=0
Chance_de_achar =randint(1,4)
clear()

while True:
            
    slow_type(""" 
   Você decide:
   1 - Andar
   0 - Dormir""")
    Decisao = int(input("""
    <> """))
    
    if Decisao == 0:
        slow_type("""
        Boa noite!
        Esperamos que você volte!
        """)
        break

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
        
    if Chance_de_achar == 1:
        slow_type("""
              Você não achou nenhum inspermon""")

    else:
        import pokemons2
        continue


        