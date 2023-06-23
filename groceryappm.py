#class to get user details
class User:
    def __init__(self,username,password):
        self.Username = username
        self.Password = password

#class to get grocery items
class GroceryItem:
    def __init__(self,item_id,name,price,avail_quantity):
        self.ItemId = item_id
        self.Name = name
        self.Price = price
        self.Quantity = avail_quantity

#main app environment
class GroceryStoreApp:

    def __init__(self):
        self.users = []
        self.logged_in_user = None
        self.grocery_items = []
        self.cart =[]
        self.booked_history = []

    #login
    def login(self,username,password,users):
        for user in users:
            if user.Username == username:
                if user.Password == password:
                    self.logged_in_user = user
                    print("Login Successful")
                    return True
                else:
                    print("Incorrect Password")
                    return False
        print("Incorrect Username")
        return False
    
    #Choice 1 : Display Grocery Items
    def display_grocery_items(self):
        print("Grocery Items:")
        for item in GroceryListItems:
            print(f"{item.ItemId}, {item.Name}: Rs{item.Price}")
            print('--------------------------------------------')
    
    #Choice 2 : Add to cart
    def add_to_cart(self,item_name,item_quantity):
        for item in GroceryListItems:
            if item.Name == item_name:
                if item_quantity <= item.Quantity: #user_gn_input <= availbale quantity
                    self.cart.append(item)
                    print(f"{item_quantity} {item.Name} added to cart.\n")
                    return
                else:
                    print("Not enough stock\n")
                    return
        print("Item not found.")

    #Choice 3 : View Cart
    def view_cart(self):
        print("My Cart Items:")
        print("------------------------------------")
        for item in self.cart:
            print(f"{item.Name}: Rs{item.Price}")
            print(f"Quantity of {item.Name} = {item_quantity}")
        print("------------------------------------")

    #Choice 4 : Booked History 
    def check(self):
        total_price = 0
        for item in self.cart:
            total_price+=(item.Price*item_quantity)

        self.booked_history.append((self.logged_in_user,self.cart,total_price))
        print("Checkout Successful\n")

    def view_booked_history(self):
        print("Booking History:")
        for user,cart,total_price in self.booked_history:
            print(f"User: {user.Username}")
            print("Cart:")
            for item in cart:
                print(f"{item.Name}: Rs{item.Price}")
            print("--------------------------------------")
            print(f"Total Price: Rs{total_price}" )
            print("--------------------------------------")

    #Choice 5 : Delete History
    def delete_history(self):
        self.cart=[]
        self.booked_history = []
        print("Booking History Deleted\n")

    #Choice 6 : Logout
    def logout(self):
        self.logged_in_user = None
        print("Logout Successful")
        return



if __name__ == "__main__":
    users=[
        User("user1","password1"),
        User("user2","password2"),
        User("user3","password3")
    ]    

    GroceryListItems = [
        GroceryItem(1, 'Mango', 20, 100),
        GroceryItem(2, 'Cauliflower', 40, 100),
        GroceryItem(3, 'Cabbage', 30, 100)
    ]

    app = GroceryStoreApp()
    
    #login
    username = input("Enter Username:")
    password = input("Enter Password:")
    result = app.login(username,password,users)
    if(result):
        CustomerInApp = True
        while(CustomerInApp):
            print("Customer Menu")
            print("1. Display the grocery")
            print("2. Add to cart")
            print("3. View cart")
            print("4. Booked History")
            print("5. Delete your history")
            print("6. Logout")

            choice = int(input("Enter your Choice: "))

            if choice==1:  #Display the grocery
                app.display_grocery_items()
                
            elif choice==2: #Add to Cart
                num_of_items = int(input("Enter the number of grocery items u want to buy:"))
                for i in range(num_of_items):
                    item_name = input(f"Enter the item name {i+1}:")
                    item_quantity = int(input(f"Enter the number of {item_name}:"))
                    app.add_to_cart(item_name,item_quantity)
            
            elif choice==3:
                app.view_cart()
            
            elif choice==4:
                app.check()
                app.view_booked_history()
            
            elif choice==5:
                app.delete_history()
            
            elif choice==6: #Logout
                #logout
                CustomerInApp = False
                app.logout()
                

        

