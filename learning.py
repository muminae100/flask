from flask import Flask,render_template,jsonify,request
app = Flask(__name__)

books = [

    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}

]
@app.route('/')
def home_page():
        return render_template("test.html")

@app.route('/books/all')
def resource1():
    return jsonify(books)

@app.route('/books')
def check_id():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error!The book has not been found!"

    results = []

    for book in books:
        if book['id'] == id:
            results.append(book)

    return jsonify(results)


@app.errorhandler(404)
def error_message(e):
    return "<h1>Error! Book could not be found!</h1>", 404

if __name__ == '__main__':
    app.run(debug=True)