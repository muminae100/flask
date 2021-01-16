from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

# POST, PUT, DELETE (methods)
@app.route('/books', methods=['GET'])
def books():
    name = 'mumiona '
    age = '15'
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

    return jsonify(books)

@app.route('/books/a', methods=['GET'])
def books_starting_a():
    name = 'mumiona '
    age = '15'
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
    books_starting_with_a = []
    for book in books:
        if book['title'].startswith('A'):
            books_starting_with_a.append(book)

    return jsonify(books_starting_with_a)

if __name__ == '__main__':
    app.debug = True
    app.run()
