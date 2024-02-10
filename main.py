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
    driver = webdriver.Chrome()
    driver.get("https://www.telepizza.es/")
    driver.maximize_window()
    time.sleep(2)
    element = driver.find_element(By.ID, "cookie-agree")
    element.click()
    time.sleep(2)
    element = driver.find_element(By.XPATH, "//a[@href='https://www.telepizza.es/comida-a-domicilio/ofertas']")
    element.click()
    time.sleep(2)
    element = driver.find_element(By.ID, "bannerPM")
    element.click()
    time.sleep(2)
    element = driver.find_element(By.ID, "storeSelection-select-pickup")
    element.click()
    time.sleep(2)
    element = driver.find_element(By.ID, "searchStore-search-input")
    element.send_keys("Barrio Carbonaire Travesia 8")
    time.sleep(2)
    element = driver.find_element(By.ID, "searchStore-pickup-body__icon")
    element.click()
    time.sleep(3)
    element = driver.find_element(By.CLASS_NAME, "s4d-scroll-content")
    element.click()
    time.sleep(3)
    element = driver.find_element(By.ID, "orderDetails-start-order-button")
    element.click()
    time.sleep(2)
    element = driver.find_element(By.ID, "s4d-modal-confirm-no")
    element.click()
    time.sleep(2)
    element = driver.find_element(By.ID, "bannerPM")
    element.click()
    time.sleep(2)
    element = driver.find_element(By.CLASS_NAME, "flavor-selector__button")
    element.click()
    time.sleep(2)
    element = driver.find_element(By.ID, "search-button-329")
    element.click()
    time.sleep(2)
    element = driver.find_element(By.ID, "coupon-configurator-order-button")
    element.click()
    time.sleep(2)
    element = driver.find_element(By.ID, "receipt-place-order")
    element.click()
    time.sleep(2)
    element = driver.find_element(By.ID, "select-upsell-products-close")
    element.click()
    time.sleep(2)
    driver.save_screenshot('PedidoTelepizza.png')
    time.sleep(3)
def opcion3():
    print("Seleccionaste la opción 3")
    driver = webdriver.Chrome()
    driver.get(
        "https://www.dominospizza.es/promociones-pizza-a-domicilio?gad_source=1&gclid=CjwKCAiA2pyuBhBKEiwApLaIO-DKerb-KnTSz5_z9iH9MZsUrVP5lmN8gE48lvVp2PPXqKWBXB3IFRoCWMIQAvD_BwE&gclsrc=aw.ds")
    driver.maximize_window()
    time.sleep(2)
    element = driver.find_element(By.ID, "onetrust-accept-btn-handler")
    element.click()
    time.sleep(2)
    element = driver.find_element(By.LINK_TEXT, "Crea tu pizza")
    element.click()
    time.sleep(2)
    element = driver.find_element(By.ID, "selectTamanioDet")
    element.click()
    time.sleep(2)
    element = driver.find_element(By.CLASS_NAME, "ico ico-pizza-half")
    element.click()
    time.sleep(2)
    element = driver.find_element(By.CLASS_NAME, "product-carousel-item-figure")
    element.click()
    time.sleep(2)

def opcion4():
    print("Seleccionaste la opción 4")
    driver = webdriver.Chrome()
    driver.get("https://www.game.es/")
    driver.maximize_window()
    time.sleep(2)
    element = driver.find_element(By.ID, "btnCookiesAcceptAll")
    element.click()
    time.sleep(2)
    element = driver.find_element(By.ID, "searchinput")
    element.send_keys("PlayStation 5 consola")
    time.sleep(2)
    element = driver.find_element(By.ID, "submitsearch")
    element.click()
    time.sleep(4)
    element = driver.find_element(By.LINK_TEXT, "Más información")
    element.click()
    time.sleep(2)
    element = driver.find_element(By.CLASS_NAME, "product-thumbnail-anchor")
    element.click()
    time.sleep(2)

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