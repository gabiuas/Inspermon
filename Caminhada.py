import sys,time
from random import randint
Quebra= 0
Decisao=0
Chance_de_achar = 0
def slow_type(t):
        for l in t:
            sys.stdout.write(l)
            sys.stdout.flush()
            time.sleep(0.05)
def fast_type(t):
        for l in t:
            sys.stdout.write(l)
            sys.stdout.flush()
            time.sleep(0.000000000001)            
while Quebra!=1:
    Decisao = 0
    Quebra = 0
    
    while True:
            
        slow_type(""" 
   Você decide:
   1 - Andar
   0 - Dormir""")
        Decisao = int(input("   <>"))
        break
    
    if Decisao == 0:
        break
                    
    slow_type("""
                  <>Você decidiu caminhar<>""")
    
        
    fast_type("""
                      oooO
         @           (....).... Oooo....          @
         @           .\..(.....(....)...          @
         @           ..\_)..... )../....          @
         @           .......... (_/.....          @
         @            oooO                        @
         @           (....)....Oooo.....          @
         @           .\..(.....(....)...          @
         @           ..\_)..... )../....          @
         @           ...........(_/.....          @
        """ )
        
    Chance_de_achar =2 #randint(1,2)
    if Chance_de_achar == 1:
        slow_type("Você não achou nenhum inspermon")
    else:
        import pokemons2
        