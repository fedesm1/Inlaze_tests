from time import sleep

from selenium.webdriver.common.devtools.v85.dom import get_attributes
from typing_extensions import assert_type
import data
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By


#En esta clase se define la paguina web, y las variables de la clase definen los elementos de la pagina web como atributos de la clase
class InlazeRegisterPage:

    #Elementos de formulario de registro
    name_field = (By.ID, 'full-name')
    email_field = (By.ID, 'email')
    password_field = (By.XPATH, '/html/body/app-root/app-sign-up/main/section[2]/app-sign-up-form/form/div[3]/app-password/div/input')
    repeat_password_field = (By.XPATH, '/html/body/app-root/app-sign-up/main/section[2]/app-sign-up-form/form/div[4]/app-password/div/input')
    password_match_message = (By.XPATH, "/html/body/app-root/app-sign-up/main/section[2]/app-sign-up-form/form/div[4]/label[2]/span")



    #Segmento de validación
    valid_section = (By.XPATH, '/html/body/app-root/app-sign-up/main/section[2]/app-sign-up-form/form')

    #Elementos de inicio y cierre de sesión
    sing_in_email_field = (By.ID, 'email')
    sing_in_password_field = (By.XPATH, '/html/body/app-root/app-sign-in/main/section[1]/app-sign-in-form/form/div[2]/app-password/div/input')
    sing_in_button = (By.XPATH, "/html/body/app-root/app-sign-in/main/section[1]/app-sign-in-form/form/button")
    name_letters = (By.CLASS_NAME,"font-bold")
    avatar_icon = (By.XPATH,"/html/body/app-root/app-panel-root/app-navbar/div/div[2]/div/div/label/div/img")
    logout_button = (By.XPATH,"/html/body/app-root/app-panel-root/app-navbar/div/div[2]/div/ul/li[3]/a")
    sing_in_letters = (By.XPATH, "/html/body/app-root/app-sign-in/main/section[1]/app-sign-in-form/h1")



    #Inicializador de controlador
    def __init__(self, driver):
        self.driver = driver

    #Función para realizar acciones de registro
    def register(self):

        ### Prueba 1 registro exitoso con datos validos
        full_name_field = self.driver.find_element(*self.name_field)
        full_name_field.send_keys(data.data1[0])

        email_signup_field= self.driver.find_element(*self.email_field)
        email_signup_field.send_keys(data.data1[1])

        password_signup_field = self.driver.find_element(*self.password_field)
        password_signup_field.send_keys(data.data1[2])

        repeat_password_field = self.driver.find_element(*self.repeat_password_field)
        repeat_password_field.send_keys(data.data1[2])

        #Localizador de validador de formulario
        def locate_validation ():
            validation = self.driver.find_element(*self.valid_section)
            attribute = validation.get_attribute("class")
            return attribute

        #Comprobación de la prueba 1
        try:
            assert 'ng-valid' in locate_validation(), "ERROR EN PRUEBA 1"
        except AssertionError as e:
            print(e)
        else:
            print("Prueba 1 : registro exitoso con datos validos, APROBADA.")


        #Función para borrar campos y proceder con la siguiente prueba
        def clear():
            full_name_field.send_keys(Keys.CONTROL + "a")
            full_name_field.send_keys(Keys.DELETE)

            email_signup_field.send_keys(Keys.CONTROL + "a")
            email_signup_field.send_keys(Keys.DELETE)

            password_signup_field.send_keys(Keys.CONTROL + "a")
            password_signup_field.send_keys(Keys.DELETE)

            repeat_password_field.send_keys(Keys.CONTROL + "a")
            repeat_password_field.send_keys(Keys.DELETE)
        clear()



        ### Prueba 2 resgistro sin confirmar contraseña

        full_name_field.send_keys(data.data2[0])
        email_signup_field.send_keys(data.data2[1])
        password_signup_field.send_keys(data.data2[2])
        repeat_password_field.send_keys(data.data2[3])

        # Comprobación de la prueba 2
        try:
            assert 'ng-valid' not in locate_validation(), "ERROR EN PRUEBA 2"
        except AssertionError as e:
            print(e)
        else:
            print("Prueba 2 : registro sin confirmar contraseña invalidado, APROBADA.")
        clear()



        ### Prueba 3 registro sin agregar contraseña invalidado

        full_name_field.send_keys(data.data3[0])
        email_signup_field.send_keys(data.data3[1])
        password_signup_field.send_keys(data.data3[2])
        repeat_password_field.send_keys(data.data3[3])

        # Comprobación de la prueba 3
        try:
            assert 'ng-valid' not in locate_validation(), "ERROR EN PRUEBA 3"
        except AssertionError as e:
            print(e)
        else:
            print("Prueba 3 : registro sin agregar contraseña invalidado, APROBADA.")
        clear()



        ### Prueba 4 registro sin agregar correo invalidada

        full_name_field.send_keys(data.data4[0])
        email_signup_field.send_keys(data.data4[1])
        password_signup_field.send_keys(data.data4[2])
        repeat_password_field.send_keys(data.data4[2])

        # Comprobación de la prueba 4
        try:
            assert 'ng-valid' not in locate_validation(), "ERROR EN PRUEBA 4"
        except AssertionError as e:
            print(e)
        else:
            print("Prueba 4 : registro sin agregar correo invalidada, APROBADA.")
        clear()



        ### Prueba 5 registro sin nombre invalidado

        full_name_field.send_keys(data.data5[0])
        email_signup_field.send_keys(data.data5[1])
        password_signup_field.send_keys(data.data5[2])
        repeat_password_field.send_keys(data.data5[2])

        # Comprobación de la prueba 5
        try:
            assert 'ng-valid' not in locate_validation(), "ERROR EN PRUEBA 5"
        except AssertionError as e:
            print(e)
        else:
            print("Prueba 5 : registro sin nombre invalidado, APROBADA.")
        clear()


        # Saltamos hasta la prueba 8, ya que las pruebas 6 y 7 segun los casos de prueba se realizan en otra pestaña

        ### Prueba 8 el campo "Full name" acepta 2 o más palabras

        full_name_field.send_keys(data.data8[0])
        email_signup_field.send_keys(data.data8[1])
        password_signup_field.send_keys(data.data8[2])
        repeat_password_field.send_keys(data.data8[2])

        # Comprobación de la prueba 8
        try:
            assert 'ng-valid' in locate_validation(), "ERROR EN PRUEBA 8"
        except AssertionError as e:
            print(e)
        else:
            print("Prueba 8 : el campo 'Full name' acepta 2 o más palabras, APROBADA.")
        clear()



        ### Prueba 9 el campo "Full name"  no acepta solo una palabra

        full_name_field.send_keys(data.data9[0])
        email_signup_field.send_keys(data.data9[1])
        password_signup_field.send_keys(data.data9[2])
        repeat_password_field.send_keys(data.data9[2])

        # Comprobación de la prueba 9
        try:
            assert 'ng-valid' not in locate_validation(), "ERROR EN PRUEBA 9"
        except AssertionError as e:
            print(e)
        else:
            print("Prueba 9 : el campo 'Full name'  no acepta solo una palabra, APROBADA.")
        clear()



        ### Prueba 10 el campo "Email" se valida con un formato de correo estandar

        full_name_field.send_keys(data.data10[0])
        email_signup_field.send_keys(data.data10[1])
        password_signup_field.send_keys(data.data10[2])
        repeat_password_field.send_keys(data.data10[2])

        # Comprobación de la prueba 10
        try:
            assert 'ng-valid' in locate_validation(), "ERROR EN PRUEBA 10"
        except AssertionError as e:
            print(e)
        else:
            print("Prueba 10 : el campo 'Email' se valida con un formato de correo estandar, APROBADA.")
        clear()






        ### Prueba 11 el campo "Email" no se valida cuando se ingresa un correo sin el formato estandar.

        full_name_field.send_keys(data.data11[0])
        email_signup_field.send_keys(data.data11[1])
        password_signup_field.send_keys(data.data11[2])
        repeat_password_field.send_keys(data.data11[2])

        # Comprobación de la prueba 11
        try:
            assert 'ng-valid' not in locate_validation(), "---¡ERROR EN PRUEBA 11, EL FORMATO DE CORREO SE VALIDA¡"
        except AssertionError as e:
            print(e)
        else:
            print("Prueba 11 : El campo 'Email' no se valida cuando se ingresa un correo sin el formato estandar., APROBADA.")
        clear()



        ### Prueba 12 la contraseña se valida cuando tiene 8 caracteres.

        full_name_field.send_keys(data.data12[0])
        email_signup_field.send_keys(data.data12[1])
        password_signup_field.send_keys(data.data12[2])
        repeat_password_field.send_keys(data.data12[2])

        # Comprobación de la prueba 12
        try:
            assert 'ng-valid' in locate_validation(), "¡ERROR EN PRUEBA 12¡"
        except AssertionError as e:
            print(e)
        else:
            print(
                "Prueba 12 : La contraseña de valida cuando tiene 8 caracteres., APROBADA.")
        clear()



        ### Prueba 13 la contraseña no se valida cuando no tiene un caracter especial.

        full_name_field.send_keys(data.data13[0])
        email_signup_field.send_keys(data.data13[1])
        password_signup_field.send_keys(data.data13[2])
        repeat_password_field.send_keys(data.data13[2])

        # Comprobación de la prueba 13
        try:
            assert 'ng-valid' not in locate_validation(), "---¡ERROR EN PRUEBA 13, SE VALIDA LA CONTRASEÑA SIN CARACTER ESPECIAL¡"
        except AssertionError as e:
            print(e)
        else:
            print(
                "Prueba 13 : La contraseña no se valida cuando no tiene un caracter especial., APROBADA.")
        clear()

        ### Prueba 14 la contraseña no se valida cuando no tiene numeros.

        full_name_field.send_keys(data.data14[0])
        email_signup_field.send_keys(data.data14[1])
        password_signup_field.send_keys(data.data14[2])
        repeat_password_field.send_keys(data.data14[2])

        # Comprobación de la prueba 14
        try:
            assert 'ng-valid' not in locate_validation(), "---¡ERROR EN PRUEBA 14¡"
        except AssertionError as e:
            print(e)
        else:
            print(
                "Prueba 14 : La contraseña no se valida cuando no tiene números, APROBADA.")
        clear()

        ### Prueba 15 la contraseña no se valida cuando no letras minusculas.

        full_name_field.send_keys(data.data15[0])
        email_signup_field.send_keys(data.data15[1])
        password_signup_field.send_keys(data.data15[2])
        repeat_password_field.send_keys(data.data15[2])

        # Comprobación de la prueba 15
        try:
            assert 'ng-valid' not in locate_validation(), "---¡ERROR EN PRUEBA 15¡"
        except AssertionError as e:
            print(e)
        else:
            print(
                "Prueba 15 : La contraseña no se valida cuando no letras minusculas, APROBADA.")
        clear()

        ### Prueba 16 la contraseña no se valida cuando no letras mayusculas.

        full_name_field.send_keys(data.data16[0])
        email_signup_field.send_keys(data.data16[1])
        password_signup_field.send_keys(data.data16[2])
        repeat_password_field.send_keys(data.data16[2])

        # Comprobación de la prueba 16
        try:
            assert 'ng-valid' not in locate_validation(), "---¡ERROR EN PRUEBA 16¡"
        except AssertionError as e:
            print(e)
        else:
            print(
                "Prueba 16 : La contraseña no se valida cuando no letras mayusculas, APROBADA.")
        clear()





        ### Prueba 17 la contraseña no se valida cuando tiene 7 caracteres.

        full_name_field.send_keys(data.data17[0])
        email_signup_field.send_keys(data.data17[1])
        password_signup_field.send_keys(data.data17[2])
        repeat_password_field.send_keys(data.data17[2])

        # Comprobación de la prueba 17
        try:
            assert 'ng-valid' not in locate_validation(), "---¡ERROR EN PRUEBA 17, SE VALIDA LA CONTRASEÑA CON 7 CARACTERES¡"
        except AssertionError as e:
            print(e)
        else:
            print(
                "Prueba 17 : La contraseña no se valida cuando tiene 7 caracteres, APROBADA.")
        clear()




        ### Prueba 18 la contraseña no se valida cuando tiene 9 caracteres.

        full_name_field.send_keys(data.data18[0])
        email_signup_field.send_keys(data.data18[1])
        password_signup_field.send_keys(data.data18[2])
        repeat_password_field.send_keys(data.data18[2])

        # Comprobación de la prueba 18
        try:
            assert 'ng-valid' not in locate_validation(), "---¡ERROR EN PRUEBA 18, SE VALIDA LA CONTRASEÑA CON 9 CARACTERES¡"
        except AssertionError as e:
            print(e)
        else:
            print(
                "Prueba 18 : La contraseña no se valida cuando tiene 9 caracteres, APROBADA.")
        clear()




        ### Prueba 19 se informa si las contraseñas no coinciden



        full_name_field.send_keys(data.data19[0])
        email_signup_field.send_keys(data.data19[1])
        password_signup_field.send_keys(data.data19[2])
        repeat_password_field.send_keys(data.data19[3])

        # Comprobación de la prueba 19

            # Identificador se mensaje sobre coincidencia de la cntraseña
        passwords_match = self.driver.find_element(*self.password_match_message)
        message_password_text = passwords_match.text

        try:
            assert 'Passwords do not match' in message_password_text , "---¡ERROR EN PRUEBA 19¡"
        except AssertionError as e:
            print(e)
        else:
            print(
                "Prueba 19 : Se informa si las contraseñas no coinciden, APROBADA.")
        clear()




        ### Prueba 20 no se permite iniciar sesión cuando el campo "Email" esta vacio.

        full_name_field.send_keys(data.data20[0])
        email_signup_field.send_keys(data.data20[1])
        password_signup_field.send_keys(data.data20[2])
        repeat_password_field.send_keys(data.data20[2])

        # Comprobación de la prueba 20
        try:
            assert 'ng-valid' not in locate_validation(), "---¡ERROR EN PRUEBA 20¡"
        except AssertionError as e:
            print(e)
        else:
            print(
                "Prueba 20 : No se permite iniciar sesión cuando el campo 'Email' esta vacio., APROBADA.")
        clear()

        ### Prueba 21 no se permite iniciar sesión cuando el campo "Password" esta vacio.

        full_name_field.send_keys(data.data21[0])
        email_signup_field.send_keys(data.data21[1])
        password_signup_field.send_keys(data.data21[2])
        repeat_password_field.send_keys(data.data21[3])

        # Comprobación de la prueba 20
        try:
            assert 'ng-valid' not in locate_validation(), "---¡ERROR EN PRUEBA 21¡"
        except AssertionError as e:
            print(e)
        else:
            print(
                "Prueba 21 : No se permite iniciar sesión cuando el campo 'Password' esta vacio, APROBADA.")
        clear()



### Pruebas 6 & 7


    #Función para acciones de inicio de sesión
    def sing_in(self):

        self.driver.get(data.sing_in_url)

        ### Prueba 6 nombre de usuario a la vista

        field0 = self.driver.find_element(*self.sing_in_email_field)
        field0.send_keys(data.user_email)

        field1 = self.driver.find_element(*self.sing_in_password_field)
        field1.send_keys(data.user_password)

        field2 = self.driver.find_element(*self.sing_in_button)
        field2.click()
        time.sleep(3)
        letters = self.driver.find_elements(*self.name_letters)
        name = letters[1].text

        # Comprobación de la prueba 6
        try:
            assert data.user_name == name, "ERROR EN PRUEBA 6"
        except AssertionError as e:
            print(e)
        else:
            print("Prueba 6 : Nombre de usuario a la vista, APROBADA")

        ### Prueba 7 se puede cerrar sesión correctamente

        avatar_photo = self.driver.find_element(*self.avatar_icon)
        avatar_photo.click()

        logout = self.driver.find_element(*self.logout_button)
        logout.click()



        try:
            letters_of_sing_in = self.driver.find_element(*self.sing_in_letters)
            letter_text = letters_of_sing_in.text
            assert letter_text == "Sign in", "ERROR EN PRUEBA 7"
        except AssertionError as e:
            print(e)
        else:
            print("Prueba 7 : Se puede cerrar sesión correctamente, APROBADA")






