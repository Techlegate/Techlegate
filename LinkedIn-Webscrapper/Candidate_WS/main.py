from lib2to3.pgen2 import driver
from functions.start import start
from functions.run import run

driver = start()
run(driver)
driver.close()