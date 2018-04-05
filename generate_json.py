import json

def generate_data (string):
    string = '{' +'\n' + '"text":"*Cayce heils you!* The update for today:", "attachments": [' + string[:-1]
    string = string + ']}'
    return string

def app_data (icon, title, country, rank, chart, developer, url):
    data = '{' +'\n' + '"title": "' + title + '", "text": "Highest Rank Country: ' + country + '\t Current Rank: ' + rank + '\t Chart: ' + chart + '\t Developer: ' + developer + '", "thumb_url": "' + url +  '"},'
    return data

#TODO once the input to python is decided, we will need a function that will loop through apps like code below:
datam = ''
for i in range (0,3):
    datam = datam+app_data('icon', 'Dragon Times', 'AU', '100', 'Free', 'crazy_developer', 'https://lh3.googleusercontent.com/lZhL5smuoS8EqylXKUgv5tN7V9jlSUT2txzyHYHcIBDwTLkKjDGmuEXDS5N6YB5Oag=w340')

file = open('data2.json', 'w')
#file.write(generate_data(app_data('icon', 'Dragon Times', 'AU', '100', 'Free', 'crazy_developer', 'https://lh3.googleusercontent.com/lZhL5smuoS8EqylXKUgv5tN7V9jlSUT2txzyHYHcIBDwTLkKjDGmuEXDS5N6YB5Oag=w340')))
file.write(generate_data(datam))
file.close()
