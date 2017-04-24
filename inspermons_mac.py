from random import randint
import time,sys
import json
import os

def slow_type(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(0.065)


def clear():
    time.sleep(1)
    os.system('clear')


with open("inspermons_amigos.json","r") as inspermons_amigos:
    inspermons_amigos = json.load(inspermons_amigos)


nome="nome"
vida="vida"
vida_maxima="vida_maxima"
poder="poder"
defesa="defesa"
nome_poder="nome_poder"
xp="xp"
nivel="nivel"



clear()
slow_type("""
    Deseja ver as especificações de qual inspermon?
    (Vovê também poderá alterar o nome deste inspermon)

""")


i=0
while i < len(inspermons_amigos):
    n=0
    if inspermons_amigos[i][0][nivel] > 5:
        n+=1
        if inspermons_amigos[i][n][nivel] > 5:
            n+=1

    print("""           %d - %s""" %(i,inspermons_amigos[i][n][nome]))
    i+=1


seu_amigo = int(input("""            <>"""))

if seu_amigo<0 or seu_amigo>=i:
    slow_type("""
    Digite um comando valido""")
else:
    n=0
    if inspermons_amigos[seu_amigo][0][nivel] > 5:
        n+=1
        if inspermons_amigos[seu_amigo][n][nivel] > 5:
            n+=1

amigo=inspermons_amigos[seu_amigo][n]
slow_type("""
    Você escolheu o {}""".format(amigo[nome]))

clear()
print("""
        


    Nome:{0}
    Nivel:{1}
    Vida:{2}
    Nome do Ataque:{3}
    Força do Ataque:{4}
    Força da Defesa:{5}""" .format(amigo[nome], amigo[nivel], amigo[vida],amigo[nome_poder],amigo[poder],amigo[defesa]))


slow_type("""

        Aperte:
      1 - Alterar nome do Inspermon
      0 - Sair""")

sorte=int(input("""
       <>"""))

if sorte == 1:
    clear()
    slow_type("""
    Digite o nome que deseja dar ao seu inspermon""")
    nom=input("""
        <> """)
    amigo[nome]=nom
    slow_type("""
    O nome do seu inspermon foi alterado para: "{}" """.format(amigo[nome]))

    with open("inspermons_amigos.json", "w") as arquivo:
        json.dump(inspermons_amigos, arquivo)










