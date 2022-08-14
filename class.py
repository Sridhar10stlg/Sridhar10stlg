class Player:
    fees = 1000
    def __init__(self, name, age, role):
        self.name = name
        self.role = role
        self.age = age

    def address(self):
        add = f" Name:{self.name}\n Age : {self.age}\n Role: {self.role}\n Fees: {self.fees}" 
        return add  
    
    

P1 = Player('Hari', 20, 'Fast Bowler')
P2 = Player('Arun', 20, 'Batsman')

print(P1.address())
print(P2.address())
