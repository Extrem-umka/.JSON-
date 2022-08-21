import json
from pprint import pprint
import collections

def read_json(newsafr, max_len_word=6, top_words=10):
    with open('newsafr.json', encoding='utf-8') as news_file:
        news = json.load(news_file)
        # pprint(news)
        description_words = []
        for item in news['rss']['channel']['items']:
            description = [word for word in item['description'].split(' ') if len(word) > max_len_word]
            description_words.extend(description)
            counter_words = collections.Counter(description_words)
        pprint(counter_words.most_common(top_words))


if __name__ == '__main__':
    read_json('newsafr.json')
