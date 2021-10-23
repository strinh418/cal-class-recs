import requests
import lxml
from bs4 import BeautifulSoup
import re


def processRating(rating):
	# get quality and difficulty
	quality, difficulty = rating.find_all(class_ = re.compile("CardNumRatingNumber"))
	quality,difficulty = quality.get_text(), difficulty.get_text()
	className = rating.find(class_ = re.compile("RatingHeader__StyledClass")).get_text()
	metaItems = rating.find_all(class_ = re.compile("StyledMetaItem"))
	grade = "null"
	takeAgain = "null"
	for item in metaItems:
		if "Grade" in item.get_text():
			grade = item.get_text()[7:]
		if "Would Take Again" in item.get_text():
			takeAgain = item.get_text()[18:]
	comment = rating.find(class_ = re.compile("StyledComments")).get_text()
	tagsHtml = rating.find_all("span", class_ = re.compile("Tag"))
	tags = []
	for tag in tagsHtml:
		tags.append(tag.get_text())

	print(quality, difficulty, className, grade, takeAgain, comment, tags)
	print("---------")

def fetchProfessor(id):
	url = "https://www.ratemyprofessors.com/ShowRatings.jsp?tid={id}".format(id=id)

	headers = {
	  'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
	}
	f = requests.get(url)

	soup = BeautifulSoup(f.content,'html.parser')

	ratings = soup.find_all(class_=re.compile("Rating__RatingBody"))
	data = []
	for rating in ratings:
		data.append(processRating(rating))
	# print(data)
	
# fetchProfessor(525740) #satish rao
fetchProfessor(1621181) #Denero