
line = '/'*40 +" ^_^ "+ "/"*40
space = ' '*100

def part():
    print(space)
    print(line)
    print(space)


movies = {
    "Shawshank Redemption": 9.7,
    "The God Father": 8.0
    # 'Key' : 'Value' 
}
print(movies)


part()


#Keys and Values can be added to dictionaries
print("Adding X-men Rating..")
movies['X-men'] = 7.4
print(movies)


part()


print("Adding Mad Max Rating..")
movies['Mad Max'] = 6.5
print(movies)


part()
print("\n \n")

#/////////////////////////////////////////////////////////////////////////////////////


sentence = "Hey there what are you doing hey what"
#len(sentence.split())) Output is the number of words in the sentence

def WordCalc(sentence):
    counter = {}
    words = sentence.split()
    word_count = str(len(sentence.split()))
    
    for word in words:
        if word not in counter:
            counter[word] = 1
        else:
            counter[word] = counter[word] + 1
    
    print("The input sensence: ")
    print(sentence)
    print("\n")
    print("Number of words: " +word_count)
    print("\n")
    print("List of word occurrences:")
    print(counter)
    print("\n")

print(WordCalc(sentence))