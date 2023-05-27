print("パスワード")
word = input("mozi")
print(word)

import random
import string

random_number=list(range(1, 10))*2
random_word= list (string.ascii_lowercase)
choices=random_number + random_word
number= input("文字数：")
decide_number = int(number)
for i in range(decide_number):
    random_pass = random.choice(choices)
    print(random_pass)

