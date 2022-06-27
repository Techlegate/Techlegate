from Functions.start import start
from Functions.run import run

# Calling start function to create driver
driver = start()

# Calling run function function for scraping job
run(driver)

# SHutting down driver after use
driver.close()