import sys
from googleapiclient.discovery import build

cx = '002728055490769483510:ekrupke_ugg'
key = sys.argv[2]


def make_custom_search(url, content, include_snippet):
    service = build('customsearch', 'v1', developerKey=key)
    if url != '':
        response = service.cse().list(q=str(content), num='1', siteSearch=url, cx=cx).execute()
    else:
        response = service.cse().list(q=str(content), num='1', cx=cx).execute()
    try:
        title = str(response['items'][0]['title'])
        link = str(response['items'][0]['link'])
        snippet = str(response['items'][0]['snippet'])
        snippet = snippet.replace('\n', '')
    except KeyError:
        return 'There\'s nothing to be found.'
    if include_snippet:
        return '**{0}**\n**Link: ** {1}\n**Snippet: ** {2}'.format(title, link, snippet)
    else:
        return '**{0}**\n**Link: ** {1}'.format(title, link)


def nethys(msg):
    return make_custom_search('archivesofnethys.com', msg.content[len('/nethys '):], True)


def pfsrd(msg):
    return make_custom_search('d20pfsrd.com', msg.content[len('/pfsrd '):], True)


def google(msg):
    return make_custom_search('', msg.content[len('/google '):], False)


def g(msg):
    return make_custom_search('', msg.content[len('/g '):], False)


def youtube(msg):
    return make_custom_search('youtube.com', msg.content[len('/youtube '):], False)


def yt(msg):
    return make_custom_search('youtube.com', msg.content[len('/yt '):], False)
