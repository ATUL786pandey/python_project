'''
implement a student libarary system using oop where student can borrow thefrom the list of book
create a seprate library and student class your program must be menu driven 
you are free to choose method and attribute of your choice to implement this functionality
'''


class libarary:
    def __init__(self,listofbook):
        self.listofbook = listofbook


    def displayAvailablebook(self):
        print("Display all the book available")
        for book in self.listofbook:
            print(" * " + book)

    def borrowBook(self,bookname):
        if bookname in self.listofbook:
            print(f"you have issue the {bookname} please take care of book handle it properly")
            self.listofbook.remove(bookname)
            return True
        else:
            print(f"the book {bookname} want to issue is not available know please wait till book is available ")
            return False

    def returnbook(self,bookname):
        self.listofbook.append(bookname)
        print(f"Thank you for returning the {bookname} please visit again if any book required ") 

class student:
    

    def requestbook(self):
        self.book=input("Enter the book name  you want : ")
        return self.book
        
    def returnbook(self):
        self.book=input("Enter the book to return : ")
        return self.book



if __name__ == "__main__":
    lib=libarary(["PYTHON","JAVA","DJANGO","C","C++","SQL","STATISTIC"])
    std=student()
    while(True):
        print("************Welcome To Central Library Club**************")
        print("1 List all Book")
        print("2 request a Book")
        print("3 Return a  Book")
        print("4 Exit")

        a=int(input("Enter your choice :"))

        if a == 1:
            lib.displayAvailablebook()
        elif a== 2:
            lib.borrowBook(std.requestbook())
        elif a == 3:
            lib.returnbook(std.returnbook())
        elif a == 4:
            break
        else:
            print("invalid chioce ")
            continue



        