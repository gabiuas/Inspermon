from random import randint
import time,sys
import json
import os

def slow_type(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(0.065)

def slow_type2(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(0.1)


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
nivel="nivel"




clear()
slow_type("""
    Bem vindo a nossa Enfermaria!

    Nós curamos a vida do seu Inspermon ate que ela esteja perfeita!
    
    Você quer?:
        1 - Curar
        0 - Cancelar""")
cura = int(input("""
         <>"""))

if cura == 1:


    clear()
    slow_type("""
    Você pode curar apenas um inspermon por vez
    Qual inspermon você deseja curar?

""")

    i=0
    while i < len(inspermons_amigos):

        n=0
        if inspermons_amigos[i][0][nivel] > 5:
            n+=1
            if inspermons_amigos[i][n][nivel] > 5:
                n+=1

        print("""        %d - %s""" %(i,inspermons_amigos[i][n][nome]))
        i+=1


    seu_amigo = int(input("""           <>"""))

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
        slow_type2("""
    ...
    ...
    ...""")
        slow_type("""
    Pronto, a vida do seu {} ja esta curada!""".format(amigo[nome]))

    amigo[vida]=amigo[vida_maxima]







clear()
slow_type("""
    Deseja salvar suas alterações?
    1 - Sim
    0 - Não""")
salvar = int(input("""
    <>"""))
if salvar == 1:
    with open("inspermons_amigos.json", "w") as arquivo:
        json.dump(inspermons_amigos, arquivo)


slow_type("""
    Esperamos te ver denovo!
""")
