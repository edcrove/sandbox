import requests

def getTitleFromISBN(isbn): 
    url = f'https://openlibrary.org/isbn/{isbn}.json'
    response = requests.get(url)
    jsonData = response.json()
    return jsonData["title"]

def test_LOTR():
    expectedTitle = "The Lord of the Rings"
    LOTR_isbn = 9780618129027
    actualTitle = getTitleFromISBN(LOTR_isbn)
    assert actualTitle == expectedTitle

def test_LOTF():
    expectedTitle = "The Lord of the Flies"
    LOTF_isbn = 9780618129027 # Wrong ISBN it's going to fail
    actualTitle = getTitleFromISBN(LOTF_isbn)
    assert actualTitle == expectedTitle
