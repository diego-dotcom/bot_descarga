# BOT de descarga desde Mis Comprobantes - AFIP
# Creado por Diego Mendizábal

import pandas
import time
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys  
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as ec

excel_claves = r'.\claves.xlsx'

df = pandas.read_excel(excel_claves, engine = 'openpyxl')


for i in df.index:
    cuit = int(df['cuit'][i])
    clave = str(df['clave'][i])

    # Comienza el programa abriendo el login en la web de AFIP
    option = webdriver.ChromeOptions()
    option.add_argument('--disable-blink-features=AutomationControlled')
    option.add_experimental_option("excludeSwitches", ["enable-automation"])
    option.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(options=option)
    driver.maximize_window()
    url = "https://auth.afip.gob.ar/contribuyente_/login.xhtml"
    driver.get(url)


    # Borra el campo CUIT e introduce el CUIT
    campo_cuit = driver.find_element_by_id("F1:username")
    campo_cuit.clear()
    campo_cuit.send_keys(cuit)

    boton_cuit = driver.find_element_by_id("F1:btnSiguiente")
    boton_cuit.click()

    # Borra el campo clave e introduce la clave

    campo_clave = driver.find_element_by_id("F1:password")
    campo_clave.clear()
    campo_clave.send_keys(clave)

    boton_clave = driver.find_element_by_id("F1:btnIngresar")
    boton_clave.click()

    time.sleep(100)

    # Click en Mis Servicios (para acceder al menú anterior de AFIP)

    mis_servicios = driver.find_element_by_xpath ("//li[@title='Mis Servicios']")
    mis_servicios.click()

    time.sleep(3)

    
    # Click en Mis Comprobantes
    try:
        mis_comprobantes = driver.find_element_by_xpath ("//div[@title='mcmp']")
    except:
        mis_comprobantes = driver.find_element_by_link_text('Mis Comprobantes')
    mis_comprobantes.click()
    
    time.sleep(3)

    driver.switch_to.window(driver.window_handles[1])

    # Hace click en el contribuyente principal (si existe esa página), sino no hace nada

    try:
        driver.find_element_by_xpath("/html/body/form/main/div/div/div[2]/div/a").click()
        time.sleep(2)

    except:
        pass
    
    # Descarga los comprobantes emitidos del mes anterior

    driver.find_element_by_id("btnEmitidos").click()
    driver.find_element_by_id("fechaEmision").click()
    driver.find_element_by_css_selector("body > div > div.ranges > ul > li:nth-child(6)").click()
    driver.find_element_by_id("buscarComprobantes").click()
    time.sleep(8)
    driver.find_element_by_xpath("//button[@class='btn btn-default buttons-excel buttons-html5 btn-defaut btn-sm sinborde']").click()

    driver.find_element_by_xpath("//a[@href='menuPrincipal.do']").click()
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(2)

    # Descarga los comprobantes recibidos del mes anterior
    driver.find_element_by_id("btnRecibidos").click()
    driver.find_element_by_id("fechaEmision").click()
    driver.find_element_by_css_selector("body > div > div.ranges > ul > li:nth-child(6)").click()
    driver.find_element_by_id("buscarComprobantes").click()
    time.sleep(8)
    driver.find_element_by_xpath("//button[@class='btn btn-default buttons-excel buttons-html5 btn-defaut btn-sm sinborde']").click()


    #Sale de Mis Comprobantes
    driver.find_element_by_xpath("//a[@title='Salir...']").click()


    #Confirma el alert
    alert = driver.switch_to.alert
    alert.accept()

    driver.switch_to.window(driver.window_handles[0])

    #Se desloguea
    try:
        driver.find_element_by_xpath("//a[@title='Salir']").click()
    except:
        driver.find_element_by_xpath('//*[@id="cssmenu"]/ul/li[3]/a')

    driver.close()

