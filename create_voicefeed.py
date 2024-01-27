from dotenv import load_dotenv
import os
import openai
import feedparser
import json
import requests


load_dotenv()
openai.api_key = os.getenv("OPENAI__API_KEY")
elevenlab_api_key = os.getenv("ELEVENLABS_API_KEY")

kenyan_news = "www.k24tv.co.ke/category/news/feed/"

print("I am processing K24 RSS Feed")


feed = feedparser.parse(kenyan_news)

stories_today = ""
story_limit = 20

for item in feed.enteries[:story_limit]:
    stories_today = stories_today + "New Story: " + item.title + "." + item.description




print("I am now processing it on ChatGPT")


chatgpt_output = openai.ChatCompletion.create(
 model = "gpt-3.5-turbo",
 message = [{
	"role": "user",
	"content": "Rewrite the news headlines and summarize  them in a discussion context as if someone is reading the news in non-judgemental way and with no follow-on discussion , try  to include some final closing intonation:"  + stories_today
	}]
)

chat_content = chat_output.choices[0].message.content

print(chat_content)


print("I am Processing Audio")

voice_id = "lfFqxmNg1PYVjeQXy3hi"


















































