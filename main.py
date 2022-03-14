from bs4 import BeautifulSoup
import requests

# # import lxml (if html parser doesn't work, put lxml inside "parser")
#
# with open("website.html", 'r') as file:
#     file_contents = file.read()
#
# soup = BeautifulSoup(file_contents, "html.parser")
# # print(soup.prettify())
#
# all_anchor_tags=soup.find_all(name="a")
# print(all_anchor_tags)
#
# # for tag in all_anchor_tags:
# #     # print(tag.getText())
# #     print(tag.get("href"))
#
# heading = soup.find(name="h1", id="name")
# print(heading)
#
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.getText())
#
# response = requests.get("https://news.ycombinator.com")
#
# yc_webpage = response.text
#
# soup = BeautifulSoup(yc_webpage, "html.parser")
# articles = soup.find_all(name='a', class_='titlelink')
# article_texts = []
# article_links = []
#
# for article_tag in articles:
#     text = article_tag.getText()
#     article_texts.append(text)
#     link = article_tag.get('href')
#     article_links.append(link)
#
# article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name='span', class_='score')]
#
# #
# print(article_texts)
# print(article_links)
# print(article_upvotes)
#
# max_nb = max(article_upvotes)
# index_nb = article_upvotes.index(max_nb)
# print(index_nb)
# print(article_texts[index_nb])
# print(article_links[index_nb])


response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")

titles = soup.find_all("img")

blacklist = ["Amazon", "Facebook", "Twitter", "Pinterest"]

new_list = ([str(title).split('"')[1] for title in titles if str(title).split('"')[1] not in blacklist])
new_list.pop(0)
new_list.reverse()

number_1 = 0
new_list2 = []

for item in new_list:
    number_1 += 1
    item = str(f'{number_1}. ') + item + '\n'
    new_list2.append(item)

str_new_list = ''.join(new_list2)


with open("movies.txt", 'w') as f:
    f.write(str_new_list)


