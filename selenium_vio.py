from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options)

driver.get("https://estadisticasviolenciagenero.igualdad.gob.es/portalEstadistico.html")

select_element = driver.find_element(By.CLASS_NAME, 'cubes')
select = Select(select_element)
select.select_by_visible_text('Menores víctimas mortales por vdg')

# Click als indicadors
val = driver.find_element(By.XPATH, '//*[@title="Número de menores víctimas mortales"]')
val.click()

# Desplegar totes les carpetes per poder clickar als elements
elements = driver.find_elements(By.CLASS_NAME, 'folder_collapsed')
for e in elements:
    e.click()

# val = driver.find_element(By.XPATH, '//*[@title="Tramos de edad del agresor"]')
# val.click()

# Clicar a cadascun dels elements. Si triga molt a retornar les dades s'espera 10 segons i ho torna a provar.
elements = driver.find_elements(By.CLASS_NAME, 'level')
for e in elements:
    ok = None
    intents = 0
    while ok is None:
        try:
            # Si poses província i CCAA a vegades es queda lelo, amb el que prescindim de CCAA que es derivada
            if e.text == 'Comunidad autónoma':
                pass
            else:
                e.click()
                time.sleep(1)
            ok = True
        except:
            print("Entra error:" + e.text + " -- " + str(intents))
            intents+=1
            time.sleep(10)


# esperem  10 segons a que calculi les dades
time.sleep(10)
# Exportar a CSV
val = driver.find_element(By.XPATH, '//*[@title="Exportar CSV"]')
val.click()


driver.quit()
