import pytest
from app import create_app
from app import db
from app.models.book import Book

@pytest.fixture
def app():
    app = create_app({"TESTING": True})

    with app.app_context():
        db.create_all()
        yield app

    with app.app_context():
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def two_saved_books(app):
    #ARRANGE
    book_1 = Book(title="BOOK 1",
    description="DESCRIPTION 1")

    book_2 = Book(title="BOOK 2",
    description="DESCRIPTION 2")

    db.session.add_all([book_1, book_2])
    db.session.commit()


#(if I'm understanding it correctly) that these two fixtures 
#when used together work to make a copy of the database that 
#is manipulated in the process of the tests and then destroyed
#after--a little simulation of what would happen if you 
#actually ran these requests using the actual database (?). 