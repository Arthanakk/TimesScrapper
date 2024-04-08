from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def get_time_stories():
    url = "https://time.com"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    stories = []

    latest_stories_container = soup.find('div',class_= 'latest-stories')
    if latest_stories_container:
        articles = latest_stories_container.find_all('li', class_='latest-stories__item')
        for article in articles:
            link = article.find('a')['href']
            title = article.find('a').text.strip()
            stories.append({"title": title, "link": link})
    return stories
@app.route('/getTimeStories', methods = ['GET'])
def get_time_stories_api():
    stories = get_time_stories()
    return jsonify(stories)
if __name__ == '__main__':
    app.run(debug=True)