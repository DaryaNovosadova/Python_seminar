# 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

def encode(s):
    encoding = ""
    i = 0
    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i + 1]:
            count = count + 1
            i = i + 1
        encoding += str(count) + s[i]
        i = i + 1
    return encoding

s = str(input())
l = encode(s)

def decode(l):
    decoding = ''
    i = ''
    for char in l:
        if char.isdigit():
            i += char
        else:
            decoding += char * int(i)
            i = ''
    return decoding

d = decode(l) 

with open("text_words.txt", "a", encoding="utf-8") as file:
    file.write(f"{s}\n")
with open("text_code_words.txt", "a", encoding="utf-8") as file:
    file.write(f"{l}\n")
with open("text_decode_words.txt", "a", encoding="utf-8") as file:
    file.write(f"{d}\n")

print(l)
print(d)
