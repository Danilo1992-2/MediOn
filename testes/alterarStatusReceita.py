from selenium import webdriver
from time import sleep


driver = webdriver.Chrome(executable_path='chromedriver//chromedriver.exe')

cpfBusca= '13315381739'
localhost = '127.0.0.1:5000'
loginfarmacia = '123456789121'

#loginMedico
driver.get(f"http://{localhost}")
driver.get(f'http://{localhost}/loginfarmacia')
driver.find_element_by_name('login').send_keys(loginfarmacia)
driver.find_element_by_name('senha').send_keys(loginfarmacia)
driver.find_element_by_css_selector('.btn').click()
#Buscar e vender  NECESSÁRIO HAVER UMA RECEITACOM STATUS 'D'
driver.get(f'http://{localhost}/consultareceitafarmacia')
driver.find_element_by_name('search').send_keys(cpfBusca)
driver.find_element_by_css_selector('.btn').click()
driver.find_element_by_xpath("//section[@id='features8-2s']/div/div/div[2]/form/div/div[2]/button").click()
print("STATUS ALTERADO PARA V(VENDIDO)")