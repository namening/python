from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser=webdriver.Firefox()
browser.get('https://gabrielecirulli.github.io/2048/')
htmlElem=browser.find_element_by_tag_name('html')

DOWN=htmlElem.send_keys(Keys.DOWN)
UP=htmlElem.send_keys(Keys.UP)
LEFT=htmlElem.send_keys(Keys.LEFT)
RIGHT=htmlElem.send_keys(Keys.RIGHT)

for i in range(200):
    htmlElem.send_keys(Keys.DOWN)
    htmlElem.send_keys(Keys.UP)
    htmlElem.send_keys(Keys.LEFT)
    htmlElem.send_keys(Keys.RIGHT)
