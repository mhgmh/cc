import requests
from Pub_articles import articles


headers = {
    'authority': 'm.toutiao.com',
    'method': 'GET',
    'scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cookie': 'UM_distinctid=16352d801092ac-0eb0a388034e86-33657f07-1fa400-16352d8010afee; tt_webid=6554563661830604302; uuid="w:a904362acac346dbb2b84c78fd6a868f"; sso_login_status=0; _ga=GA1.2.1416607795.1526551943; __utma=24953151.1416607795.1526551943.1526553949.1526553949.1; __utmz=24953151.1526553949.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _gid=GA1.2.1927624416.1526711605; __tasessionId=ocugf0p0c1526714508060',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Mobile Safari/537.36',
}


url = 'https://m.toutiao.com/group/6556835381898117635/'
html = requests.get(url, headers=headers, allow_redirects=False)
print(html.headers['location'])