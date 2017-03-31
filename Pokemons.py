from random import randint
import time,sys
import json

def slow_type(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(0.05)
with open("inspermons.json","r") as inspermons:
    inspermons = json.load(inspermons)
y = int(input("""Escolha o Inspermon que voce quer invocar:
          0 - pikaxu
          1 - xarmander
          2 - pidijet
          <>"""))
print("")
print("""Voce invocou o:
    {}""".format(inspermons[y]["nome"]))
#Atributos do seu pokemon
nome_amigo = inspermons[y]["nome"]
vida_amigo = inspermons[y]["vida"]
poder_amigo = inspermons[y]["poder"]
defesa_amigo = inspermons[y]["defesa"]


nome_inimigo = inspermons[2]["nome"]
vida_inimigo = inspermons[2]["vida"]
poder_inimigo = inspermons[2]["poder"]
defesa_inimigo = inspermons[2]["defesa"]


AcaoInimigo=3
while vida_amigo>0 and vida_inimigo>0:
    slow_type("""Sua vida é {0}
A vida de seu oponente é{1}""".format(vida_amigo,vida_inimigo))
    AcaoAmigo =int(input("""Escolha:
                    0 - atacar
                    1 - defender
                    2 - tentar fugir
                    <>"""))
    if AcaoAmigo == 0:
        if AcaoInimigo ==1:
            vida_inimigo += defesa_inimigo - poder_amigo
        else:
            vida_inimigo+= -poder_amigo
            
    if AcaoAmigo == 2:
        Fugir = randint(1,10)
        if Fugir > 9:
            break
    
        
           
    if vida_inimigo < 0.1*vida_inimigo:
        AcaoInimigo =randint(0,2)
    else:
        AcaoInimigo =randint(0,1)
    if AcaoInimigo == 0:
        if AcaoAmigo ==1:
            vida_amigo += defesa_amigo - poder_inimigo
        else:
            vida_amigo += -poder_inimigo
        if AcaoInimigo == 2:
            Fugir = randint(1,10)
            if Fugir > 9:
                break
            

