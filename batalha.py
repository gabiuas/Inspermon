from random import randint
import time,sys
import json
import os

def slow_type(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(0.067)


def clear1():
    time.sleep(2)
    os.system('cls')

def clear():
    time.sleep(1)
    os.system('cls')
    


with open("inspermons_amigos.json","r") as inspermons_amigos:
    inspermons_amigos = json.load(inspermons_amigos)
with open("inspermons_inimigos.json","r") as inspermons_inimigos:
    inspermons_inimigos = json.load(inspermons_inimigos)    
    
amigo=0
nome="nome"
vida="vida"
poder="poder"
defesa="defesa"
nome_poder="nome_poder"

ii=randint(0,2)
inimigo=inspermons_inimigos[ii]

slow_type("""
             Um {} selvagem apareceu!""".format(inimigo[nome]))
x=0
while x<1:

    clear1()
    slow_type("""
    Escolha o Inspermon que você quer usar para batalhar:""")
    seu_amigo = int(input("""
          0 - Pikachu
          1 - Charmander
          2 - Pidgey
          <>"""))

#Definição Inspermons
    if seu_amigo<0 or seu_amigo>2:
        slow_type("""
    Digite um comando valido""")
    else:
        amigo=inspermons_amigos[seu_amigo]
        slow_type("""
    Você escolheu o {}""".format(amigo[nome]))
        x=1


slow_type("""
    Vai {0}!""".format(amigo[nome]))


#Atributos do seu pokemon

while amigo[vida]>0 and inimigo[vida]>0:
    
    clear()
    slow_type("""
    Seu {0} esta com {1} de Vida
    O {2} adversario esta com {3} de Vida""".format(amigo[nome],amigo[vida],inimigo[nome],inimigo[vida]))
    print("")
    AcaoAmigo =int(input("""
        Você...
            0 - Ataca
            1 - Defende
            2 - Tenta fugir
            <>"""))

    if inimigo[vida] < 0.1*inimigo[vida]:
        AcaoInimigo =randint(0,2)
    else:
        AcaoInimigo =randint(0,1)

    if AcaoAmigo<0 or AcaoAmigo>2:
        

        slow_type("""
   Como você é engraçado
   Eu tambem sei ser engraçado 
   Você perdeu seu turno""")

    elif AcaoAmigo == 0:
        
        slow_type("""

    Você Escolheu atacar""")



        if AcaoInimigo==0:
            inimigo[vida]+= -amigo[poder]
            amigo[vida]+= -inimigo[poder]

            slow_type("""
    O oponente escolheu atacar""")

            slow_type("""
    {0} usou {1}""".format(amigo[nome],amigo[nome_poder]))

            slow_type("""
    O {0} adversario usou {1}
    """.format(inimigo[nome],inimigo[nome_poder]))

            slow_type("""
    Você causou {} de dano em seu oponente""".format(amigo[poder]))
            


            slow_type("""
    Você recebeu {} de dano do seu oponente""".format(inimigo[poder]))

        if AcaoInimigo ==1:
            if amigo[poder]>inimigo[defesa]:
                inimigo[vida] += inimigo[defesa] - amigo[poder]


                slow_type("""
    O oponente escolheu defender""")

                slow_type("""
    {0} usou {1}""".format(amigo[nome],amigo[nome_poder]))


                slow_type("""
    Seu oponente defendeu parcialmente seu ataque.""")
                slow_type("""
    Você causou {} de dano em seu oponente """.format(amigo[poder]-inimigo[defesa]))
            
            if inimigo[defesa]>=amigo[poder]:

                slow_type("""
    Seu oponente defendeu seu ataque.""")
        
        if AcaoInimigo == 2:
            Fugir = randint(1,10)
            if Fugir > 9:
                               slow_type("""
        O oponente fugiu da batalha
        """)
            else:

                slow_type("""
        Seu oponente tentou fugir
        """)
                inimigo[vida]+= -amigo[poder]

                slow_type("""
    Você causou {} de dano em seu oponente""".format(amigo[poder]))
                break

    elif AcaoAmigo == 1:
        slow_type("""

    Você Escolheu defender""")

        if AcaoInimigo==0:

            slow_type("""
    O oponente escolheu atacar""")


            slow_type("""
        O {0} adversario usou {1}
        """.format(inimigo[nome],inimigo[nome_poder]))
            if inimigo[poder]>amigo[defesa]:
                amigo[vida] += amigo[defesa] - inimigo[poder]

                slow_type("""
    Você defendeu parcialmente o ataque do seu inimigo.""")
                
                slow_type("""
    Você recebeu {} de dano do seu oponente""".format(inimigo[poder]))

            if amigo[defesa]>=inimigo[poder]:

                slow_type("""
    Você defendeu o ataquedo seu oponente.""")
            

        if AcaoInimigo ==1:
            slow_type("""
    Seu imnimigo tambem tentou se defender.""")
        
        if AcaoInimigo == 2:
            Fugir = randint(1,10)
            if Fugir > 9:

                slow_type("""
        O oponente fugiu da batalha
        """)
            else:

                slow_type("""
        Seu oponente tentou fugir
        """)
                break

    if AcaoAmigo == 2:
        Fugir = randint(1,10)
        if Fugir > 9:

            slow_type("""
        Você fugiu da batalha""")
            break
        else:
            if AcaoInimigo==0:
                amigo[vida]+= -inimigo[poder]
                slow_type("""
    Você tentou fugir, mas não teve sucesso.""")

                slow_type("""
    O oponente escolheu atacar""")

                slow_type("""
    O {0} adversario usou {1}""".format(inimigo[nome],inimigo[nome_poder]))
                    

                slow_type("""
    Você recebeu {} de dano do seu oponente""".format(inimigo[poder]))
                


if amigo[vida]<=0:
    clear()
    slow_type("""
    Seu Pokemon morreu...

    Você perdeu a batalha.
    """)
if inimigo[vida]<=0:
    clear()
    slow_type("""
    O inimigo {0} Morreu!!
    {1} ganhou {2} pontos de EXP.
    Mais um conquista !!!
    """.format(inimigo[nome],amigo[nome],(inimigo[vida]*0.1)))






























    
