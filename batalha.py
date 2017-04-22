from random import randint
import time,sys
import json
import os

def slow_type(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(0.065)


def clear1():
    time.sleep(2)
    os.system('cls')

def clear():
    time.sleep(1)
    os.system('cls')

def esperar():
    time.sleep(3)






with open("inspermons_amigos.json","r") as inspermons_amigos:
    inspermons_amigos = json.load(inspermons_amigos)
with open("inspermons_inimigos.json","r") as inspermons_inimigos:
    inspermons_inimigos = json.load(inspermons_inimigos)
with open("insperdex.json","r") as insperdex:
    insperdex = json.load(insperdex)
    
amigo=0
nome="nome"
vida="vida"
vida_maxima="vida_maxima"
poder="poder"
defesa="defesa"
nome_poder="nome_poder"
xp="xp"
nivel="nivel"



y=len(inspermons_amigos)



slow_type("""
             Um Inspermon selvagem apareceu!""")


#Definição Inspermon

x=0
while x<1:

    clear1()
    slow_type("""
    Escolha o Inspermon que você quer usar para batalhar:

""")

    i=0
    while i< len(inspermons_amigos):

        n=0
        if len(inspermons_amigos[i])>n+1:
            if inspermons_amigos[i][n][nivel] > 5:
                n+=1

                if len(inspermons_amigos[i])>n+1:
                    if inspermons_amigos[i][n][nivel] > 5:
                        n+=1

        print("""        {0} - {1}""".format(i, inspermons_amigos[i][n][nome]))
        i+=1






    seu_amigo = int(input("""         <>"""))

    if seu_amigo<0 or seu_amigo>=i:
        slow_type("""
    Digite um comando valido""")
    else:
        n=0
        if inspermons_amigos[seu_amigo][n][nivel] > 5:
            n+=1
            if inspermons_amigos[seu_amigo][n][nivel] > 5:
                n+=1
        amigo=inspermons_amigos[seu_amigo][n]

    if amigo[vida]<=0:
        slow_type("""
    Este inspermon esta sem vida, vá até a Enfermaria para recupera-lo!""")
        esperar()
        sys.exit()

    else:

        slow_type("""
    Você escolheu o {}""".format(amigo[nome]))
        x=1


        slow_type("""
    Vai {0}!""".format(amigo[nome]))



#Definicao inimigo
    ii=randint(0,38)
    inimigo=inspermons_inimigos[ii][n]

    slow_type("""

        Seu adversario é o {}""".format(inimigo[nome]) )


#Experiência
pontos_ganhos=inimigo[nivel]*10


#Batalha

while amigo[vida]>0 and inimigo[vida]>0:

    sorte=randint(0,10)
    
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

    if inimigo[vida] < 0.2*inimigo[vida]:
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

        if sorte==10:
            amigo[poder]=amigo[poder]-amigo[poder]//10
            slow_type("""
    Por escolha do destino seu ataque diminuiu 1/10
    Seu novo ataque causa {} de dano
    """.format(amigo[poder]))
        if sorte==9:
            amigo[poder]=amigo[poder]+amigo[poder]//10
            slow_type("""
    Por escolha do destino seu ataque aumentou 1/10
    Seu novo ataque causa {} de dano
    """.format(amigo[poder]))
        if AcaoInimigo==0:
            inimigo[vida]+= -amigo[poder]
            amigo[vida]+= -inimigo[poder]

            slow_type("""
    O oponente escolheu atacar""")

            slow_type("""
    Seu {0} usou {1}""".format(amigo[nome],amigo[nome_poder]))

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
    Seu {0} usou {1}""".format(amigo[nome],amigo[nome_poder]))


                slow_type("""
    Seu oponente defendeu parcialmente seu ataque""")
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
            AcaoInimigo=0
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
    amigo[xp]+=pontos_ganhos
    amigo[nivel]=amigo[xp]//100

    slow_type("""
    O inimigo {0} Morreu!!
    Seu {1} ganhou {2} pontos de EXP
    Seu inspermon esta no nivel {3}
    Mais um conquista !!!
    """.format(inimigo[nome],amigo[nome],pontos_ganhos,amigo[nivel]))



    if amigo[nivel]>5:
        slow_type("""
    Parabéns, seu inspermon evoluiu!""")

    inimigo[vida]=0
    inspermons_amigos.append(inspermons_inimigos[ii])
    slow_type("""
    Você capturou mais um inspermon!!!
    Mas infelizmente ele voltou para o sua evolução básica""")
    with open("inspermons_amigos.json", "w") as arquivo:
        json.dump(inspermons_amigos, arquivo)

  
insperdex.append(inspermons_inimigos[ii])

clear()
slow_type("""
    Deseja salvar o seu progresso?
    1 - Sim
    0 - Não""")
salvar = int(input("""
     <>"""))
if salvar == 1:
    with open("inspermons_amigos.json", "w") as arquivo:
        json.dump(inspermons_amigos, arquivo)
    with open("insperdex.json", "w") as arquivo:
        json.dump(insperdex, arquivo)

