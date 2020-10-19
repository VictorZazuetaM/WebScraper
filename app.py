import requests
from bs4 import BeautifulSoup

PAGINATION_COUNT = 1000

def get_soup(page_number):
    response = requests.get("https://stackoverflow.com/questions?tab=newest&page=" + str(page_number))
    return BeautifulSoup(response.text, "html.parser")


with open("questions.txt", "w") as file:
    for i in range(0, PAGINATION_COUNT):
        soup = get_soup(i)
        questions = soup.select(".question-summary")
        file.write(f"Page {i}\n-------------------------------------------------------------\n")
        for j in range(len(questions)):
            question_text = questions[j].select_one(".question-hyperlink").getText()
            question_votes = questions[j].select_one(".vote-count-post").getText()
            file.write(f"{j + 1} - {question_text}: {question_votes}\n")

        file.write("\n")
