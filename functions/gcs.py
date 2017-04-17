import sys
from googleapiclient.discovery import build

pfsrd_cx = '006680642033474972217:6zo0hx_wle8'
nethys_cx = '012046020158994114137:raqss6g6jvy'
key = sys.argv[2]


def makeCustomSearch(url, cx, content):
    service = build('customsearch', 'v1', developerKey=key)
    response = service.cse().list(q=str(content), num='1', siteSearch=url, cx=cx).execute()
    try:
        title = str(response['items'][0]['title'])
        link = str(response['items'][0]['link'])
        snippet = str(response['items'][0]['snippet'])
        snippet = snippet.replace('\n', '')
    except KeyError:
        return 'There\'s nothing to be found.'
    return '**{0}**\n**Link: ** {1}\n**Snippet: ** {2}'.format(title, link, snippet)


def nethys(msg):
    return makeCustomSearch('archivesofnethys.com', nethys_cx, msg.content[len('/nethys '):])


def pfsrd(msg):
    return makeCustomSearch('d20pfsrd.com', pfsrd_cx, msg.content[len('/pfsrd '):])
