from random import randint
import time,sys
import json
import os

def slow_type(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(0.067)


def clear():
    time.sleep(1)
    os.system('clear')


clear()
slow_type("""
	Programa em desenvolvimento""")