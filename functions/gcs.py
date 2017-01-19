from googleapiclient.discovery import build

gcsFile = 'googlecustomsearch.txt'
with open(gcsFile, 'r') as f:
    gcsKey = f.readline()


def makeCustomSearch(url, cx, msg, cutoff):
    content = str(msg.content)[cutoff:]
    service = build('customsearch', 'v1', developerKey=gcsKey)
    response = service.cse().list(q=str(content),
                                  num='1',
                                  siteSearch=url,
                                  cx=cx).execute()
    try:
        title = str(response['items'][0]['title'])
        link = str(response['items'][0]['link'])
        snippet = str(response['items'][0]['snippet'])
    except (NameError, KeyError):
        return 'There\'s nothing to be found.'
    snippet = snippet.replace('\n', '')
    return '**{0}**\n**Link: ** {1}\n**Snippet: ** {2}'.format(title, link, snippet)
