"""
Created on Wed Sep 15 10:53:39 2021
@author: barbara
barbarahmiley@gmail.com
"""

import sys
import sklearn
import matplotlib 

print("Iniciando...")
print("____________________________________________")
print("Olá, eu sou a Alicia!")
print("Bem vindo!")
print()
print("Esse é o conteúdo estatístico sobre LC")
print()
print("ATENÇÃO: para conversar comigo, volte no\t\narquivo anterior.")
print()

def menu():
  print("\tMENU\n\t[1] - Previsão\n\t[2] - Alicia's Playlist\n\t[3] - Esquema")
  escolha_menu = int(input("\tAlicia: Digite o número da opção escolhida: "))
  return escolha_menu

print()
print("____________________________________________________________")

escolha_menu = menu()
print()

#previsão da Alicia - média de quantas palavras uma pessoa sabe de acordo com a idade
if (escolha_menu == 1):
  print()
  print("\tAlicia demonstra em gráfico, a média de quantas palavras\n\tum indivíduo adulto pode saber de acordo com\n\ta média prevista na pesquisa de Altmann (2011).")
  from sklearn.datasets import make_regression
  x, y = make_regression(n_samples=100000, n_features=1, noise=50)
  import matplotlib.pyplot as plt
  plt.scatter(x,y)
  from sklearn.linear_model import LinearRegression
  modelo = LinearRegression()
  modelo.fit(x,y)
  modelo.predict(x)
  plt.scatter(x,y)
  plt.plot(x, modelo.predict(x), color='blue', linewidth=3)
  plt.show()
  print()

#redireciona para a playlist
if (escolha_menu == 2):
  print()
  print("\tAlicia:\tClique no link abaixo e aproveite!")
  print("\tAlicia: https://open.spotify.com/playlist/6aKw3Z085NuSiK8wPvh7l3?si=81ab8662dede4712")

#redireciona para o esquema 
if (escolha_menu == 3):
  print()
  print("\tAlicia: https://drive.google.com/drive/folders/1iupJJBxpvHcxkrxjehxS-KORkIIIHwTB?usp=sharing")

#encerra o programa.
else:
  print("Programa encerrado.")
  exit
