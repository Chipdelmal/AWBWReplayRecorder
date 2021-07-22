
import os
from sys import argv
from time import sleep
from os import path
from PIL import Image
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import constants as cst
import functions as fun

if fun.isnotebook():
    (ID, NAME, OUT_PTH) = (
        '357091', '04_Booyah-Chip_Yami_Richie', 
        '/home/chipdelmal/Documents/AWBW/'
    )
    (TRN, ZOM) = (57, 8)
else:
    (ID, NAME, TRN, ZOM, OUT_PTH) = (
        argv[1], argv[2], int(argv[3]), int(argv[4]), argv[5]
    )
###############################################################################
# Create folders and load driver
###############################################################################
URL = cst.BASE_URL.format(ID)
OUT_PTH = path.join(OUT_PTH, NAME)
if not path.exists(OUT_PTH):
    os.makedirs(OUT_PTH)
# Load driver and mainpage ----------------------------------------------------
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
if cst.MAP_ONLY:
    prep = 'M'
###############################################################################
# Iterate through turns (frames)
###############################################################################
for ndx in range(0, TRN+1):
    print('* Scraping ({}/{})'.format(ndx+1, TRN), end='\r')
    driver.get('{}{}'.format(URL, ndx))
    sleep(cst.SLEEP)
    if cst.MAP_ONLY:
        element = driver.find_element_by_id('gamemap-container')
    else:
        element = driver.find_element_by_id('gamecontainer')
    imgName = '{}_turn_{}.png'.format(prep, str(ndx).zfill(3))
    imgPath = path.join(OUT_PTH, imgName)
    element.screenshot(imgPath)
###############################################################################
# Close driver
###############################################################################
sleep(cst.SLEEP)
print('* Done ({}/{})'.format(ndx, TRN), end='\r')
driver.close()
