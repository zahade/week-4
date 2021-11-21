# A time traveler has suddenly appeared in your classroom!

# Create a variable representing the traveler's
# year of origin (e.g., year = 2000)
# and greet our strange visitor with a different message
# if he is from the distant past (before 1900),
# the present era (1900-2020) or from the far future (beyond 2020).


# replaced '==' with '=', 'int.input' with 'int(input)' and single quotes with double quotes
year = int(input("Greetings! What is your year of origin?"))

if year <= 1900:  # added a ":" after 1900
    # replaced single quotes with double quotes
    print("Woah, that's the past!")
elif year > 1900 & year < 2020:  # replaced '&&' with '&'
    print("That's totally the present!")
else:  # replaced elif statement with else statement
    print("Far out, that's the future!!")
