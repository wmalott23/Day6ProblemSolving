# Reversing a string

# def rev_string():
#     char_list = []
#     rev_list = []
#     user_input = input("What word would you like reversed?")
#     user_len = len(user_input)
#     neg_len_range = range(-1, -(user_len)-1, -1)
#     for char in user_input:
#         char_list.append(char)
#     for neg_num in neg_len_range:
#         rev_list.append(char_list[neg_num])
#     answer = ''.join(rev_list)
#     print(answer)

# rev_string()

# Capitalize letter

# def cap_words():
#     cap_list = []
#     word_list = input("Please enter a sentence here.")
#     split_list = word_list.split()
#     for word in split_list:
#         word = word.capitalize()
#         cap_list.append(word)
#     cap_sents = ' '.join(cap_list)
#     print(cap_sents)

# cap_words()

# Compress a string of characters

# def dup_removal():
#     num_chars = []
#     str_chars = []
#     num_str = []
#     char_count = 0
#     user_string = input("Please enter a string of random characters")
#     last_char = user_string[0]
#     for char in user_string:
#         if char == last_char:
#             char_count += 1
#             last_char = char
#         else:
#             num_chars.append(char_count)
#             char_count = 1
#             str_chars.append(last_char)
#             last_char = char
#     num_chars.append(char_count)
#     str_chars.append(last_char)
#     for each in range(len(num_chars)):
#         num_str.append(str(num_chars[each]))
#         num_str.append(str_chars[each])
#     result = ''.join(num_str)
#     print(result)

# dup_removal()
    
# Palindrome

# def palindrome_check():
#     char_list = []
#     rev_list = []
#     user_input = input("Let's see if your word is a palindrome!")
#     user_len = len(user_input)
#     neg_len_range = range(-1, -(user_len)-1, -1)
#     for char in user_input:
#         char_list.append(char)
#     for neg_num in neg_len_range:
#         rev_list.append(char_list[neg_num])
#     answer = ''.join(rev_list)
#     if user_input == answer:
#         print("It is a palindrome!")
#     else:
#         print("Nope")

# palindrome_check()