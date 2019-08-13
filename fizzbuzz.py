
for i in range(1, 101):
    if i % 3 == 0 and i % 5 != 0:
        out_str = "Fizz"
    elif i % 5 == 0 and i % 3 != 0:
        out_str = "Buzz"
    elif i % 5 == 0 and i % 3 == 0:
        out_str = "FizzBuzz"
    else:
        out_str = i

    print(out_str)

