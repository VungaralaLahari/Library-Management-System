class Library():
    books={}
    def create (  name , author , year_of_publication,id):
        if id in Library.books:
            print("Already Present")
            
        else:
            Library.books[id]=name
            print(f" '{name}' written by {author} published in { year_of_publication} is successfully added.")

    def show():
        print("--Central Library Hyderabad--")
        print(Library.books)
        print("Number of books:",len(Library.books))


    def search(search_id):
        if Library.books=={}:
            print("Empty! No Books yet ")
        elif search_id in Library.books.keys():
            print(f" Book : {Library.books.get(search_id)} of id {search_id} Found Successfully!")
        else:
            print("Book Not Available")

    def delete_book(del_id):
         if Library.books=={}:
            print("Empty! No Books yet ")
        else : 
            if del_id in Library.books:
                del Library.books[del_id]
                print("deleted")
           

        else:
            print("Book not found with such id ")
        
            

b=Library()
while True:
    n=int(input("--MENU--\n 1. Add Book \n 2. Check All Available books \n 3.Search Book \n 4. Delete Book \n 5.Exit"))

    if n==1:
        print("Enter the Book details:")
        name=input("Name of Book:")
        author = input("Name of the Author:")
        year_of_publication = int(input("Year of Publication:"))
        id = int(input("Enter the Book_id:"))
        Library.create(name,author,year_of_publication,id)

    elif n==2:
        Library.show()

    elif n==3:
        search_id = int(input("Enter the Book id to be Searched:"))
        Library.search(search_id)

    elif n==4:
        del_id = int(input("Enter the Book Id that is to be deleted:"))
        Library.delete_book(del_id)

    elif n==5:
        print("Exiting...")
        break 


    else:
        print("Invalid Choice")


        