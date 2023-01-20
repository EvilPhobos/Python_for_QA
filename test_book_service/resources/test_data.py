from test_book_service.modules.additional.specific_func import fake_data


header = {"Content-Type": "application/json; charset=UTF-8"}
post_json = {"title": "Book 3",
             "type": "Satire",
             "creation_date": fake_data()}
param_creation_date_neg = fake_data() + "-1"
book_types = [
    "Science",
    "Satire",
    "Drama",
    "Adventure",  # Action and Adventure = Adventure
    "Romance"
]
book_types_neg = [
    "Action and Adventure",
    "Romance1"
]
