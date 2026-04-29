from flask import Flask, jsonify, request

books = [
    {'id': 1, 'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald'},
    {'id': 2, 'title': 'To Kill a Mockingbird', 'author': 'Harper Lee'}
]

app = Flask(__name__)

@app.route('/')
def home():
    return 'Nasa kniznica'

@app.route(rule='/knihy', methods=['GET'])
def get_books():
    return jsonify({'books': books})

@app.route(rule='/knihy', methods=['POST'])
def add_book():
    print(request.json)
    new_book = {
        'id': books[-1]['id'] + 1,
        'title': request.json['title'],
        'author': request.json['author']
    }
    books.append(new_book)
    return jsonify(new_book), 201

@app.route("/knihy/<int:book_id>", methods=['GET'])
def get_one(book_id):
    for b in books:
        if b["id"] == book_id:
            return jsonify(b), 200
    return f"chyba: kniha nenajdena", 404

@app.route("/knihy/<int:book_id>", methods=['PUT'])
def update_book(book_id):
    for b in books:
        if b["id"] == book_id:
            b["title"] = request.json["title"]
            b["author"] = request.json["author"]
            return jsonify(b), 200
    return f"chyba: kniha nenajdena", 404

@app.route("/knihy/<int:book_id>", methods=['DELETE'])
def delete(book_id):
    for b in books:
        if b["id"] == book_id:
            books.remove(b)
            return f"kniha s ID {book_id} vymazana", 200
    return f"chyba: kniha s ID {book_id} sa nenasla", 404

if __name__ == '__main__':
    app.run()
