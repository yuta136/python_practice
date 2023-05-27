print("パスワード")
word = input("mozi")
print(word)

import random

number= input("文字数：")
decide_number = int(number)
for i in range(decide_number):
    random_number = random.randint(1, 9)
    print(random_number)

