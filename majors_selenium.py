import typing
from requests import get
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")
driver = webdriver.Chrome(options=options, executable_path='chromedriver')

classes_url = "http://guide.berkeley.edu/undergraduate/degree-programs/"

def scrape_majors(name: str) -> None:
    """
    Given the name of a major, return a dictionary in the form:
    {requirement: [class1, class2], ...}
    """

    formatted_name = str.lower().replace(' ', '-')
    major_url = classes_url + formatted_name
    major_url = major_url + '/#majorrequirementstext'

    driver.get(major_url)

    print(driver.find_element_by_class_name('page-header'))


scrape_majors('Data Science')






