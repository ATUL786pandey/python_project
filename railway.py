class Railway:
    
    def __init__(self):
        self.seat=300

    def displayseat(self):
        return self.seat
        
    
    def bookTicket(self,passanger):
        if passanger < self.seat :
            print(f"the ticket  for  {passanger} passanger  is booked \n Enjoy Your Journey")
            self.seat=self.seat - passanger
            return f" seat available in the train  is  {self.seat}"
        else:
            print(f"the seat for no of  {passanger} passanger  is not availabe please check another train ")
            return f"thank you"

    def cancelTicket(self,passanger):
        
        if  self.seat == 300:
            print("sorry ticket are not booked in this train please check the another ")
            return self.seat
            
        else:
            
            print(f"the ticket for {passanger} passanger has been cancel")
            self.seat=self.seat + passanger
            return f" seat available in train is {self.seat}"

class passanger:
    def bookTicket(self):
        self.book=int(input("Enter the no of ticket to book : "))
        return self.book

    def cancelTicket(self):
        self.book=int(input("Enter the no of ticket to cancel : "))
        return self.book


if __name__ == "__main__":
    rly=Railway()
    psg=passanger()
    #print(rly.bookTicket())
    #print(rly.cancelTicket(5))
    #print(rly.displayseat())


    while(True):
        print("*******************Welcome to Indian Railway*********************** ")
        print("-------------------We are happy to help you-------------------------")
        print(" 1 press for seat available ")
        print(" 2 for book ticket")
        print(" 3 for cancel ticket ")
        print(" 4 for exit")


        a=int(input("Enter your choice : "))

        if a ==1:
            print(rly.displayseat())
        elif a ==2:
            print(rly.bookTicket(psg.bookTicket()))
        elif a ==3:
            print(rly.cancelTicket(psg.cancelTicket()))
        elif a== 4:
            break
        else:
            print("invallid choice ")
            continue

        