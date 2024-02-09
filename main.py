import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests







def opcion1():
    print("Seleccionaste la opción 1")
    driver =webdriver.Chrome()
    driver.get('https://aarricgra.github.io/')
    driver.maximize_window()
    time.sleep(2)
    element = driver.find_element(By.LINK_TEXT,"CONTÁCTANOS")
    element.click()
    time.sleep(2)
    element = driver.find_element(By.NAME, "Name")
    element.send_keys("Nestor")
    time.sleep(2)
    element = driver.find_element(By.NAME,"Email")
    element.send_keys("Nestor@gmail.com")
    time.sleep(2)
    element = driver.find_element(By.NAME, "Telf")
    element.send_keys("681633623")
    time.sleep(2)
    element=driver.find_element(By.NAME, "Subject")
    element.send_keys("Sujeto Néstor")
    time.sleep(2)
    element=driver.find_element(By.NAME,"Reason")
    element.send_keys("Asunto Néstor")
    time.sleep(2)
    element = driver.find_element(By.XPATH,"//button[@style='font-size: 20px;']")
    element.click()
    time.sleep(2)
    driver.save_screenshot('FormularioHERPmes.png')
    time.sleep(2)

def opcion2():
    print("Seleccionaste la opción 2")
    driver =webdriver.Chrome()
    driver.get("https://www.telepizza.es/")
    driver.maximize_window()
    time.sleep(2)
    element = driver.find_element(By.ID,"cookie-agree")
    element.click()
    time.sleep(2)
    element = driver.find_element(By.XPATH,"//a[@href='https://www.telepizza.es/comida-a-domicilio/ofertas']")
    element.click()
    time.sleep(2)
    element = driver.find_element(By.ID,"bannerPM")
    element.click()
    time.sleep(2)
    element= driver.find_element(By.ID,"storeSelection-select-pickup")
    element.click()
    time.sleep(2)
    element = driver.find_element(By.ID,"searchStore-search-input")
    element.send_keys("Barrio Carbonaire Travesia 8")
    time.sleep(2)
    element = driver.find_element(By.ID,"searchStore-pickup-body__icon")
    element.click()
    time.sleep(2)
    element = driver.find_element(By.CLASS_NAME,"s4d-scroll-content")
    element.click()
    time.sleep(7)
def opcion3():
    print("Seleccionaste la opción 3")

def opcion4():
    print("Seleccionaste la opción 4")

def opcion_default():
    print("Opción no válida")

# Definir un diccionario que mapea los casos a las funciones
switcher = {
    1: opcion1,
    2: opcion2,
    3: opcion3,
    4: opcion4
}

def switch_case(opcion):
    # Obtener la función correspondiente al caso
    func = switcher.get(opcion, opcion_default)
    # Ejecutar la función
    func()

# Ejemplo de uso
opcion = int(input("Ingrese un número de opción: "))
switch_case(opcion)