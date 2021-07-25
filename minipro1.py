class Library:
    def __init__(self,List,name):
        self.booklist=List
        self.name=name
        self.lendDict={}
    def displayBook(self):
        print(f"we have follwing books for the {self.name}'s Librery")
        for book in self.booklist:
            print(book)


    def lendbook(self,user,book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("Lender_book database has been upadated.you can take the book ")
        else:
            print(f"book is already being used by{self.lendDict[book]}")

    def addbook(self,book):
        self.booklist.append(book)
        print("book has been added to the booklist")

    def returnbook(self,book):
        self.lendDict.pop(book)


if __name__ == '__main__':
    het=Library(["python","c++","mongodb",".net","kali linux","c++ basics"],"het")

    while(True):
        print(f"welcome to the{het.name} librery.Enter your choice to continue")
        print("1. Display book")
        print("2.Lend book")
        print("3. Add book")
        print("4.Return book")
        user_choice=int(input())


        if user_choice==1:
            het.displayBook()
        elif user_choice==2:
            book=input("Enter the book you want to Lend")
            user=input("Enter your name")
            print(het.lendbook(user, book))
        elif user_choice==3:
            book=input("Enter the book you want to add")
            het.addbook(book)
        elif user_choice==4:
            book = input("Enter the book you want to return")
            het.returnbook(book)
            print("your book has been updadated")



        else:
            print("not a valid option")

        user_choice2 = input("preed q to quit and c to continue\n")
        if user_choice2 == "q":
            exit()
        elif user_choice2 == "c":
            continue
        else:
            print("not a valid input")































































       


























































