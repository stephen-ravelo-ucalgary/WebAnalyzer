import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/University_of_Calgary"

try:
    response = requests.get(url)
    response.raise_for_status() # Ensures the request was successful
    soup = BeautifulSoup(response.text, 'html.parser')
    print(f"Successfully fetched content from {url}")
except Exception as e:
    print(f"Error fetching content: {e}")

print()
headings = 0
for i in range(1,7):
    headings += len(soup.find_all(f"h{i}"))
links = len(soup.find_all("a"))
paragraphs = len(soup.find_all("p"))
    
print(f"Number of headings: {headings}")
print(f"Number of links: {links}")
print(f"Number of paragraphs: {paragraphs}")

soup_text = soup.get_text()
keyword = input("Please enter a keyword: ")
keyword_appearances = 0
for word in soup_text.split():
    if (word == keyword):
        keyword_appearances += 1
print(f"\"{keyword}\" appears: {keyword_appearances} times")

print()
words = soup_text.split()
for i in range(len(words)):
    words[i] = words[i].lower()
unique_words = {}
for word in words:
    if (word not in unique_words):
        unique_words[word] = 1
    else:
        unique_words[word] += 1

print()
top_5 = {}
unique_words_copy = unique_words
for i in range(5):
    cur_max = 0
    cur_max_word = ''
    for key, value in unique_words_copy.items():
        if (value > cur_max):
            cur_max = value
            cur_max_word = key
    top_5[cur_max_word] = cur_max
    unique_words_copy.pop(cur_max_word)
place = 1
for key, value in top_5.items():
    print(f"{place}. \"{key}\" appeared {value} times")
    place += 1

print()
longest_paragraph = ''
for para in soup.find_all("p"): 
    if (len(para.get_text().split()) < 5):
        continue
    if (len(para.get_text()) > len(longest_paragraph)):
        longest_paragraph = para.get_text()
print(longest_paragraph)

import matplotlib.pyplot as plt
labels = ['Headings', 'Links', 'Paragraphs']
values = [headings, links, paragraphs]
plt.bar(labels, values)
plt.title('Group #1')
plt.ylabel('Count')
plt.show()