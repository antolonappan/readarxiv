from bs4 import BeautifulSoup as bs
import urllib.request
import os


page = urllib.request.urlopen('https://arxiv.org/list/astro-ph.CO/recent')
soup = bs(page)
content = soup.body.find("div", {'id': 'content'})

issue_title = content.find("h3").text
dt_list = content.dl.find_all("dt")
dd_list = content.dl.find_all("dd")

no_of_papers = len(dt_list)

with open('.arxiv.txt', 'w') as writer:
    writer.write(f"Hello Anto, today there are {no_of_papers} papers\n")
    writer.write("The first one is\n")
    for i in range(no_of_papers):
        title = dd_list[i].find("div", {"class": "list-title mathjax"}).text.replace("Title: ", "").strip()
        writer.write(f"{title}\n")
        if i ==  no_of_papers-2:
            writer.write("\n")
            writer.write("\n")
            writer.write("The Last one is\n")
            writer.write("\n")
            writer.write("\n")
            writer.write("\n")
            writer.write("\n")
        elif i == no_of_papers-1:
            writer.write("\n")
            writer.write("\n")
            writer.write("Finished\n")
        else:
            writer.write("\n")
            writer.write("\n")
            writer.write("The next one is\n")
            writer.write("\n")
            writer.write("\n")
            writer.write("\n")
            writer.write("\n")


