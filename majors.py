import typing
from requests import get
from bs4 import BeautifulSoup
from pprint import pprint


classes_url = "http://guide.berkeley.edu/undergraduate/degree-programs/"
major_div = "majorrequirementstextcontainer"

def scrape_majors(name: str) -> None:
    """
    Given the name of a major, return a dictionary in the form:
    {requirement: [class1, class2], ...}
    """

    formatted_name = str.lower(name).replace(' ', '-')
    major_url = classes_url + formatted_name
    major_url = major_url + '/#majorrequirementstext'

    req = get(major_url)
    soup = BeautifulSoup(req.content, 'html.parser')
    soup = soup.find('div', id=major_div)

    d = {}

    for t in soup.find_all('table', 'sc_courselist'):
        title = t.find_previous('h3')
        title_strong = t.find_previous('strong')
        if title.find_next('strong') == title_strong:
            title = title_strong
        title = title.text.replace('\xa0', ' ').strip()

        courses = []
        for td in t.find_all('td', 'codecol'):
            course = td.text.replace('\xa0', ' ').replace('or ', '')
            courses.append(course)

        d[title] = courses

    pprint(d)
    return d
    

scrape_majors('History')






