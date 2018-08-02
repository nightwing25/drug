from requests import get
from bs4 import BeautifulSoup
import urllib.request
import random 


#"https://abovetheinfluence.com/drugs/"
list_text = []
drug_names = []

def drug(drugname):
	url = "https://abovetheinfluence.com/drugs/"
	base = url+drugname+"/"
	req = get(base).content
	grab = BeautifulSoup(req,"html.parser")
	for grab_page in grab.findAll('p'):
		list_text.append(grab_page.text)
	print(list_text)

def save_facts(drugname):
	url = "https://abovetheinfluence.com/drugs/"
	base = url+drugname+"/"
	req = get(base).content
	grab = BeautifulSoup(req,"html.parser")
	for grab_page in grab.findAll('p'):
		list_text.append(grab_page.text)
	with open("drugs.txt",'a') as high:
		high.write(str(list_text))
		print('file has been saved')


#the imaging may or may not work
def grab_image(drugy):
	name = random.randrange(1,1000)
	name2 = "drugs"+str(name)+".jpg"
	urllib.request.urlretrieve(drugy,name2)
	

def list_drugs(letter):
	url = "https://druginfo.nlm.nih.gov/drugportal/drug/names/"+letter
	lists = get(url).content
	weed = BeautifulSoup(lists,"html.parser")
	pass

