usua =  {"id": 1, "email": "sebas@gmail.com", "phone": "2307699402", "password": "sebas123"}

# Jueguito ejercicio
import random

vidas = 5

puntos = 0

while(vidas != 0):

    num=random.randint(0,9)

    if num == 0:
        vidas -=1
        print(f'vidas: {vidas}')
    
    else:
        puntos +=1
        print(f"puntos: {puntos}")
