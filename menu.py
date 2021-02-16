class User:
    def __init__(self,login,password):
        self.login = login
        self.pasword = password


    def to_whom(self,addressee):
        self.addressee = addressee



    def numbers_of_message(self,nbr):
        self.list_of_message=[]
        self.nbr = nbr


    def message(self):
        for x in range(self.nbr):
            print("Input your message and clic enter")
            message = input()
            self.list_of_message.append(message)
