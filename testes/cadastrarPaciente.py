from selenium import webdriver
from time import sleep



driver = webdriver.Chrome(executable_path='chromedriver//chromedriver.exe')

#localhost = input("digite o local host:\n")
localhost = '127.0.0.1:5000'
loginMedico = '13325885251'

#login
driver.get(f"http://{localhost}")
driver.get(f'http://{localhost}/loginmedico')
driver.find_element_by_name('login').send_keys(loginMedico)
driver.find_element_by_name('senha').send_keys(loginMedico)
driver.find_element_by_css_selector('.btn').click()
#cadastroPaciente
driver.get(f'http://{localhost}/cadastropaciente')
driver.find_element_by_name('name').send_keys('Luiz Carvalho')
driver.find_element_by_name('email').send_keys('LuC@gmail.com')
driver.find_element_by_name('rg').send_keys('260856987')
driver.find_element_by_name('cpf').send_keys('12254785698')
driver.find_element_by_name('telefone').send_keys('21987785452')
driver.find_element_by_name('dataNascimento').send_keys('04111987')
driver.find_element_by_name('sexo').send_keys('Masculino')
driver.find_element_by_css_selector('.btn').click()

print('CADASTRO OK')