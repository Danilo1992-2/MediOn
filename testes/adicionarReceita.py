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
#cadastrarReceita
driver.get(f'http://{localhost}/cadastrarreceita')
driver.find_element_by_name('cpf').send_keys('13315381739')
driver.find_element_by_name('crm').send_keys('123456')
driver.find_element_by_name('prescricao').send_keys(
    '''
        teste de prescricao\n
        teste de prescricao\n
        teste de prescricao\n
        teste de prescricao\n
        teste de prescricao\n
    '''
)
driver.find_element_by_css_selector('.btn').click()
print("RECEITA CADASTRADA")