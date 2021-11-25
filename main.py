!pip install newspaper3k
import tkinter as tk
import nltk
from textblob import TextBlob
from newspaper import Article
nltk.download('punkt')

url = 'https://edition.cnn.com/2021/11/23/asia/taiwan-strait-us-warship-intl-hnk/index.html'

article = Article(url)

article.download()
article.parse()

article.nlp()

print(f'Title: {article.title}')
print(f'Authors: {article.authors}')
print(f'Publication Date: {article.publish_date}')
print(f'Summary: {article.summary}')

analysis = TextBlob(article.text)
print(analysis.polarity)
print(f'Sentiment: {"positive" if analysis.polarity > 0 else "negative" if analysis.polarity < 0 else "neutral"}')
