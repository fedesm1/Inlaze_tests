import data
import elements
from selenium import webdriver

#Inicializar Controlador
driver = webdriver.Chrome()

#Comando para abrir el sitio web
driver.get(data.register_url)

#Se instancia el driver de la clase
inlaze_page = elements.InlazeRegisterPage(driver)

#Inicializa el proceso de registro (Pruebas 1-5 & 8-21)
elements.InlazeRegisterPage.register(inlaze_page)

#Inicializa el proceso de inicio de sesion (Pruebas 6 & 7)
elements.InlazeRegisterPage.sing_in(inlaze_page)

driver.quit()