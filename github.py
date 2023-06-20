#search_github_repositories.py
import requests
from pprint import pprint
import re
import PyPDF2
from git import Repo
from github import *
import base64

# github username
username = "poorvisuparn"
# url to request
url = f"https://api.github.com/users/{username}"
# make the request and return the json
user_data = requests.get(url).json()
# pretty print JSON data
# pprint(user_data)
# Open The File in the Command
file = open("link.pdf", 'rb')
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
# print(find_url(text))

repo = Repo('C:/Users/poorv/Documents/GitHub/Tinder-Bot')


def print_repo(repo):
    # repository full name
    print("Full name:", repo.full_name)
    # repository description
    print("Description:", repo.description)
    # the date of when the repo was created
    print("Date created:", repo.created_at)
    # the date of the last git push
    print("Date of last push:", repo.pushed_at)
    # home website (if available)
    print("Home Page:", repo.homepage)
    # programming language
    print("Language:", repo.language)
    # number of forks
    print("Number of forks:", repo.forks)
    # number of stars
    print("Number of stars:", repo.stargazers_count)
    print("-"*50)
    print(len(list(repo.iter_commits())))
    # repository content (files & directories)
    print("Contents:")
    for content in repo.get_contents(""):
        print(content)
    try:
        # repo license
        print("License:", base64.b64decode(repo.get_license().content.encode()).decode())
    except:
        pass

print_repo(repo)