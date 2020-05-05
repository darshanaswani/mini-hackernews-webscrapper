import requests
from bs4 import BeautifulSoup
import pprint

response = requests.get('https://news.ycombinator.com/news')

soup_object = BeautifulSoup(response.text, 'html.parser')

story_links = soup_object.select('.storylink')
subtext = soup_object.select('.subtext')


def sort_stories_by_votes(hnlist):
    '''
    this function sorts the news based on highest votes
    '''
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


def create_custom_hn(links, votes):
    '''
    this function filter out the news  having votes greater than 99 and returns
    object containing link to the news,title,and votes
    '''
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace('points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)


pprint.pprint(create_custom_hn(story_links, subtext))
