!pip install selenium #para windows - abrir uma guia e redirecionar
from selenium import webdriver

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe%s'
driver = webdriver.Chrome(chrome_path)
driver.get("https://open.spotify.com/playlist/6aKw3Z085NuSiK8wPvh7l3?si=81ab8662dede4712")

"""
macOS: chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
linux: chrome_path = '/usr/bin/google-chrome %s'

ou 
macos: your_browser_path = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
driver = webdriver.Chrome(your_browser_path)
driver.get("inserir url")

"""
