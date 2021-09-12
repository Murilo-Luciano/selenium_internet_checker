from halo import Halo
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException
from termcolor import colored


spinner = Halo(text='Loading', spinner='dots')

options = Options()
options.add_argument('--headless')
driver = webdriver.Firefox(options=options)


def get_internet_value():
    spinner.start()
    driver.get('https://fast.com/')
    element_found = False
    while(element_found == False):
        try:
            velocity_value = driver.find_element_by_class_name(
                'speed-results-container.succeeded').text

            velocity_unit = driver.find_element_by_class_name(
                'speed-units-container.succeeded').text

            element_found = True
        except NoSuchElementException:
            element_found = False

    driver.close()
    spinner.stop()
    print(colored('Download speed', 'green') +
          ' ➤ ' + velocity_value + velocity_unit)


get_internet_value()
