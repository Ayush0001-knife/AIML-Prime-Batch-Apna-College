class Book():
      def __init__(self,title,author,lor):
            self.title=title
            self.author=author
            self.lor=lor

      def displaylor(self):
            print("The list of reviews for the book is: ",self.lor)

      def countlor(self):
            print("The number of reviews for the book is: ",len(self.lor))

      def addlor(self,newlor):
            self.lor.append(newlor)
            print("The new list of reviews for the book is: ",self.lor)

book1=Book("The Great Gatsby","F. Scott Fitzgerald",["Excellent read!","A classic."])
book1.displaylor()
book1.countlor()
book1.addlor("Highly recommended!")