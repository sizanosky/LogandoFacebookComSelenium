"""
* Módulo 20 - Logando no Facebook com Selenium, webdriver
* Criado por Marcos Fabricio Sizanosky
* Professor: Jefferson Santos
* Data criação: 27/05/2021
  Programa em Python 3 para realizar testes com websites.
"""
from time import sleep
import getpass
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from config import URL

print("Hello World!!!")

usuario_facebook = input("Digite o seu e-mail: ")
senha = getpass.getpass("Digite a sua senha: ")
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(URL)

print("\n- Abrindo o Facebook")
sleep(1)

campo_usuario = driver.find_element_by_id('email')
campo_usuario.clear()
campo_usuario.send_keys(usuario_facebook)
print("- Inserindo e-mail usuário >")

campo_senha = driver.find_element_by_id('pass')
campo_senha.send_keys(senha)
print("- Inserindo senha usuário >>")

botao_login = driver.find_element_by_id('loginbutton')
botao_login.click()
print("- Logando no Facebook >>>")

input("- Pressione qualquer tecla para SAIR: ")
driver.quit()
print("Encerrando o programa...")

