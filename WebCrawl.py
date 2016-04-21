import webbrowser
import urllib

index = []
def addToIndex(index,keyword,url):
    for entry in index:
        if (entry[0] == keyword):
            entry[1].append(url)
            return
    index.append([keyword, [url]])

def addPageToIndex(index,url,content):
    words = content.split()
    for word in words:
        addToIndex(index, word, url)

def lookup(index,keyword):
    for entry in index:
        if (entry[0] == keyword):
            return entry[1]
    return []

def openMe(url):
    # Open URL in new window, raising the window if possible.
    webbrowser.open_new(url)

def getPage(url):
    try:
        # import urllib
        return urllib.urlopen(url).read()
    except:
        return ''

def getNextTarget(page):
    startLink = page.find('<a href=')
    if startLink == -1: 
        return None, 0
    startQuote = page.find('"', startLink)
    endQuote = page.find('"', startQuote + 1)
    url = page[startQuote + 1:endQuote]
    return url, endQuote

def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)

def getAllLinks(page):
    links = []
    while True:
        url,endpos = getNextTarget(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links

# def crawlWeb(seed,maxDepth):    
#     toCrawl = [seed]
#     crawled = []
#     nextDepth = []
#     depth = 0
#     while toCrawl and depth <= maxDepth:
#         page = toCrawl.pop()
#         if page not in crawled:
#             union(nextDepth, getAllLinks(getPage(page)))
#             crawled.append(page)
#         if not toCrawl:
#             toCrawl, nextDepth = nextDepth, []
#             depth = depth + 1
#     return crawled

def crawlWeb(seed):    
    toCrawl = [seed]
    crawled = []
    index = [] #different
    while toCrawl:
        page = toCrawl.pop()
        if page not in crawled:
            content = getPage(page) #different
            addPageToIndex(index, page, content) #different
            union(toCrawl, getAllLinks(getPage(page)))
            crawled.append(page)

    return index #different

# def printList(url,depth):
#     myList = crawlWeb(url,depth)
#     for item in myList:
#         print(item)

def printList(url):
    myList = crawlWeb(url)
    for item in myList:
        print(item)


# printList("http://www.udacity.com/cs101x/index.html",1)
# printList("http://www.udacity.com/cs101x/index.html")

# print(crawlWeb("http://www.udacity.com/cs101x/index.html",1))
#print(crawlWeb("http://www.udacity.com/cs101x/index.html"))

#print(getAllLinks(getPage("http://firstcoastymca.org/program/my-y-on-demand-staff-training-9/")))

# print getPage('http://www.yikyakapp.com/wp-content/themes/yik-yak-web-general/yaks.php')
# print(getPage("http://www.facebook.com"))
# print(getPage("http://firstcoastymca.org/"))

