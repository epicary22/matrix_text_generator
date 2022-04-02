# letters = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
# japanese = "一 | 乙 | 〇 | 丁 | 七 | 九 | 了 | 二 | 人 | 入 | 八 | 刀 | 力 | 十 | 又 | 乃 | 万 | 丈 | 三 | 上 | 下 | 丸 | 久 | 亡 | 凡 | 刃 | 千 | 口 | 土 | 士 | 夕 | 大 | 女 | 子 | 寸 | 小 | 山 | 川 | 工 | 己 | 干 | 弓 | 才 | 之 | 巾 | 乞 | 于 | 也 | 々 | 勺"
# numbers = "0 1 2 3 4 5 6 7 8 9"

# print(letters.split(" "))
# print(japanese.split(" | "))
# print(numbers.split(" "))

import random

letters_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
japanese_list = ['一', '乙', '〇', '丁', '七', '九', '了', '二', '人', '入', '八', '刀', '力', '十', '又', '乃', '万', '丈', '三', '上', '下', '丸', '久', '亡', '凡', '刃', '千', '口', '土', '士', '夕', '大', '女', '子', '寸', '小', '山', '川', '工', '己', '干', '弓', '才', '之', '巾', '乞', '于', '也', '々', '勺']
numbers_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# 26 + 50 + 10

total_list = letters_list + japanese_list + numbers_list
# print(total_list)

string = ""
for _ in range(50):
    rng = random.random()
    if rng < 0.25:
        character = random.choice(letters_list)
    if rng >= 0.25 and rng < 0.8:
        character = random.choice(japanese_list)
    if rng > 0.8:
        character = random.choice(numbers_list)
    string += character

print(string)
