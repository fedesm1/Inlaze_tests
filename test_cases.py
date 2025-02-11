import data
from main import PageClass
import main

page = PageClass(main.driver)

def test_open():
   main.driver.get(data.register_url)

### Prueba 1 registro exitoso con datos validos
def test_1_registration():
    page.valid_data_registration()

### Prueba 2 resgistro sin confirmar contraseña
def test_2_registration_bad_password():
    page.bad_password_registration()

### Prueba 3 registro sin agregar contraseña invalidado
def test_3_registration_no_password():
    page.no_password_registration()

### Prueba 4 registro sin agregar correo invalidada
def test_4_registration_no_email():
    page.no_email_registration()

### Prueba 5 registro sin nombre invalidado
def test_5_registration_no_name():
    page.no_name_registration()

### Prueba 8 el campo "Full name" acepta 2 o más palabras
def test_8_registration_2_words():
    page.registration_2_words()

### Prueba 9 el campo "Full name"  no acepta solo una palabra
def test_9_registration_1_word():
    page.registration_1_word()

### Prueba 10 el campo "Email" se valida con un formato de correo estandar
def test_10_registration_valid_email():
    page.registration_valid_email()

#Prueba 11 el campo "Email" no se valida cuando se ingresa un correo sin el formato estandar.
def test_11_registration_invalid_email():
    page.registration_invalid_email()

### Prueba 12 la contraseña se valida cuando tiene 8 caracteres.
def test_12_registration_8_characters_password():
    page.registration_8_characters_password()

### Prueba 13 la contraseña no se valida cuando no tiene un caracter especial.
def test_13_registration_special_characters_password():
    page.registration_special_characters_password()

### Prueba 14 la contraseña no se valida cuando no tiene numeros.
def test_14_registration_no_numbers_password():
    page.registration_no_numbers_password()

### Prueba 15 la contraseña no se valida cuando no tiene letras minusculas.
def test_15_registration_no_lower_letters_password():
    page.registration_no_lower_letters_password()

### Prueba 16 la contraseña no se valida cuando no letras mayusculas.
def test_16_registration_no_upper_letters_password():
    page.registration_no_upper_letters_password()

### Prueba 17 la contraseña no se valida cuando tiene 7 caracteres.
def test_17_registration_7_characters_password():
    page.registration_7_characters_password()

### Prueba 18 la contraseña no se valida cuando tiene 9 caracteres.
def test_18_registration_9_characters_password():
    page.registration_9_characters_password()

### Prueba 19 se informa si las contraseñas no coinciden
def test_19_registration_unmatch_password():
    page.registration_unmatch_password()

### Prueba 20 no se permite iniciar sesión cuando el campo "Email" esta vacio.
def test_20_registration_empty_email():
    page.registration_empty_email()

### Prueba 21 no se permite iniciar sesión cuando el campo "Password" esta vacio.
def test_21_registration_empty_password():
    page.registration_empty_password()

### Prueba 22 no se debe poder registrar un usuario ya registrado
def test_22_double_user_registration():
    page.registration_double_user_registration()





### Prueba 6 nombre de usuario a la vista
def test_6_user_name_seen():
    page.user_name_seen()

### Prueba 7 se puede cerrar sesión correctamente
def test_7_valid_sign_out():
    page.valid_sign_out()




# Cierre del controlador
def test_close():
   main.driver.quit()









