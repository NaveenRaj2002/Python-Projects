def fact_num():
    fact = []
    num = int(input("Enter a number: "))
    number = abs(num)
    for i in range(1, number + 1):
        if number % i == 0:
            fact.append(i)
    print(f"The factors of {number} is {fact}")
fact_num()