import data
import elements
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

#Inicializar Controlador
driver = webdriver.Chrome()

#Se abre la pagina
driver.get(data.register_url)

#Se instancia el driver de la clase
inlaze_page = elements.InlazeRegisterPage(driver)

#Inicializa el proceso de registro (Pruebas 1-5 & 8-21)
elements.InlazeRegisterPage.register(inlaze_page)

#Inicializa el proceso de inicio de sesion (Pruebas 6 & 7)
elements.InlazeRegisterPage.sing_in(inlaze_page)

driver.quit()