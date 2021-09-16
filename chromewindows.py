!pip install selenium #para windows - abrir uma guia e redirecionar
from selenium import webdriver

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe%s'
driver = webdriver.Chrome(chrome_path)
driver.get("https://open.spotify.com/playlist/6aKw3Z085NuSiK8wPvh7l3?si=81ab8662dede4712")

#para mudar o navegador, só trocar o nome do chrome pelo navegador desejado. Observar também o endereço onde o navegador fica hospedado no windows.
