# Import required libraries
import PyPDF2
import textract
import re
import string
import pandas as pd
import matplotlib.pyplot as plt
# import git
# %matplotlib inline

# Open pdf file
pdfFileObj = open("D:/Downloads/resumes/timothy_tithpecker_resume.pdf", 'rb')

# Read file
pdfReader = PyPDF2.PdfFileReader(pdfFileObj, strict=False)

# Get total number of pages
num_pages = pdfReader.numPages

# Initialize a count for the number of pages
count = 0

# Initialize a text empty etring variable
text = ""

""" # Extract text from every page on the file
while count < num_pages:
    pageObj = pdfReader.getPage(count)
    count += 1
    text += pageObj.extractText() """


# Convert all strings to lowercase
text = text.lower()

# Remove numbers
text = re.sub(r'\d+', '', text)

# Remove punctuation
text = text.translate(str.maketrans('', '', string.punctuation))
# text = text.translate(str.maketrans(''-'', string.punctuation))


terms = {'skills': ['python', 'c', 'jupyter', 'project', 'c#', 'c++', 'java', 'javascript', 'go', 'linux', 'development', ''],

        'qualifications': {'beginner': ['ba', 'bs', 'btech', 'bachelor', 'undergraduate'], 'intermediate': ['masters', 'ma', 'ms', 'postgraduate'],

        'advanced':['phd', 'da', 'ds', 'edd', 'dba', 'docorate']},

        'projects': ['python', 'c', 'jupyter', 'project', 'c#', 'c++', 'java', 'javascript', 'go', 'linux'],

         'education': ['course', 'certified', 'intermediate', 'distinction', 'first class'],

         'workexperience': ['manager', 'published', 'employee', 'developed', 'devised', 'built', 'created', 'coordinated', 'assisted', 'maintained'],

         'years worked': ['zero', 'one year', 'two years', 'three years', 'four years', 'five years', 'six years', 'seven years', 'eight years', 'nine years', 'ten years', 'eleven years', 'twelve years', 'thirteen years', 'fourteen years', 'fifteen years', 'sixteen years', 'seventeen years', 'eighteen years', 'nineteen years', 'twenty years', 'twenty one years', 'twenty two years', 'twenty three', 'twenty four', 'twenty five'],
         
         'management': ['coached', 'led', 'guided', 'mentored', 'directed', 'shaped', 'supervised', 'administration', 'oversaw'
         'agile', 'budget', 'cost', 'direction', 'feasibility analysis', 'finance', 'leader', 'leadership', 'management', 'milestones', 'planning']}

# 'bachelor', 'diploma','masters','technology','engineering','phd','undergraduate','postgraduate','BS','BA','MA','MS'

# Initialize score counters for each area
skills= 0
qualifications= 0
education= 0
experience= 0
projects= 0
management= 0
workexperience= 0 


# Create an empty list where the scores will be stored
scores= []
# regex= r"(https?://\S+)"
# Obtain the scores for each area
for area in terms.keys():

    if area == 'skills':
        for word in terms[area]:
            if word in text:
                skills += 1
        scores.append(skills)
        

    elif area == 'qualifications':
        for word in terms[area]['beginner']:
            if word in text:
                qualifications += 1
        for word in terms[area]['intermediate']:
            if word in text:
                qualifications += 2
        for word in terms[area]['advanced']:
            if word in text:
                qualifications += 3
        scores.append(qualifications)

    elif area == 'work experience':
        for word in terms[area]:
            if word in text:
                experience += 1
        scores.append(experience)

    elif area == 'years worked':
            for word in terms[area]:
                if word in text:
                    experience += 1

    else:
        for word in terms[area]:
            if word in text:
                management += 1
        scores.append(management)

    

    # elif area == regex:
    #     for word in terms[area]:
    #         if



print(scores)

# # Create a data frame with the scores summary
# summary= pd.DataFrame(scores, index=terms.keys(), columns=['score']).sort_values(by='score', ascending=False)
# # summary
# print(summary)

# # Create pie chart visualization
# pie= plt.figure(figsize=(20, 20))
# plt.pie(summary['score'], labels=summary.index, explode=(
#     0, 1, 0, 0, 0, 0, 0), autopct='%1.0f%%', shadow=True, startangle=90)
# plt.title('Industrial Engineering Candidate - Resume Decomposition by Areas')
# plt.axis('equal')
# plt.show()

# pie.savefig('resume_screening_results.png')
