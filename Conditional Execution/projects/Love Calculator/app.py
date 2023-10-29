name_1 = str(input("enter first name: "))
name_2 = str(input("enter second name: "))

name_1 = name_1.lower()
name_2 = name_2.lower()

#True count
t_count = name_1.count("t") + name_2.count("t")
r_count = name_1.count("r") + name_2.count("r")
u_count = name_1.count("u") + name_2.count("u")
e_count = name_1.count("e") + name_2.count("e")
true_total = t_count + r_count + u_count + e_count

#Love count
l_count = name_1.count("l") + name_2.count("l")
o_count = name_1.count("o") + name_2.count("o")
v_count = name_1.count("v") + name_2.count("v")
#We took e's total previously
love_total = l_count + o_count + v_count + e_count

love_score = int(str(true_total) + str(love_total))


if love_score<10 or love_score>85:
    print(f"Your score is: {love_score}. You go together like coke and mentos.")
elif 40<= love_score <= 70:
    print(f"Your score is: {love_score}. You're alright together.")
else:
    print(f"Your score is: {love_score}.")