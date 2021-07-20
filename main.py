# importing webdriver from selenium
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver

# selecting browser
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path='/Library/Frameworks/Python.framework/Versions/3.9/bin/chromedriver')

# URL of the website
url = "https://www.javatpoint.com/python-tutorial"

# opening link in the browser
driver.get(url)
delay = 3  # seconds
try:
    myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="menu"]')))
    print("Page is ready!")
except TimeoutException:
    print("Loading took too much time!")

# Contains menu web element
containers = driver.find_element_by_xpath('//*[@id="menu"]')
# List all webelements under div menu

submenu = containers.find_elements_by_tag_name('div')

headKey = containers.find_elements_by_xpath('//*[@id="menu"]/a')
result = {}


if len(headKey) == 0:
    for i in range(len(submenu)):
        if submenu[i].get_attribute('class') == 'leftmenu':
            continue
        else:
            if submenu[i].get_attribute('class') == 'leftmenu2' and submenu[i + 1].get_attribute('class') == 'leftmenu':
                subsubmenu = submenu[i+1].find_elements_by_tag_name('a')
                list = []
                for item in subsubmenu:
                    list.append(item.text)

                result.update({submenu[i].text: list})
            else:
                subsubmenu = submenu[i].find_elements_by_tag_name('a')
                for item in subsubmenu:
                    result.update({item.text: []})
else:
    result[headKey[0].text] = {}
    for i in range(len(submenu)):
        if submenu[i].get_attribute('class') == 'leftmenu':
            continue
        else:
            if submenu[i].get_attribute('class') == 'leftmenu2' and submenu[i + 1].get_attribute('class') == 'leftmenu':
                subsubmenu = submenu[i+1].find_elements_by_tag_name('a')
                list = []
                for item in subsubmenu:
                    list.append(item.text)

                result[headKey[0].text].update({submenu[i].text: list})
            else:
                subsubmenu = submenu[i].find_elements_by_tag_name('a')
                for item in subsubmenu:
                    result[headKey[0].text].update({item.text: []})

print(result)
