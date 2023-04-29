def fizzbuzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "fizzbuzz"
    elif number % 3 == 0:
        return "fizz"
    elif number % 5 == 0:
        return "buzz"
    else:
        return str(number)


# computer and player play together one by one
next_number = 0
while next_number < 10:
    next_number = next_number + 1
    print(fizzbuzz(next_number))
    next_number = next_number + 1
    correct_answer = fizzbuzz(next_number)
    player_answer = input("Your go: ")
    if player_answer != correct_answer:
        print(f"you chose wrong from correct one: {correct_answer}")
        break
else:
    print(f"you reached: {next_number}")

# for i in range(1, 50):
#     result = fizzbuzz(i)
#     print(result)
