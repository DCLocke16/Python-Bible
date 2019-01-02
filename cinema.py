films = {
    "Finding Dory": [3, 5],
    "Bourne": [18, 5],
    "Tarzan": [15, 5],
    "Ghost Busters": [12, 5]
}

while True:
    print("Welcome to the Cinema!")

    choice = input("Which film would you like to see? ").strip().title()

    if choice in films:
        age = int(input("How old are you? ").strip())

        # check user age
        if age >= films[choice][0]:

            # check enoungh seats
            num_seats = films[choice][1]
            if num_seats > 0:
                films[choice][1] = films[choice][1] - 1
                print("Enjoy the film!")
            else:
                print("Sorry we are sold out for that film.")
        else:
            print("You are to young to see the film....sorry!")
    else:
        print("We are not currently showing that film.....sorry!")
