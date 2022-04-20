class Books():
    def __init__(self, title, author, pages, rating):
        self.title = title
        self.author = author
        self.pages = pages
        self.rating = rating


    def get_values(self):
        print(f"\nTitle: {self.title.title()}\nAuthor: {self.author.title()} \nPages: {self.pages}\nRating: {self.rating}\n")

bookshelf = []


#Sci Fi
Astronaut = Books("der astronaut", "andy weir", 560, "4,7/5")
Anhalter = Books("per anhalter durch die galaxis", "douglas adams",200 , "4,1/5" )
Dune = Books("dune - der wüstenplanet", "frank herbert", 644, "4,3/5" )

scifi = [Astronaut, Anhalter, Dune]
bookshelf.append(scifi)

#Thriller
Therapie = Books("die therapie", "sebastian fitzek", 349, "4,8/5")
Rätsel = Books("das rätsel", "john katzenbach", 470, "4,5/5")
Origin = Books("origin", "dan brown", 687, "4,7/5")

thriller = [Therapie, Rätsel, Origin]
bookshelf.append(thriller)

#Crime

Macbeth = Books("macbeth", "jo nesbø", 485, "4,5/5")
Münster = Books("münsters fall", "hakan nesser", 379, "4,2/5")
Chemie = Books("chemie des todes", "simon beckett", 473, "4,6/5")

crime = [Macbeth, Münster, Chemie]
bookshelf.append(crime)


