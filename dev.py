
import os
from sys import argv
from time import sleep
from os import path
from PIL import Image
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import constants as cst

(ID, NAME) = ('344511', '02_Witchez-Chip_Yami_Richie')
(TRN, ZOM, MAP_ONLY) = (103, 15, True)
# Create output folder --------------------------------------------------------
URL = 'https://awbw.amarriner.com/2030.php?games_id={}&ndx='.format(ID)
OUT_PTH = path.join(cst.OUT_PTH, NAME)
if not path.exists(OUT_PTH):
    os.makedirs(OUT_PTH)
# Load driver and mainpage ----------------------------------------------------
print('* Loading selenium scraper...', end='\r')
options = webdriver.ChromeOptions()
if cst.HEADLESS:
    options.add_argument("--window-size=1920x1080")
    options.add_argument("--headless")
else:
    options.add_argument("--start-maximized")
driver = webdriver.Chrome(cst.DRV_PTH, options=options)
driver.get('{}{}'.format(URL, 0))
# Set zoom --------------------------------------------------------------------
for i in range(ZOM):
    driver.find_element_by_id('zoom-in').click()
# Prepend identifier to filenames ---------------------------------------------
prep = 'S'
if MAP_ONLY:
    prep = 'M'
# Iterate through frames ------------------------------------------------------
for ndx in range(0, TRN+1):
    print('* Parsing ({}/{})'.format(ndx, TRN), end='\r')
    driver.get('{}{}'.format(URL, ndx))
    sleep(cst.SLEEP)
    if MAP_ONLY:
        element = driver.find_element_by_id('gamemap-container')
    else:
        element = driver.find_element_by_id('gamecontainer')
    imgName = '{}_turn_{}.png'.format(prep, str(ndx).zfill(3))
    imgPath = path.join(OUT_PTH, imgName)
    element.screenshot(imgPath)
# Close driver ----------------------------------------------------------------
sleep(cst.SLEEP)
print('* Done ({}/{})'.format(ndx, TRN), end='\r')
driver.close()

# convert -delay 60 -resize 500x500 -loop 0 *.png animation.gif
# convert -delay 60 -resize 500x500 -loop 0 *.png animation.gif
# ffmpeg -f image2 -framerate 1 -i turn_%3d.png  out.gif