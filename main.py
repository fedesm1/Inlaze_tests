import data
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

driver = webdriver.Chrome()

class PageClass:

### Elementos de formulario de registro
    name_field = (By.ID, 'full-name')
    second_name_field = (By.ID, 'full-name')
    email_field = (By.ID, 'email')
    password_field = (By.XPATH, '/html/body/app-root/app-sign-up/main/section[2]/app-sign-up-form/form/div[3]/app-password/div/input')
    repeat_password_field = (By.XPATH, '/html/body/app-root/app-sign-up/main/section[2]/app-sign-up-form/form/div[4]/app-password/div/input')
    password_unmatch_message = (By.XPATH, "/html/body/app-root/app-sign-up/main/section[2]/app-sign-up-form/form/div[4]/label[2]/span")
    sign_up_button = (By.XPATH, "/html/body/app-root/app-sign-up/main/section[2]/app-sign-up-form/form/button")
    sign_up_button_back = (By.XPATH, "/html/body/app-root/app-sign-in/main/section[1]/app-sign-in-form/span/a")
    registration_message = (By.XPATH, "/html/body/app-root/app-toasts-container/div/app-toast/div/div[2]")

    # Segmento de validación
    valid_section = (By.XPATH, '/html/body/app-root/app-sign-up/main/section[2]/app-sign-up-form/form')

### Elementos de inicio y cierre de sesión
    sign_in_email_field = (By.ID, 'email')
    sign_in_password_field = (By.XPATH, '/html/body/app-root/app-sign-in/main/section[1]/app-sign-in-form/form/div[2]/app-password/div/input')
    sign_in_button = (By.XPATH, "/html/body/app-root/app-sign-in/main/section[1]/app-sign-in-form/form/button")
    name_letters = (By.CLASS_NAME, "font-bold")
    avatar_icon = (By.XPATH, "/html/body/app-root/app-panel-root/app-navbar/div/div[2]/div/div/label/div/img")
    logout_button = (By.XPATH, "/html/body/app-root/app-panel-root/app-navbar/div/div[2]/div/ul/li[3]/a")
    sign_in_letters = (By.XPATH, "/html/body/app-root/app-sign-in/main/section[1]/app-sign-in-form/h1")
    welcome_message = (By.XPATH, "/html/body/app-root/app-panel-root/main/section[1]/h2")

    def __init__(self, driver):
        self.driver = driver

    def clear(self):

        full_name_field = self.driver.find_element(*self.name_field)
        full_name_field.send_keys(Keys.CONTROL + "a")
        full_name_field.send_keys(Keys.DELETE)

        email_signup_field = self.driver.find_element(*self.email_field)
        email_signup_field.send_keys(Keys.CONTROL + "a")
        email_signup_field.send_keys(Keys.DELETE)

        password_signup_field = self.driver.find_element(*self.password_field)
        password_signup_field = self.driver.find_element(*self.password_field).send_keys(Keys.CONTROL + "a")
        password_signup_field = self.driver.find_element(*self.password_field).send_keys(Keys.DELETE)

        repeat_password_field = self.driver.find_element(*self.repeat_password_field)
        repeat_password_field.send_keys(Keys.CONTROL + "a")
        repeat_password_field.send_keys(Keys.DELETE)

    # Localizador de validador de formulario
    def locate_validation(self):
        validation = self.driver.find_element(*self.valid_section)
        attribute = validation.get_attribute("class")
        return attribute


    def valid_data_registration(self):

        full_name_field = self.driver.find_element(*self.name_field).send_keys(data.data1[0])
        email_signup_field = self.driver.find_element(*self.email_field).send_keys(data.data1[1])
        password_signup_field = self.driver.find_element(*self.password_field).send_keys(data.data1[2])
        repeat_password_field = self.driver.find_element(*self.repeat_password_field).send_keys(data.data1[2])

        # Comprobación de la prueba 1
        assert 'ng-valid' in PageClass.locate_validation(self), "ERROR EN PRUEBA 1"


    def bad_password_registration(self):

        PageClass.clear(self)

        full_name_field = self.driver.find_element(*self.name_field).send_keys(data.data2[0])
        email_signup_field = self.driver.find_element(*self.email_field).send_keys(data.data2[1])
        password_signup_field = self.driver.find_element(*self.password_field).send_keys(data.data2[2])
        repeat_password_field = self.driver.find_element(*self.repeat_password_field).send_keys(data.data2[3])

        assert 'ng-valid' not in PageClass.locate_validation(self), "ERROR EN PRUEBA 2"


    def no_password_registration(self):

        PageClass.clear(self)

        full_name_field = self.driver.find_element(*self.name_field).send_keys(data.data3[0])
        email_signup_field = self.driver.find_element(*self.email_field).send_keys(data.data3[1])
        password_signup_field = self.driver.find_element(*self.password_field).send_keys(data.data3[2])
        repeat_password_field = self.driver.find_element(*self.repeat_password_field).send_keys(data.data3[3])

        assert 'ng-valid' not in PageClass.locate_validation(self), "ERROR EN PRUEBA 3"


    def no_email_registration(self):

        PageClass.clear(self)

        full_name_field = self.driver.find_element(*self.name_field).send_keys(data.data4[0])
        email_signup_field = self.driver.find_element(*self.email_field).send_keys(data.data4[1])
        password_signup_field = self.driver.find_element(*self.password_field).send_keys(data.data4[2])
        repeat_password_field = self.driver.find_element(*self.repeat_password_field).send_keys(data.data4[2])

        assert 'ng-valid' not in PageClass.locate_validation(self), "ERROR EN PRUEBA 4"


    def no_name_registration(self):

        PageClass.clear(self)

        full_name_field = self.driver.find_element(*self.name_field).send_keys(data.data5[0])
        email_signup_field = self.driver.find_element(*self.email_field).send_keys(data.data5[1])
        password_signup_field = self.driver.find_element(*self.password_field).send_keys(data.data5[2])
        repeat_password_field = self.driver.find_element(*self.repeat_password_field).send_keys(data.data5[2])

        assert 'ng-valid' not in PageClass.locate_validation(self), "ERROR EN PRUEBA 5"


    def registration_2_words(self):

        PageClass.clear(self)

        full_name_field = self.driver.find_element(*self.name_field).send_keys(data.data8[0])
        email_signup_field = self.driver.find_element(*self.email_field).send_keys(data.data8[1])
        password_signup_field = self.driver.find_element(*self.password_field).send_keys(data.data8[2])
        repeat_password_field = self.driver.find_element(*self.repeat_password_field).send_keys(data.data8[2])

        assert 'ng-valid' in PageClass.locate_validation(self), "ERROR EN PRUEBA 8"


    def registration_1_word(self):

        PageClass.clear(self)

        full_name_field = self.driver.find_element(*self.name_field).send_keys(data.data9[0])
        email_signup_field = self.driver.find_element(*self.email_field).send_keys(data.data9[1])
        password_signup_field = self.driver.find_element(*self.password_field).send_keys(data.data9[2])
        repeat_password_field = self.driver.find_element(*self.repeat_password_field).send_keys(data.data9[2])

        assert 'ng-valid' not in PageClass.locate_validation(self), "ERROR EN PRUEBA 9"


    def registration_valid_email(self):

        PageClass.clear(self)

        full_name_field = self.driver.find_element(*self.name_field).send_keys(data.data10[0])
        email_signup_field = self.driver.find_element(*self.email_field).send_keys(data.data10[1])
        password_signup_field = self.driver.find_element(*self.password_field).send_keys(data.data10[2])
        repeat_password_field = self.driver.find_element(*self.repeat_password_field).send_keys(data.data10[2])

        assert 'ng-valid' in PageClass.locate_validation(self), "ERROR EN PRUEBA 10"

    def registration_invalid_email(self):

        PageClass.clear(self)

        full_name_field = self.driver.find_element(*self.name_field).send_keys(data.data11[0])
        email_signup_field = self.driver.find_element(*self.email_field).send_keys(data.data11[1])
        password_signup_field = self.driver.find_element(*self.password_field).send_keys(data.data11[2])
        repeat_password_field = self.driver.find_element(*self.repeat_password_field).send_keys(data.data11[2])

        assert 'ng-valid' not in PageClass.locate_validation(self), "ERROR EN PRUEBA 11"


    def registration_8_characters_password(self):

        PageClass.clear(self)

        full_name_field = self.driver.find_element(*self.name_field).send_keys(data.data12[0])
        email_signup_field = self.driver.find_element(*self.email_field).send_keys(data.data12[1])
        password_signup_field = self.driver.find_element(*self.password_field).send_keys(data.data12[2])
        repeat_password_field = self.driver.find_element(*self.repeat_password_field).send_keys(data.data12[2])

        assert 'ng-valid' in PageClass.locate_validation(self), "ERROR EN PRUEBA 12"


    def registration_special_characters_password(self):

        PageClass.clear(self)

        full_name_field = self.driver.find_element(*self.name_field).send_keys(data.data13[0])
        email_signup_field = self.driver.find_element(*self.email_field).send_keys(data.data13[1])
        password_signup_field = self.driver.find_element(*self.password_field).send_keys(data.data13[2])
        repeat_password_field = self.driver.find_element(*self.repeat_password_field).send_keys(data.data13[2])

        assert 'ng-valid' not in PageClass.locate_validation(self), "ERROR EN PRUEBA 13"


    def registration_no_numbers_password(self):

        PageClass.clear(self)

        full_name_field = self.driver.find_element(*self.name_field).send_keys(data.data14[0])
        email_signup_field = self.driver.find_element(*self.email_field).send_keys(data.data14[1])
        password_signup_field = self.driver.find_element(*self.password_field).send_keys(data.data14[2])
        repeat_password_field = self.driver.find_element(*self.repeat_password_field).send_keys(data.data14[2])

        assert 'ng-valid' not in PageClass.locate_validation(self), "ERROR EN PRUEBA 14"


    def registration_no_lower_letters_password(self):

        PageClass.clear(self)

        full_name_field = self.driver.find_element(*self.name_field).send_keys(data.data15[0])
        email_signup_field = self.driver.find_element(*self.email_field).send_keys(data.data15[1])
        password_signup_field = self.driver.find_element(*self.password_field).send_keys(data.data15[2])
        repeat_password_field = self.driver.find_element(*self.repeat_password_field).send_keys(data.data15[2])

        assert 'ng-valid' not in PageClass.locate_validation(self), "ERROR EN PRUEBA 15"


    def registration_no_upper_letters_password(self):

        PageClass.clear(self)

        full_name_field = self.driver.find_element(*self.name_field).send_keys(data.data16[0])
        email_signup_field = self.driver.find_element(*self.email_field).send_keys(data.data16[1])
        password_signup_field = self.driver.find_element(*self.password_field).send_keys(data.data16[2])
        repeat_password_field = self.driver.find_element(*self.repeat_password_field).send_keys(data.data16[2])

        assert 'ng-valid' not in PageClass.locate_validation(self), "ERROR EN PRUEBA 16"


    def registration_7_characters_password(self):

        PageClass.clear(self)

        full_name_field = self.driver.find_element(*self.name_field).send_keys(data.data17[0])
        email_signup_field = self.driver.find_element(*self.email_field).send_keys(data.data17[1])
        password_signup_field = self.driver.find_element(*self.password_field).send_keys(data.data17[2])
        repeat_password_field = self.driver.find_element(*self.repeat_password_field).send_keys(data.data17[2])

        assert 'ng-valid' not in PageClass.locate_validation(self), "ERROR EN PRUEBA 17"


    def registration_9_characters_password(self):

        PageClass.clear(self)

        full_name_field = self.driver.find_element(*self.name_field).send_keys(data.data18[0])
        email_signup_field = self.driver.find_element(*self.email_field).send_keys(data.data18[1])
        password_signup_field = self.driver.find_element(*self.password_field).send_keys(data.data18[2])
        repeat_password_field = self.driver.find_element(*self.repeat_password_field).send_keys(data.data18[2])

        assert 'ng-valid' not in PageClass.locate_validation(self), "ERROR EN PRUEBA 18"


    def registration_unmatch_password(self):

        PageClass.clear(self)

        full_name_field = self.driver.find_element(*self.name_field).send_keys(data.data19[0])
        email_signup_field = self.driver.find_element(*self.email_field).send_keys(data.data19[1])
        password_signup_field = self.driver.find_element(*self.password_field).send_keys(data.data19[2])
        repeat_password_field = self.driver.find_element(*self.repeat_password_field).send_keys(data.data19[3])

        passwords_match = self.driver.find_element(*self.password_unmatch_message)
        unmatch_message_password_text = passwords_match.text

        assert 'Passwords do not match' in unmatch_message_password_text , "---¡ERROR EN PRUEBA 19¡"


    def registration_empty_email(self):

        PageClass.clear(self)

        full_name_field = self.driver.find_element(*self.name_field).send_keys(data.data20[0])
        email_signup_field = self.driver.find_element(*self.email_field).send_keys(data.data20[1])
        password_signup_field = self.driver.find_element(*self.password_field).send_keys(data.data20[2])
        repeat_password_field = self.driver.find_element(*self.repeat_password_field).send_keys(data.data20[2])

        assert 'ng-valid' not in PageClass.locate_validation(self), "---¡ERROR EN PRUEBA 20¡"


    def registration_empty_password(self):

        PageClass.clear(self)

        full_name_field = self.driver.find_element(*self.name_field).send_keys(data.data21[0])
        email_signup_field = self.driver.find_element(*self.email_field).send_keys(data.data21[1])
        password_signup_field = self.driver.find_element(*self.password_field).send_keys(data.data21[2])
        repeat_password_field = self.driver.find_element(*self.repeat_password_field).send_keys(data.data21[3])

        assert 'ng-valid' not in PageClass.locate_validation(self), "---¡ERROR EN PRUEBA 21¡"


    def registration_double_user_registration(self):

        PageClass.clear(self)

        full_name_field = self.driver.find_element(*self.name_field).send_keys(data.data22[0])
        email_signup_field = self.driver.find_element(*self.email_field).send_keys(data.data22[1])
        password_signup_field = self.driver.find_element(*self.password_field).send_keys(data.data22[2])
        repeat_password_field = self.driver.find_element(*self.repeat_password_field).send_keys(data.data22[2])
        click = sign_up_button_click = self.driver.find_element(*self.sign_up_button)
        click.click()

        sign_up_button_wait = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(PageClass.sign_up_button_back))

        self.driver.get(data.register_url)

        full_name_field = self.driver.find_element(*self.name_field)
        full_name_field.send_keys(data.data22[0])

        email_signup_field = self.driver.find_element(*self.email_field)
        email_signup_field.send_keys(data.data22[1])

        password_signup_field = self.driver.find_element(*self.password_field)
        password_signup_field.send_keys(data.data22[2])

        repeat_password_field = self.driver.find_element(*self.repeat_password_field)
        repeat_password_field.send_keys(data.data22[2])

        sign_up_button_click = self.driver.find_element(*self.sign_up_button)
        sign_up_button_click.click()

        registration_valid_wait = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(PageClass.registration_message))
        registration_valid = self.driver.find_element(*self.registration_message)
        valid_message = registration_valid.text

        assert 'Successful registration!' not in valid_message, "---¡ERROR EN PRUEBA 22, Se valida el registro de un usuario ya registrado¡"


    def user_name_seen(self):

        self.driver.get(data.sing_in_url)

        sign_in_field = self.driver.find_element(*self.sign_in_email_field)
        sign_in_field.send_keys(data.user_email)

        password_field = self.driver.find_element(*self.sign_in_password_field)
        password_field.send_keys(data.user_password)

        sign_in_click = self.driver.find_element(*self.sign_in_button).click()

        letter_wait = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(PageClass.welcome_message))
        letters = self.driver.find_elements(*self.name_letters)
        name_letters_validation = letters[1].text

        assert data.user_name == name_letters_validation, "---!ERROR EN PRUEBA 6¡"


    def valid_sign_out(self):

        avatar_wait = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(PageClass.avatar_icon))
        avatar_photo = self.driver.find_element(*self.avatar_icon).click()

        logout = self.driver.find_element(*self.logout_button)
        logout.click()

        letters_of_sing_in = self.driver.find_element(*self.sign_in_letters)
        letter_text = letters_of_sing_in.text

        assert letter_text == "Sign in", "---¡ERROR EN PRUEBA 7¡"

