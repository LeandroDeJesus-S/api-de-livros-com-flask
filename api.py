"""
/books/ (GET)    -> Consultar todos os livros
/books/id (GET)  -> consultar um livro em especifico
/books/id (POST) -> adicionar um novo livro
/books/id (PUT) -> adicionar um novo livro
/books/id (DELETE) -> deletar um livro
"""
import json
from flask import Flask, jsonify, request


app = Flask(__name__)

def load_books():
    with open('books.json', 'r', encoding='utf-8') as file:
        return json.load(file)

def dump_books(data):
    with open('books.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)


# getting all the books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(load_books())


# getting just one book
@app.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    for book in load_books():
        if book.get('id') == id:
            return jsonify(book)


# addicting a new book
@app.route('/books/add', methods=['POST'])
def add_book():
    new_book = request.get_json()
    _books = load_books()
    _books.append(new_book)
    dump_books(_books)
    return jsonify(load_books())


# editing a book
@app.route('/books/edit/<int:id>', methods=['PUT'])
def edit_book(id):
    altered_book = request.get_json()
    books = load_books()
    for index, book in enumerate(books):
        if book.get('id') == id:
            books[index].update(altered_book)
            dump_books(books)
            return jsonify(books[index])


# deleting a book
@app.route('/books/delete/<int:id>', methods=['DELETE'])
def delete_book(id):
    books = load_books()
    for index, book in enumerate(books):
        if book.get('id') == id:
            books.pop(index)
            dump_books(books)
            return jsonify(books)


if __name__ == '__main__':
    app.run('localhost', 5000, debug=True)
