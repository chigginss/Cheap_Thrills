""" Data from Eventbrite's API """

import requests
import unicodedata

# next month
# https://www.eventbriteapi.com/v3/events/search/?location.address=san+francisco&location.within=30mi&price=free&start_date.keyword=next_month&token=ZAKXWP2CDSBC2SS7RVYQ

# next week
# https://www.eventbriteapi.com/v3/events/search/?location.address=san+francisco&location.within=30mi&price=free&start_date.keyword=next_week&token=ZAKXWP2CDSBC2SS7RVYQ

#api key hidden
# url = "https://www.eventbriteapi.com/v3/events/search/?location.address=san+francisco&location.within=30mi&price=free&start_date.keyword=next_month&token={mytoken}".format(mytoken=mytoken)

data = requests.get("https://www.eventbriteapi.com/v3/events/search/?location.address=san+francisco&location.within=30mi&price=free&start_date.keyword=next_week&token=ZAKXWP2CDSBC2SS7RVYQ")

all_events = data.json()

week_events = all_events['events']

content = []

for i in range(len(week_events)):
        title = (week_events[i].get('name')['text'] or " ").encode('utf-8')
        about = (week_events[i].get('description')['text'] or " ").encode('utf-8')
        url = (week_events[i].get('url') or " ").encode('utf-8')
        time = (week_events[i].get('start')['local'] or " ").encode('utf-8')
        event = "title: {} description: {} url: {} time: {}".format(title, about, url, time)
        event = unicode(event, 'utf-8')
        content.append(event)

# print title + "\n", "description: " + about + "\n", "url: " + url + "\n", "time: " + time

# content = unicode(content)
# final_events = content.normalize("NFKD", u'\xa0')

content = str(content)
content = content.split("\\xa0")

# for item in content:
#     if '\\xa0' == item:
#         item.replace('\\xa0', ' ')
#     elif '\\n' == item:
#         item.replace('\\n', ' ')
#     elif '\\n' == item:
#         item.replace('\n', ' ')
#     elif '\\n' == item:
#         item.replace('\xa0', ' ')

print " ".join(content)