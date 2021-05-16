from flask import jsonify, request
from libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from forms.book import SearchForm
from viewmodels.book import BookViewModel
from . import web


@web.route('/book/search')
def search():
	form = SearchForm(request.args)
	if form.validate():
		q = form.q.data.strip()
		page = form.page.data
		isbn_or_key = is_isbn_or_key(q)
		if isbn_or_key == "isbn":
			result = YuShuBook.search_by_isbn(q)
			result = BookViewModel.package_single(result, q)
		else:
			result = YuShuBook.search_by_keyword(q)
			result = BookViewModel.package_collections(result, q)
		# return json.dumps(result), 200, {'application/json'}
		return jsonify(result)
	else:
		return jsonify(form.erros)
