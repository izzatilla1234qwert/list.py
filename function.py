# def myFunction(x):
#     print(x ** 2)

# myFunction(4)
# myFunction(5)
# myFunction(8)
#     print(4 ** 2)
            #     print(8 ** 2)
            #     print(42 ** 2)
            #     print(420 ** 2)
            #     1234567890123456
            # def hide_cart_number(cart_number):
            #     result = ''
            #     if len(cart_number) == 16:
            #         for index, i in enumerate(cart_number):
            #             if index > 3 and index < 12:
                        
            #                 result += '⭐'
            #                 continue
            #             result += i
                    
            #         print(result)
                        

            # hide_cart_number(input("Karta raqamini kiriting: "))




# 111111111
# number = (8, 2, 3, -1, 7)

# def myFunction():
#     a =0
#     for i in number:
#         a += i
#     print(a)

# myFunction()

# 2222222222
# def qwerty():
#     a = input("Matn kiriting: ")
#     kichik = 0
#     katta = 0
#     for i in range(len(a)):
#         if a[i].lower()==a[i]:
#             kichik+=1
#         else:
#             katta+=1

#     print(f"katta harflarsoni {katta}ga, kichik harflar soni esa {kichik}ga teng")

# print(qwerty())         

# i = input(">>>")
# if i.lower()==i:
#     print("AAA")

#3333333333
# list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# list1 =[]
# def toqson():
#     for i in list:
#         if i % 2 != 0:
#             list1.append(i)
#     print(list1)
# toqson()

# 444444444444  

# list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# def JUFTson():
#     a =0
#     for i in list:
#         if i % 2 == 0:
#           a+=1  
#     print(a)
# JUFTson()



# def myCard(*args):
#     new_list = []
#     for i in args:
#         new_list.append(i)
    
#     print(new_list)


# myCard(1,8,2,85, 'Khurshida','Islom')


# def myData(**kwargs):
#     print(kwargs)

#     myData(name='Khurshida',in_lesson='Yomon',have_laptop=True)

# def muFunc(*args,**kwargs)
#     print(args)
#     print(kwargs)

# myFunc('Salom',5,78.52, name='Abdulloh')


# def myFunc(*args, **kwargs):
#     print(args)
#     print(kwargs)

# myFunc('Salom', 5, 78.52, name='Abdulloh')


# def myData(name: str):
#     context = f"Assalomu aleykum {name}"

#     return context

# result = myData(input("Ism kiriting: "))
# print(result)


import random

word = {
    '>': '🙁shu mavzudan',
    '<': '😕boshqa mavzudan',
    'win': '🥳topdingiz'
}

while True:
    print(' yangi oyin')
    random_word = random.randint(word)
    user_word = str(input('soz taxmin qiling:'))

    if user_word == random_word:
        print(word['win'])
    else:       
        while True:
            if user_word > random_word:
                print(word['<'])
            elif user_word < random_word:
                print(word['>'])
            user_word = str(input('soz taxmin qiling')) 
            if user_word == random_word:
                print(word['win'])
                break




