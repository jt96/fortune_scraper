import bs4, requests, random


page_count = 0

# makes HTTP request to fortune site and parses the html
res = requests.get('http://www.fortunecookiemessage.com/archive.php?start=' + str(page_count))
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')

# fortunes on this site were links
# selects based on "a" tag
elems = soup.select('td > a')

# new list to store fortune strings in correct format
fortunes = []

# pulls from every page to grab all the fortunes
while len(elems) != 0:
    # converts bs4.element.tag to string, extracts the fortune sentence from the elem and adds to fortune list
    for elem in map(str, elems):
        if elem not in fortunes:
            fortunes.append(elem[elem.index('>') + 1:elem[1:].index('<') + 1])
        else:
            print('fortune already exists')
    page_count += 50
    res = requests.get('http://www.fortunecookiemessage.com/archive.php?start=' + str(page_count))
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('td > a')

# prints random fortune from list
print(random.choice(fortunes))