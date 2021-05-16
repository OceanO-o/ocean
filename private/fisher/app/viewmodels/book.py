

class BookViewModel():

	@classmethod
	def package_single(cls, data, keyword):
		result = {
			'book': [],
			'total': 0,
			'keyword': keyword
		}
		if data:
			result['total'] = 1
			result['book'] = [cls.__cut_book_data(data)]
		return result

	@classmethod
	def package_collections(cls, keyword):
		pass

	@classmethod
	def __cut_book_data(cls, data):
		book = {
			'title': data['title'],
			'summary': data['summary'],
			'image': data['image'],
			'price': data['price'],
			'author': ''.join(data['author']),
			'pages': data['pages'],
			'publisher': data['publisher']
		}
		return book

