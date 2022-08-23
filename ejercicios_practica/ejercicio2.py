# JSON ETL [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

import json
import requests

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
     #creo el grafico
    data1 = []

#def bar_plot():
    usuarios = ['userId 1 - UserId 3', 'userId 4 - userId 6', 'userId 7 - UserId 9', 'userId 10']
    libros = ['title 1', 'title 2', 'title 3', 'title 4', 'title 5', 'title 6', 'title 7', 'title 8', 'title 9', 'title 10']
    fig = plt.figure()
    fig.suptitle('usuarios - libros', fontsize=16)
    ax = fig.add_subplot()

    ax.bar(usuarios, libros, label='libro')
    ax.set_facecolor('whitesmoke')
    ax.legend()
    plt.show()

    url = "https://jsonplaceholder.typicode.com/todos"
    data1 = extract(url)
  
    x, y = transform(data1)

    # Ejercicio de consumo de datos por API
    
    # def upate_animation(frame):

def extract(url):
    
    response = requests.get(url)
    data1 =response.json()
    return data1

def transform(data1):
    # Transformar los datos en dos vectores
    # para graficar
    x = [d['usuarios'] for d in data1]
    y =[d['titulos'] for d in data1]
    return x, y

def load(x ,y):
        



    return load (x, y)
    
    response = requests.get("https://jsonplaceholder.typicode.com/todos")
    data4 = response.json()
    #return data4
    print('imprimo los datos traidos de la url')
    print(json.dumps(data4, indent = 4))

    for user in data4:
        if user ['userId'] > 1:
            break
        print('El usuario {} completó {}? {}'.format(user['userId'],
                                                      user['title'],
                                                      user['completed']
                                                      ))

    # Extraer el JSON de la URL pasada
    # como parámetro
   # 
    #data1 = response.json() #en response nos quedamos con todo lo similar a json
    #nos retorna una lista de diccionario

    # El primer paso es que copien esa URL en su explorador web
    # y analicen los datos en general:
    # 1) Observando la URL se puede ver que en total hay 200 entradas,
    # del id=1 al id=200
    # 2) Observando la URL se puede ver que en total hay 10 usuarios,
    # del userId=1 al userId=10
    # 3) En cada entrada se especifica si el usuario completó ese título,
    # mediante el campo "completed".


    # Alumno, de cada usuario en el total de las 200 entradas
    # debe contar cuantos títulos completó cada usuario (de los 10 posibles)
    # y armar un gráfico de barras resumiendo la información.
    # gráfico en el eje "x" está cada uno de los 10 usuarios y en el eje
    # "y" la cantidad de títulos completados

    # Para poder ir haciendo esto debe ir almacenando la información
    # de cada usuario a medida que "itera" en un bucle los datos
    # del JSON recolectado. Al finalizar el bucle deberá tener la data
    # de los 10 usuarios con cuantos títulos completó cada uno.

    # Debe poder graficar dicha información en un gráfico de barras.
    # En caso de no poder hacer el gráfico comience por usar print
    # para imprimir cuantos títulos completó cada usuario
    # y verifique si los primeros usuarios (mirando la página a ojo)
    # los datos recolectados son correctos.

    print("terminamos")