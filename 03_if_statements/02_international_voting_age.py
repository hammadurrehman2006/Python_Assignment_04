# -------------------PROBLEM STATEMENT:
'''
Write a program which asks a user for their age and lets them know if they can or can't vote in the following three fictional countries.
-Around the world, different countries have different voting ages. In the fictional countries of Peturksbouipo, Stanlau, and Mayengua, the voting ages are very different:
-the voting age in Peturksbouipo is 16 (in real life, this is the voting age in, for example, Scotland, Ethiopia, and Austria)
-the voting age in Stanlau is 25 (in real life this is the voting age in the United Arab Emirates)
-the voting age in Mayengua is 48 (in real life, as far as we can tell, this isn't the voting age anywhere)
'''


# constant voting ages
Peturksbouipo = 16
Stanlau = 25
Mayengua = 48

def main():
# user age for input
    user_age = int(input("Hi! How old are you? "))
# checking age limit for Peturksbouipo
    if user_age >= Peturksbouipo:
        print("You are capable for voting in Peturksbouipo, Where as the voting age in this country is " + str(Peturksbouipo))
    else:
        print("Sorry! You cannot vote in Peturksbouipo, Where as the voting age in this country is " + str(Peturksbouipo))

# checking age limit for stanlau
    if user_age >= Stanlau:
        print("You are capable for voting in Stanlau, Where as the voting age in this country is " + str(Stanlau))
    else:
        print("Sorry! You cannot vote in Stanlau, Where as the voting age in this country is " + str(Stanlau))

# checking age limit for Mayengua
    if user_age >= Mayengua:
        print("You are capable for voting in Mayengua, Where as the voting age in this country is " + str(Mayengua))
    else:
        print("Sorry! You cannot vote in Mayengua, Where as the voting age in this country is " + str(Mayengua))
# calling function
if __name__ == "__main__":
    main()