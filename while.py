# # i = 0
# # while i < 10:
# #     print(i)
# #     i += 1  # i = i + 1


# # my_list = ["Nola", "Lola", "Gul", "Atir gul"]

# # item = 0
# # while item < len(my_list):
# #     if my_list[item] != "Lola":
# #         print(my_list[item])
# #     item += 1


# # my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # i = 0

# # while i < len(my_list):
# #     if my_list[i] % 2 != 0:
# #         print(i)
# #     i += 1


# # new_list = ['Nexia', 'Gentra', 'Damas', 'Tiko', 'Matiz', 'Cobalt']
# # k = 0
# # break
# # continue

# # while k < len(new_list):
# #     print(new_list[k])
# #     k+=1
# #     if new_list[k] == "Tiko":
# #         break

# # while k < len(new_list):
# #     if new_list[k] == "Tiko":
# #         k += 1
# #         continue
# #     print(new_list[k])
# #     k += 1



# import random


# new_num = random.randint(1, 100)

# words = {
#     'win': '🥳 Tabriklaymiz siz g`olib bo`ldingiz!',
#     'lose': '😕 Siz topaolmadingiz. Yana urinib ko`ring!'
# }

# while True:
#     user_num = int(input("Dastur o`ylagan soni kiriting: "))

#     if user_num == new_num:
#         print(words['win'])
#         break

#     print(words['lose'])

import random

word = {
    '>': '🙁Kattaroq raqam kiriting',
    '<': '😕Kichikroq raqam kiriting',
    'win': '🥳topdingiz'
}

while True:
    print('\n yangi oyin')
    random_num = random.randint(1,100)
    user_num = int(input('son taxmin qiling:'))

    if user_num == random_num:
        print(word['win'])
    else:
        while True:
            if user_num > random_num:
                print(word['<'])
            elif user_num < random_num:
                print(word['>'])
            user_num = int(input('1 dan 100 gacha bolgan raqamni taxmin qiling:'))
            if user_num == random_num:
                print(word['win'])
                break
