# Prueba técnica Inlaze
## Descripción

En esta prueba se realizan verificaciones para algunas de funcionalidades y caracteristicas de la paguina test-qa.inlaze.com, basadas en los siguientes requisitos [Inlaze Requirements](https://drive.google.com/file/d/1JMPkqDPXQ12rldVpmZlH7QLYiAgtv8jM/view?usp=sharing)

## Estructura

- Casos de prueba [Test Cases](https://docs.google.com/spreadsheets/d/10POY3no5IjTm5viC-4hyzc9akf1RbbCzZH50s7OuGOs/edit?usp=sharing)
- Informe de errores [Bug Reports](https://www.notion.so/Seguimiento-de-bugs-17eaf11d03788028bf9fedf84af52cb1?pvs=4)
- Archivos del repositorio
  
  - data.py : Contiene los datos de prueba 
  - elements.py : Contiene los localizadores y métodos para la paguina web
  - page.py: Contiene los llamados a las pruebas



## Requisitos para ejecutar el código
  - Navegador : Google Chrome.
  - IDE : Python & PyCharm.
  - Webdriver : Chromedriver
  - Librerias : Selenium.
    
## Instrucciones 

  - Instalar Python en la computadora.
  - Instalar PyCharm COMMUNITY EDITION [Download PyCharm](https://www.jetbrains.com/products/compare/?product=pycharm&product=pycharm-ce)
  - Actualizar Navegador Google Chrome a la ultima versión.
  - Instalar Chromedriver
    
    - Selecciona la versión que mejor coincida con versión del navegador Google Chrome que tengas en el momento [Download Webdriver](https://developer.chrome.com/docs/chromedriver/downloads)
    - Después de descargarlo ejecuta su archivo .exe
      
  - Abre Pycharm y crea un nuevo proyecto dandole a las 3 lineas de la parte superior izquierda y ponle el nombre que quieras.
  - Instala la libreria Selenium dirigiendote a la sección "Python Packages" en la parte inferior izquierda, escribe "Selenium en el buscador y dale en "Install".
  - Crea los tres archivos indicados anteriormente en la sección Estructura con los mismos nombres dando clic derecho en el nombre del proyecyo y seleccionando "Python file".
  - Copia los códigos desde los archivos de este repositorio y pegalos en sus respectivos archivos en tu proyecto de PyCharm.
  - Dirigete al archivo page.py y en la parte superior derecha dale clic en icono triangular verde "Run".
  - Se abrira una pestaña de Chrome y se realizaran las pruebas automaticamente.
  - Cuando se terminen las pruebas la pestaña se cerrara y en la barra de herramientas en la parte inferior de PyCharm se podra ver los resultados de cada prueba.
    
  
