#Problem 1: Happy Numbers
# 1. request the number input from the user
# 2. break that input down into individual numbers
# 3. square those numbers separately
# 4. add the sums of the individual squares together
# 5. if the sum of the sums does not equal 1, then repeat and add 1 to a counter
# 6. if the counter hits 30, identify that the number as sad
# 7. If the number is happy, print that the number is "n-iterations" happy

# def happy_num():
#     counter = 0
#     num_used = []
#     user_num = input("Please enter a positive integer")
#     new_num = user_num
#     while new_num != 1 and num_used.count(new_num) != 2:
#         user_num_break = []
#         user_num_sums = []
#         for num in str(new_num):
#             user_num_break.append(num)
#         for sq_num in user_num_break:
#             user_num_sums.append(int(sq_num) * int(sq_num))
#         new_num = 0
#         for list_num in user_num_sums:
#             new_num += list_num
#         counter += 1
#         num_used.append(new_num)
#     if new_num == 1:
#         print(f'{user_num} is {counter} - happy!')
#     else:
#         print(f'{user_num} is sad :(')
    
# happy_num()
    
# Problem 2 Phone Numbers
# 1. Use a for loop to choose each number in range 100
# 2. If that number modulus every number beforehand is = 0, append number in prime list
# 3. append number to divide list in loop
# 4. print prime list

# def prime_num_100():
#     prime_list = []
#     div_list = [1]
#     for num in range(1, 100):
#         if num == 1:
#             prime_list.append(num)
#         if num != 1:
#             div_list.append(num)
#             div_num_sum = 0
#             num_div = []
#             for div_num in div_list:
#                 if num % div_num == 0:
#                     num_div.append(div_num)
#             for add_num in num_div:
#                 div_num_sum += add_num
#             if num + 1 == div_num_sum:
#                 prime_list.append(num)
#     print(prime_list)

# prime_num_100()

# Problem 3: Fibonacci Series
# 1. for each number in the series, add the number previously in the series to itself
# 2. append that new number to the same series
# 3. stop at 5

# def fibonacci_series():
#     fib_series = [int(input("input a number"))]
#     last_num = 0
#     counter = 0
#     for num in fib_series:
#         if counter != 5:
#             next_num = num + last_num
#             fib_series.append(next_num)
#             last_num = num
#             counter += 1
#     print(fib_series)

# fibonacci_series()

