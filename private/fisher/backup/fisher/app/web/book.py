from flask import jsonify, request
from app.forms.book import SearchForm
from app.celery_task.task_one import add
from . import web


@web.route('/book/search')
def search():
	# form = SearchForm(request.args)
	# if form.validate():
	# number = add.delay(2, 4)
	result = {
		# "number": number.get(),
		"subtitle": "",
		"author": ["[日] 片山恭一"],
		"pubdate": "2005-1",
		"tags": [
			{
				"count": 31,
				"name": "满月之夜白鲸现",
				"title": "满月之夜白鲸现"
			}
		],
	}
	return jsonify(result)
	# else:
	# 	return jsonify({"error": "123"})
