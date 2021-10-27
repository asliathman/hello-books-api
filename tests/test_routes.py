from flask.wrappers import Response


def test_get_all_books_with_no_records(client):
    # Act
    response = client.get("/books")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []


def test_get_one_book(client, two_saved_books):
    #ACT
    response = client.get("/books/1")
    response_body = response.get_json()

    #ASSERT
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "title": "BOOK 1",
        "description": "DESCRIPTION 1"
    }

def test_get_one_nonexistent_book(client, two_saved_books):
    #ACT
    response = client.get("/books/100")
    response_body = response.get_json()

    #ASSERT
    assert response.status_code == 404
    #how would i wrtie the response body for this test?
    #when I run pytest it says the response body == None,
    #is this because of make_resonse?
    assert response_body == "Error: Book #100 not found"


def test_get_all_books(client, two_saved_books):
    #ACT
    response = client.get("/books")
    response_body = response.get_json()

    #ASSERT
    assert response.status_code == 200
    assert response_body == [
        {
        "id": 1,
        "title": "BOOK 1",
        "description": "DESCRIPTION 1"
        }, 
        {
        "id": 2,
        "title": "BOOK 2",
        "description": "DESCRIPTION 2"
        }
    ]

def test_add_book(client, two_saved_books):
    #ACT
    response = client.post("/books", json={"title": "BOOK 3", "description": "DESCRIPTION 3"})
    response_body = response.get_json()

    #ASSERT
    assert response.status_code == 201
    assert response_body == "BOOK 3 successfully added"

