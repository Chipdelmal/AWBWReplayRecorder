
from time import sleep
from os import path
from PIL import Image
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


URL = 'https://awbw.amarriner.com/2030.php?games_id=347352&ndx='
DRV = './chromedriver/chromedriver'
OUT = './img/'
TRN = 74
SLP = 10
# Load driver and mainpage ----------------------------------------------------
print('* Loading selenium scraper...')
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(DRV, options=options)
# Iterate through frames ------------------------------------------------------
for ndx in range(4):
    driver.get('{}{}'.format(URL, ndx))
    sleep(SLP)
    # driver.execute_script("document.body.style.zoom='150%'")
    imgName = 'turn_{}.png'.format(str(ndx).zfill(3))
    imgPath = path.join(OUT, imgName)
    element = driver.find_element_by_id('gamecontainer').screenshot(imgPath)

# # element = driver.find_element_by_id('gamemap-container')
# (location, size) = (element.location, element.size)
# driver.save_screenshot(path.join(OUT, imgName))
# # crop image
# (x, y) = (location['x'], location['y'])
# width = location['x']+size['width']
# height = location['y']+size['height']
# im = Image.open(path.join(OUT, "screenshot.png"))
# im = im.crop((int(x), int(y), int(width), int(height)))
# im.save(path.join(OUT, imgName))

