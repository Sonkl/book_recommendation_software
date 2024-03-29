from books import Books, bookshelf


available_genres = ["thriller", "sci fi", "crime"] 

#Building a Tree
class Tree():

    def __init__(self, value):
        self.value = value
        self.child = []


    def add_child(self, child):
        self.child.append(child)


    def traverse(self):
        nodes_to_visit = self.child
        while nodes_to_visit:
            current_node = nodes_to_visit.pop()
            current_node.value.get_values()
            

#Adding Tree Nodes

books = Tree("Books")
genres = []
scifi = Tree("Sci Fi")
thriller = Tree("Thriller")
crime = Tree("Crime")
genres.append(scifi)
genres.append(thriller)
genres.append(crime)

#Adding Child Nodes

for genre in genres:
    books.add_child(genre)

scifi_books = []
for book in bookshelf[0]:
    scifi_books.append(Tree(book))

for book in scifi_books:
    scifi.add_child(book)

thriller_books = []
for book in bookshelf[1]:
    thriller_books.append(Tree(book))

for book in thriller_books:
    thriller.add_child(book)


crime_books = []
for book in bookshelf[2]:
    crime_books.append(Tree(book))

for book in crime_books:
    crime.add_child(book)



#function for searching a genre in books children

def genre_search(root, genre):
    for child in root.child:
        if child.value == genre:
            print(child.value) 
            return child.traverse()



#genre_search(books, "Sci Fi")

#Recommendation with user input

def user_input():

    welcome = input("""Please choose amongst the following genres:\nThriller\nSci Fi\nCrime\n""")

    if welcome.lower() in available_genres:
        genre_search(books, welcome.title())
    else:
        user_input()

    play_again()

def play_again():

    again = input("Do you want recommendations for another genre? Enter \"y\" for \"yes\" or \"n\" for \"no\": " )
    if again == "y":
        return user_input()
    elif again == "n":
        print("Thank you for using my Book Recommendation! I hope you found something you like.")
    else:
        play_again()

print("Welcome to Sonji's Book Recommendation!")
user_input()