import json
import requests
from collections import namedtuple,defaultdict
from operator import itemgetter

from settings import COOKIE,USERVID

requests.packages.urllib3.disable_warnings()

Book = namedtuple('Book',['bookId','title','author','cover','category'])


headers=\
"""
Host: i.weread.qq.com
Connection: keep-alive
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8
"""


headers = dict(x.split(': ',1) for x in headers.splitlines() if x)

headers.update(Cookie=COOKIE)
# print(headers)

def get_bookmarklist(bookId):
	"""获取某本书的笔记返回md文本"""
	url = "https://i.weread.qq.com/book/bookmarklist" 
	
	params = dict(bookId=bookId)

	try:
		r = requests.get(url,params=params,headers=headers,verify=False)
	except:
		raise

	if r.ok:
		data = r.json()
	else:
		raise Exception(r.text)



	#keys = ['synckey', 'totalCount', 'items', 'chapters']
	chapters = {c['chapterUid']:c['title'] for c in data['chapters']}
	contents = defaultdict(list)

	for item in data['updated']:
		chapter = item['chapterUid']
		text = item['markText']
		create_time = item["createTime"]
		contents[chapter].append(text)

	# print(contents)
	res = ''
	for c in chapters:
		title = chapters[c]
		res += '## '+title+'\n'
		for text in contents[c]:
			res += '### '+text.strip()+'\n'
		res += '\n'

	return res


def get_bestbookmarks(bookId):
	"""获取书籍的热门划线,返回文本"""

	url = "https://i.weread.qq.com/book/bestbookmarks" 
	params = dict(bookId=bookId)

	try:
		r = requests.get(url,params=params,headers=headers,verify=False)
	except:
		raise

	if r.ok:
		data = r.json()
	else:
		raise Exception(r.text)

	#keys = ['synckey', 'totalCount', 'items', 'chapters']
	chapters = {c['chapterUid']:c['title'] for c in data['chapters']}
	contents = defaultdict(list)
	for item in data['items']:
		chapter = item['chapterUid']
		text = item['markText']
		contents[chapter].append(text)

	res = ''
	for c in chapters:
		title = chapters[c]
		res += '## '+title+'\n'
		for text in contents[c]:
			res += '### '+text.strip()+'\n'
		res += '\n'

	return res


def get_chapters(bookId):
	"""获取书的目录"""
	url = "https://i.weread.qq.com/book/chapterInfos"
	data = '{"bookIds":["%d"],"synckeys":[0]}'% bookId
	# print(data)
	try:
		r = requests.post(url,data=data,headers=headers,verify=False)
	except:
		raise

	if r.ok:
		data = r.json()
		# print(r.json())
	else:
		raise Exception(r.text)

	chapters = []
	for item in data['data'][0]['updated']:
		chapters.append((item['level'],item['title']))

		if hasattr(item,'anchors'):
			for ac in item['anchors']:
				chapters.append((ac['level'],ac['title']))

	return chapters


def get_bookinfo(bookId):
	url = "https://i.weread.qq.com/book/info" 
	params = dict(bookId=bookId)

	try:
		r = requests.get(url,params=params,headers=headers,verify=False)
	except:
		raise

	if r.ok:
		data = r.json()
	else:
		raise Exception(r.text)

	return data

def get_bookshelf(userVid=USERVID):
	url = "https://i.weread.qq.com/shelf/friendCommon" 
	params = dict(userVid=userVid)

	try:
		r = requests.get(url,params=params,headers=headers,verify=False)
	except:
		raise

	if r.ok:
		data = r.json()
	else:
		raise Exception(r.text)
	from itertools import chain
	books = []
	for book in chain(data['finishReadBooks'],data['recentBooks']):
		# print(i,book['title'],book['author'],book['price'],book['category'])
		b = Book(book['bookId'],book['title'],book['author'],book['cover'],book['category'])
		books.append(b)
	books.sort(key=itemgetter(-1))
	return books

def get_notebooklist():
	"""获取笔记书单"""
	url = "https://i.weread.qq.com/user/notebooks"
	try:
		r = requests.get(url,headers=headers,verify=False)
	except:
		raise

	if r.ok:
		data = r.json()
	else:
		raise Exception(r.text)
	books = []
	i = 0
	for b in data['books']:
		book = b['book']
		i += 1
		# print(i,book['title'],book['author'],book['price'],book['category'])
		b = Book(book['bookId'],book['title'],book['author'],book['cover'],book['category'])
		books.append(b)
	books.sort(key=itemgetter(-1))
	return books



if __name__ == '__main__':
	main()
	print(get_bookmarklist(680309))
	books = get_booklist()
	for b in books:
		print(b)
	print(get_bookinfo(680309))
	for c in get_chapters(680309):
		print('#'*c[0],c[1])
	for b in get_bookshelf():
		print(b)
