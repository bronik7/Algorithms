import requests
from bs4 import BeautifulSoup
import random


class Scrapping:
    def __init__(self):
        self.data = []

    def get_url_data(self):

        for i in range(1, 20):
            url = requests.get(f"https://quotes.toscrape.com/page/{i}/")
            soup = BeautifulSoup(url.text, "html.parser")
            t = soup.find(class_="row").next_sibling.next_sibling.find(class_="col-md-8")
            if t.get_text().count("No quotes found!") > 0:
                break
            else:

                for div in soup.select(".quote"):
                    items = {}
                    text = div.find("span")
                    items["quote"] = text.get_text()
                    author = text.next_sibling.next_sibling.find(class_="author")
                    items["author"] = author.get_text()
                    items["url"] = div.find("a").attrs["href"]
                    self.data.append(items)

        user_input = True

        while user_input:
            count = 0
            selection = random.choice(self.data)
            print(selection["quote"])
            print(selection["author"])
            for i in range(4, 0, -1):

                user_input = input("Who said this quote: ")
                if user_input == selection["author"]:
                    answer = input("Correct answer, would you like to play again? y/n ")
                    if answer == "n":
                        user_input = False
                        break
                    else:
                        break

                else:
                    if count == 0:
                        url = requests.get(f"https://quotes.toscrape.com/{selection['url']}")
                        soup = BeautifulSoup(url.text, "html.parser")
                        
                        born = soup.body.find("h3").find(class_="author-born-date").get_text()
                        print(f"author was born {born}")
                    elif count == 1:
                        print(f"Auhtor's first name starts with {selection['author'][0]}")
                    elif count == 2:
                        print(f"Auhtor's first name starts with 3 letters {selection['author'][0:3]}")
                    else:
                        user_input = input("Sorry you lose!!!! \n Would you like to play again? y/n ")
                        if user_input == "n":
                            user_input = False

                count += 1


s = Scrapping()
s.get_url_data()
