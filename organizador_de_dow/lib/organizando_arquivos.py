import shutil
import os
from time import sleep
from organizador_de_dow.lib.funcoes import *

path = "C:\\Users\\us\\Downloads"
lista_de_pontos = list()


while True:
    if not os.listdir(path) == []:
        for c in os.listdir(path):
            lista_de_pontos.append(tira_tipo(c))

        lista_de_tipos = tirando_iguais(lista_de_pontos)

        if not os.path.exists("C:\\Users\\us\\Documents\\organizadin"):
            os.mkdir("C:\\Users\\us\\Documents\\organizadin")

        for tipo in lista_de_tipos:
            if not os.path.exists(os.path.join("C:\\Users\\us\\Documents\\organizadin", tipo)):
                os.mkdir(os.path.join("C:\\Users\\us\\Documents\\organizadin", tipo))

        for file in os.listdir(path):
            for arq in os.listdir("C:\\Users\\us\\Documents\\organizadin"):
                if tira_tipo(file) == os.path.basename(arq):
                    v = os.path.join(path, file)
                    w = os.path.join("C:\\Users\\us\\Documents\\organizadin", arq)
                    shutil.move(v, w)
    sleep(10)

