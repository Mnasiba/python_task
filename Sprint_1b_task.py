# 1
s = "Programming"
print("1) Uzunluq:", len(s))
print("   İlk simvol:", s[0])

# 2
s1 = "Hello"
s2 = "World"
combined = s1 + " " + s2
print("2) Birləşdirilmiş:", combined)

# 3
text = "Python"
print("3) Son simvol:", text[-1])

# 4
s = "Artificial"
print("4) 'Art' çıxarılmış:", s[3:])  # "Art" = s[0:3]

# 5
word = "Code"
print("5) Tərsinə:", word[::-1])

# 6
s = "abcdefgh"
print("6) Hər ikinci simvol:", s[::2])

# 7
text = "data"
print("7) Böyük:", text.upper(), "| Kiçik:", text.lower())

# 8
s = "Python-R-Java"
split_list = s.split("-")
print("8) Ayrılmış siyahı:", split_list)

# 9
ad = "Ayxan"
yaş = 25
print(f"9) {ad} {yaş} yaşındadır")

# 10
s = "salam-dunya"
print("10) Əvəz olunmuş:", s.replace("-", " "))
