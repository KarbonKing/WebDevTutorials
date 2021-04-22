#Let's filter movies with 7+ ratings

movies = [("Interstellar", 10), ("Ironman", 8.2), ("It Folows", 6.0), ("X-Men", 7)]
# There are three Tuples in this list. Each tuple has 2 elements

print(movies[0])  #Prints both elements of the first tuple
print(movies[0][0]) #Prints first element of the first tuple
print(movies[0][1]) #Prints second element of the first tuple


def rating_filter(movies, rating_min):
    print("Films above " +str(rating_min)+ " stars:")
    filtered_list = []
    for movie in movies:
        if movie[1] >= rating_min:
            filtered_list.append(movie[0])
    return filtered_list

print(rating_filter(movies, 6.5)) #Prints the movies that are above the rating_min



# Tuples: Tuples are used to store multiple items in a single variable.

#mytuple = ("apple", "banana", "cherry")



# Lists: Lists are used to store multiple items in a single variable.

# mylist = ["apple", "banana", "cherry"]







