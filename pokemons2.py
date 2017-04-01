from random import randint
import time,sys
import json

def slow_type(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(0.067)
with open("inspermons_amigos.json","r") as inspermons_amigos:
    inspermons_amigos = json.load(inspermons_amigos)
with open("inspermons_inimigos.json","r") as inspermons_inimigos:
    inspermons_inimigos = json.load(inspermons_inimigos)    
    
amigo=0
nome="nome"
vida="vida"
poder="poder"
defesa="defesa"

x=0
while x<1:
    
    slow_type("""
    Escolha o Inspermon que você quer invocar:""")
    seu_amigo = int(input("""
          0 - Pikachu
          1 - Charmander
          2 - Pidijey
          <>"""))
#Definição Inspermons
    if seu_amigo<0 or seu_amigo>2:
        slow_type("""
    Digite um comando valido
    """)
    else:
        amigo=inspermons_amigos[seu_amigo]
        inimigo=inspermons_inimigos[randint(0,2)]
        x=1
    
slow_type("""

    Você invocou o:
    {0}
    ...
    Você irá batalhar contra um {1}""".format(amigo[nome], inimigo[nome]))
#Atributos do seu pokemon

AcaoInimigo=3
while amigo[vida]>0 and inimigo[vida]>0:
    slow_type("""

    Seu Inspermon esta com {0} de Vida
    Seu oponente esta com {1} de Vida
    """.format(amigo[vida],inimigo[vida]))
    AcaoAmigo =int(input("""
        Você...
            0 - ataca
            1 - defende
            2 - tenta fugir
            <>"""))
    if AcaoAmigo<0 or AcaoAmigo>2:
        slow_type("""
   Como você é engraçado
   Eu tambem sei ser engraçado 
   Você perdeu seu turno""")

    elif AcaoAmigo == 0:
        slow_type("""
        
        Você Escolheu atacar""")
        if AcaoInimigo ==1:
            if amigo[poder]>=inimigo[defesa]:
                inimigo[vida] += inimigo[defesa] - amigo[poder]
                slow_type("""
    Você causou {} de dano em seu oponente """.format(amigo[poder]-inimigo[defesa]))
        else:
            inimigo[vida]+= -amigo[poder]
            slow_type("""
    Você causou {} de dano em seu oponente""".format(amigo[poder]))
    elif AcaoAmigo == 1:
        slow_type("""
        
                  Você escolheu Defender""")
            
    if AcaoAmigo == 2:
        Fugir = randint(1,10)
        if Fugir > 9:
            slow_type("""
            
        Voce fugiu da batalha
        """)
            break
        slow_type("""
        
        Você não conseguiu fugir""")
            
    
        
           
    if inimigo[vida] < 0.1*inimigo[vida]:
        AcaoInimigo =randint(0,2)
    else:
        AcaoInimigo =randint(0,1)
    if AcaoInimigo == 0:
        slow_type("""
        
        Seu oponente usou Atacar""")
    elif AcaoInimigo == 1:
        slow_type("""
        
        Seu oponente usou Defesa""")
    
    if AcaoInimigo == 0:
        if AcaoAmigo ==1:
            if inimigo[poder]>=amigo[defesa]:
                amigo[vida] += amigo[defesa] - inimigo[poder]
                slow_type("""
    Você perdeu {} de Vida""".format(inimigo[poder]-amigo[defesa]))
        else:
            amigo[vida] += -inimigo[poder]
            slow_type("""
    Você perdeu {} de Vida""".format(inimigo[poder]))
        if AcaoInimigo == 2:
            Fugir = randint(1,10)
            if Fugir > 9:
                slow_type("""
        O oponente fugiu da batalha
        """)
            else:
                slow_type("""
                Seu oponente tentou fugir""")
                break
if amigo[vida]<=0:
    slow_type("""
    Seu Pokemon morreu...
    Você perdeu a batalha.
    """)
if inimigo[vida]<=0:
    slow_type("""
    Você derrotou seu oponente!!
       Mais um conquista !!!
    """)


                


