import requests
from prettytable import PrettyTable



# Import necessary packages
import PyPDF2
import re
from git import Repo


# Open The File in the Command
file = open("C:/Poorvi/VScode/Arithemania/link.pdf", 'rb')
readPDF = PyPDF2.PdfFileReader(file)


def find_url(string):
    # Find all the String that matches with the pattern
    regex = r"(https?://\S+)"
    url = re.findall(regex, string)
    for url in url:
        return url


# Iterating over all the pages of File
for page_no in range(readPDF.numPages):
    page = readPDF.getPage(page_no)
    # Extract the text from the page
    text = page.extractText()
    # Print all URL
print(find_url(text))

repo = Repo(find_url(text))

print(len(list(repo.iter_commits())))
# CLost the file
file.close()


table = PrettyTable()
table.field_names = ["Repository Name", "Created Date","Language", "Stars"]

query= "python"
#first page
page=1

#search for the top repositories
# api_url = f"https://api.github.com/search/repositories?q={query}&{page}"
api_url = f"https://api.github.com/stanfortonski/Tinder-Bot.git"

#send get request
response = requests.get(api_url)

#get the json data
data =  response.json()

for repository in data["items"]:
    name = repository["full_name"]
    created_date = repository["created_at"]
    language = repository["language"]
    stars = repository["stargazers_count"]
    
    table.add_row([name, created_date, language, stars ])

print(table)