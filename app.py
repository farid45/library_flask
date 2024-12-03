import os

from flask import Flask, render_template, request

from database import db, Book, Genre

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")
db.init_app(app)

with app.app_context():
    db.session.add(
        Book(
            is_read=False
        )
    )

@app.route("/")
def all_book():
    book = Book.query.order_by(Book.added.desc()).all()
    return render_template("book.html", book=book)


@app.route("/book/<int:genre_id>")
def genre(genre_id):
    all_genre = Genre.query.get_or_404(genre_id)
    return render_template("genre.html",
                           books_name = all_genre.book,
                           book=all_genre.book)




if __name__ == '__main__':
    app.run()
