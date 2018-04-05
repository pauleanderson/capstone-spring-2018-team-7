import json

def generate_data (string):
    string = '{' +'\n' + '"text":"*Cayce heils you!* The update for today:", "attachments": [' + string[:-1]
    string = string + ']}'
    return string

def app_data (icon, title, country, rank, chart, developer, url):
    data = '{' +'\n' + '"title": "' + title + '", "text": "Highest Rank Country: ' + country + '\t Current Rank: ' + rank + '\t Chart: ' + chart + '\t Developer: ' + developer + '", "thumb_url": "' + url +  '"},'
    return data

datam = ''
for i in range (0,3):
    datam = datam+app_data('icon', 'Dragon Times', 'AU', '100', 'Free', 'crazy_developer', 'https://lh3.googleusercontent.com/lZhL5smuoS8EqylXKUgv5tN7V9jlSUT2txzyHYHcIBDwTLkKjDGmuEXDS5N6YB5Oag=w340')

#print(generate_data(datam))

def gen_app_data(icon, title, country, rank, chart, developer, url):
    return json.dumps({'title': title, 'text': 'Highest Rank Country: ' + country + '\t Current Rank: ' + rank + '\t Chart: ' + chart + '\n Developer: ' + developer, 'thumb_url': url}, separators=(',', ':'))

def gen_message (obj):
    return json.dumps({'text': "*Cayce heils you!* \n The update for today:", 'attachments': [obj]})


#with open('data.json', 'w') as outfile:
 #   json.dump(generate_data(app_data('icon', 'Dragon Times', 'AU', '100', 'Free', 'crazy_developer', 'url')), outfile)

file = open('data.json', 'w')
#file.write(generate_data(app_data('icon', 'Dragon Times', 'AU', '100', 'Free', 'crazy_developer', 'https://lh3.googleusercontent.com/lZhL5smuoS8EqylXKUgv5tN7V9jlSUT2txzyHYHcIBDwTLkKjDGmuEXDS5N6YB5Oag=w340')))
file.write(generate_data(datam))
file.close()
