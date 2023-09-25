from flask import Flask, jsonify, request, render_template
import json

app = Flask(__name__)

# Define the path to the JSON file to store book data
json_file_path = 'books.json'

# Initialize the books list from the JSON file
try:
    with open(json_file_path, 'r') as json_file:
        books = json.load(json_file)
except FileNotFoundError:
    books = []


@app.route('/', methods=['GET'])
def index():
    return render_template('menu.html', books=books)


@app.route('/books', methods=['GET'])
def get_books():
    try:
        return render_template('all_books.html', books=books)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/books/<int:id>', methods=['GET'])
def get_one_book(id):
    try:
        book = None

        for b in books:
            if b['ISBN'] == id:
                book = b
                break

        if book:
            return render_template('book_result.html', book=book)
        else:
            return render_template('book_result.html', error="Book not found.")
    except Exception as e:
        return render_template('book_result.html', error=str(e))


@app.route('/books/create', methods=['GET', 'POST'])
def create_book():
    if request.method == 'POST':
        try:
            data = request.form

            if 'title' not in data or 'price' not in data:
                error_message = "Incomplete data."
            else:
                new_book = {
                    "title": data['title'],
                    "author": data.get('author', ''),
                    "ISBN": len(books) + 1,
                    "price": float(data['price'])
                }

                books.append(new_book)

                # Update the JSON file with the new book data
                with open(json_file_path, 'w') as json_file:
                    json.dump(books, json_file)

                return render_template('create_book.html', message="New Book created successfully.")

            return render_template('create_book.html', error=error_message)
        except Exception as e:
            return render_template('create_book.html', error=str(e))
    else:
        # Handle GET request (display the form)
        return render_template('create_book.html')


@app.route('/books/delete_book', methods=['GET', 'POST'])
def delete_book_get():
    if request.method == 'POST':
        try:
            data = request.form
            book_id = data.get('book_id')
            error_message = None

            for book in books:
                if book['ISBN'] == int(book_id):
                    print("YES")
                    books.remove(book)

                    # Update the JSON file without the deleted book
                    with open(json_file_path, 'w') as json_file:
                        json.dump(books, json_file)

                    return render_template('delete_book.html', message="The book deleted.")
                else:
                    error_message = 'Not founded'
            return render_template('delete_book.html', error=error_message)
        except Exception as e:
            return render_template('delete_book.html', error=str(e))
    else:
        return render_template('delete_book.html')


if __name__ == '__main__':
    app.run(debug=True)
