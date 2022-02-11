#Intro to Dictionaries.. The Ultimate Key + Value Mapping Tool

#Dictionaries contain pairs of information that go hand in hand.

phone_book = {
    "John":"222-333-4434",
    "Billy":"444-555-2231"
    }

print("Billy's phone number is " +phone_book['Billy'])

movies = {"Shawshank Redeption":9.7,
"The Godfather": 8.0
}

print("The Godfather was rated " +str(movies['The Godfather'])+ " stars")

authors = {
    "Rafeh Qazi":['b1', 'b2'] #List within a Dictionary
    }

print(authors["Rafeh Qazi"][1])
