# Program #2: Movie Tix
# Write a program that has the user input various movie names and how many 
# tickets are desired for each movie.  
# At the end of the program it prints out the total number of tickets desired by the user.  
# Use either a "for loop" or "while loop" to accomplish this.

def main():
    ######################
    total_tickets = 0
    number_movies = int(input("How many movies?: "))
    for n in range(number_movies):
        movie_name = input(f"Enter the name of movie #{n+1}: ")
        tickets = int(input(f"How many tickets for {movie_name}?: "))
        total_tickets += tickets
    print(f"Total tickets: {total_tickets}: ")
    ######################


if __name__ == '__main__':
    main()