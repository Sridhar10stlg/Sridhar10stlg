class User:
    def __init__(self, username, password):
        self.UserName = username
        self.Password = password
        self.booking_history = []

class Movie:
    def __init__(self, title, duration, showtimes, seats_available):
        self.Title = title
        self.Duration = duration
        self.ShowTimes = showtimes
        self.AvailableSeats = seats_available
        self.reviews = []

class Booking:
    def __init__(self, user, movie, showtime, seats_booked, total_price):
        self.User = user
        self.Movie = movie
        self.Showtime = showtime
        self.SeatsBooked = seats_booked
        self.TotalPrice = total_price

class MovieTicketBookingApp:
    def __init__(self):
        self.logged_in_user = None

    #login
    def login(self,username,password,userdata):
        for user in userdata:
            if user.UserName == username:
                if user.Password == password:
                    self.logged_in_user = user
                    print("Login Successful....")
                    return user
                else:
                    print("Invalid Password")
                    return
        print("Incorrect Username...")
        return
    
    #register user
    def register_user(self,username, password, userdata):
        for user in userdata:
            if user.UserName == username:
                print("Username already exists....")
                return
        new_user = User(username, password)
        userdata.append(new_user)
        print("Registration Successful.....")
       
    #Display List of Movies
    def display_movies(self):
        print("Movies running now...")
        print("----------------------------------------------")
        for movie in moviesdata:
            print(f"{movie.Title} = {movie.Duration} minutes")
            print("----------------------------------------------")

    #display details of gn movie
    def display_movie_details(self,title):
        for movie in moviesdata:
            if movie.Title == title:
                print("----------------------------------------------")
                print(f"Movie Name: {movie.Title}")
                print(f"Duration: {movie.Duration}")
                print(f"Showtimes: {', '.join(movie.ShowTimes)}")
                print(f"Available seats: {movie.AvailableSeats}")
                print("----------------------------------------------")
                return
        print("Incorrect Movie name or Movie not found")

    #select showtime
    def select_showtime(self,title,showtime):
        for movie in moviesdata:
            if movie.Title == title:
                if showtime in movie.ShowTimes:
                    return movie
        return None
    
    #book seats/ticket
    def book_seats(self, logged_in_user, Movie_chosen, showtime, seats_booked):
        total_price = seats_booked * 120 #Rs.120 price of each ticket
        if Movie_chosen.AvailableSeats >= seats_booked:
            Movie_chosen.AvailableSeats = Movie_chosen.AvailableSeats - seats_booked
            booking = Booking(logged_in_user, Movie_chosen, showtime, seats_booked, total_price)
            logged_in_user.booking_history.append(booking)
            print(f"{seats_booked} tickets booked for {Movie_chosen.Title}")
        else:
            print("Sorry, Not enough seats available")

    #View booking history
    def view_booking_history(self, logged_in_user):
        print("Booking History....")
        for booking in logged_in_user.booking_history:
            print('--------------------------------------------')
            print(f"Movie: {booking.Movie.Title}")
            print(f"Showtime: {booking.Showtime}")
            print(f"Seats Booked: {booking.SeatsBooked}")
            print(f"Total Price: {booking.TotalPrice}")
            print('--------------------------------------------')
            
    #Add review
    def add_review(self, title, rating, review):
        for movie in moviesdata:
            if movie.Title == title:
                movie.reviews.append([rating,review])
                print("Review added Successfully....")
                return
        print("Movie Not found////")
        
    #logout
    def logout(self):
        self.logged_in_user = None
        print("Logout Successful...")
        print("!!!!!!!!!!!!!!!!!!!!")
        return


if __name__ == '__main__':
    userdata = [
        User("alex","123"),
        User("Kevin","asdfgf")
    ]

    moviesdata = [
        Movie("Leo",120,['8:00AM','11:00AM','3:00PM','6:00PM'],240),
        Movie("Jailer",120,['8:00AM','11:00AM','3:00PM','6:00PM'],240)
    ]
    
    app = MovieTicketBookingApp()

    CustomerInApp = True
    while CustomerInApp:
        print("1. Register")
        print("2. Login")
        
        choice = int(input("Enter your choice: "))

        #register
        if choice == 1:
            print("---Create Account---")
            username = input("Enter username for registration: ")
            password = input("Enter password for registration: ")
            app.register_user(username,password,userdata)


        #login
        elif choice == 2:
            username = input("Enter Username: ")
            password = input("Enter Password: ")
            logged_in_user = app.login(username,password,userdata)

            if logged_in_user:
                isLogin = True
                while isLogin:
                    print("1. List of Movies")
                    print("2. Showtime & Seat Selection")
                    print("3. Payment Options")
                    print("4. Movie Rating and Reviews")
                    print("5. Booking History")
                    print("6. Logout")
                    

                    choice = int(input("Enter your Choice: "))

                    #1. Movie Listings
                    if choice == 1:
                        app.display_movies()
                    
                    #2. Showtime & Seat Selection
                    elif choice == 2:
                        title = input("Enter the movie title: ")
                        app.display_movie_details(title)
                        showtime = input("Enter the available showtime: ")
                        Movie_chosen = app.select_showtime(title, showtime)
                        if Movie_chosen:
                            seats_booked = int(input("Enter the number of seats to be booked: "))
                            app.book_seats(logged_in_user, Movie_chosen,showtime,seats_booked)
                        else:
                            print("Invalid Movie title or showtime.....")
                    
                    #3. Payment Options
                    elif choice == 3:
                        pass

                    #4. Movie Rating and Reviews
                    elif choice == 4:
                        title = input("Enter the movie title: ")
                        rating = float(input("Enter the rating(out of 5): "))
                        review = input("Enter your review: ")
                        app.add_review(title, rating, review)

                    #5. Booking History
                    elif choice == 5:
                        app.view_booking_history(logged_in_user)

                    #6. Logout
                    elif choice == 6:
                        isLogin = False
                        app.logout()

                    else:
                        print("Invalid Choice.....")

        else:
            print("Invalid Input....")
            break
    

    
        
    

