from selenium import *
import selenium.webdriver
from selenium.webdriver.common.by import *
from requests import get
import cv2
import numpy as np

driver = selenium.webdriver.Chrome()

driver.get("https://www.reddit.com/r/dogpictures")
image_elements = driver.find_elements(By.CLASS_NAME, "ImageBox-image")
for image_element in image_elements[0:1]:
    img_src = image_element.get_attribute("src")
    get_response_content = get(img_src).content
    image_bytes = np.asarray(bytearray(get_response_content))
    image_decoded = cv2.imdecode(image_bytes, flags=cv2.IMREAD_COLOR)
    cv2.imshow('win', image_decoded/256)
    cv2.waitKey(0)
