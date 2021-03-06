book = {
	"rating": {
		"max": 10,
		"numRaters": 309,
		"average": "7.0",
		"min": 0
	},
	"subtitle": "",
	"author": [
		"[日] 片山恭一"
	],
	"pubdate": "2005-1",
	"tags": [
		{
			"count": 118,
			"name": "片山恭一",
			"title": "片山恭一"
		},
		{
			"count": 56,
			"name": "日本",
			"title": "日本"
		},
		{
			"count": 49,
			"name": "日本文学",
			"title": "日本文学"
		},
		{
			"count": 32,
			"name": "小说",
			"title": "小说"
		},
		{
			"count": 31,
			"name": "满月之夜白鲸现",
			"title": "满月之夜白鲸现"
		},
		{
			"count": 11,
			"name": "爱情",
			"title": "爱情"
		},
		{
			"count": 7,
			"name": "純愛",
			"title": "純愛"
		},
		{
			"count": 7,
			"name": "外国文学",
			"title": "外国文学"
		}
	],
	"origin_title": "",
	"image": "http://img3.douban.com/mpic/s1747553.jpg",
	"binding": "平装",
	"translator": [
		"豫人"
	],
	"catalog": "\n ",
	"pages": "180",
	"images": {
		"small": "http://img3.douban.com/spic/s1747553.jpg",
		"large": "http://img3.douban.com/lpic/s1747553.jpg",
		"medium": "http://img3.douban.com/mpic/s1747553.jpg"
	},
	"alt": "http://book.douban.com/subject/1220562/",
	"id": "1220562",
	"publisher": "青岛出版社",
	"isbn10": "7543632608",
	"isbn13": "9787543632608",
	"title": "满月之夜白鲸现",
	"url": "http://api.douban.com/v2/book/1220562",
	"alt_title": "",
	"author_intro": "",
	"summary": "那一年，是听莫扎特、钓鲈鱼和家庭破裂的一年。说到家庭破裂，母亲怪自己当初没有找到好男人，父亲则认为当时是被狐狸精迷住了眼，失常的是母亲，但出问题的是父亲……。",
	"price": "15.00元"
}


class YuShuBook():
	isbn_url = "http://t.yushu.im/v2/book/isbn/{}"
	keyword_url = "http://t.yushu.im/v2/book/search?q={}&count={}start={}"

	@classmethod
	def search_by_isbn(cls, isbn):
		# url = cls.isbn_url.format(isbn)
		# result = Http.get(url)
		# return result
		return book

	@classmethod
	def search_by_keyword(cls, keyword, count=15, start=0):
		# url = cls.keyword_url.format(keyword, count, start)
		# result = Http.get(url)
		# return result
		return book


