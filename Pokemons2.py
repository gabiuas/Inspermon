from random import randint
import time,sys
import json

def slow_type(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(0.067)
with open("inspermons.json","r") as inspermons:
    inspermons = json.load(inspermons)
    
amigo=0
nome="nome"
vida="vida"
poder="poder"
defesa="defesa"


slow_type("""
    Escolha o Inspermon que você quer invocar:""")
seu_amigo = int(input("""
          0 - Pikachu
          1 - Charmander
          2 - Pidijey
          <>"""))
#Definição Inspermons
amigo=inspermons[seu_amigo]
inimigo=inspermons[randint(0,2)]
    
slow_type("""

    Você invocou o:
    {0}
    ...
    Você irá batalhar com o {1}""".format(amigo[nome], inimigo[nome]))
#Atributos do seu pokemon

AcaoInimigo=3
while amigo[vida]>0 and inimigo[vida]>0:
    slow_type("""

    Sua vida é {0}
    A vida de seu oponente é {1}""".format(amigo[vida],inimigo[vida]))
    AcaoAmigo =int(input("""
        Escolha:
            0 - atacar
            1 - defender
            2 - tentar fugir
            <>"""))
    if AcaoAmigo == 0:
        if AcaoInimigo ==1:
            if amigo[poder]>=inimigo[defesa]:
                inimigo[vida] += inimigo[defesa] - amigo[poder]
                slow_type("""
    Você tirou {} de Vida do seu oponente""".format(amigo[poder]-inimigo[defesa]))
        else:
            inimigo[vida]+= -amigo[poder]
            slow_type("""
    Você tirou {} de Vida""".format(amigo[poder]))
            
    if AcaoAmigo == 2:
        Fugir = randint(1,10)
        if Fugir > 9:
            slow_type("""
        Voce fugiu da batalha""")
            break
            
    
        
           
    if inimigo[vida] < 0.1*inimigo[vida]:
        AcaoInimigo =randint(0,2)
    else:
        AcaoInimigo =randint(0,1)
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
        O oponente fugio da batalha""")
                break
                


