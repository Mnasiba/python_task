# 1) List yaradın
reqemler = [5, 10, 15, 20]
print("1) reqemler:", reqemler)

# 2) Uzunluq
print("2) Uzunluq:", len(reqemler))

# 3) 25 əlavə et
reqemler.append(25)
print("3) 25 əlavə olunmuş:", reqemler)

# 4) 2-ci indeksə 12 əlavə et
reqemler.insert(2, 12)
print("4) 2-ci indeksə 12 əlavə olunmuş:", reqemler)

# 5) List birləşdirmə
list1 = [1, 2, 3]
list2 = [4, 5, 6]
birlesmis = list1 + list2
print("5) Birləşmiş list:", birlesmis)

# 6) 2-ci və 3-cü elementlər
print("6) 2 və 3-cü elementlər:", reqemler[2:4])

# 7) İlk elementi 50 ilə əvəz et
reqemler[0] = 50
print("7) İlk element 50 ilə əvəz olunmuş:", reqemler)

# 8) 19 olub-olmadığını yoxla
print("8) 19 listdə var?", 19 in reqemler)

# 9) "a" neçə dəfə var
chars = ["a", "b", "a", "c"]
print("9) 'a' sayı:", chars.count("a"))

# 10) "x" elementlərini sil
chars2 = ["x", "y", "x", "z"]
chars2 = [el for el in chars2 if el != "x"]
print("10) 'x' silinmiş list:", chars2)

# 11) Azalan sırayla sıralama
nums = [7, 2, 9, 1]
nums.sort(reverse=True)
print("11) Azalan sırada:", nums)

# 12) 10-dan böyük elementlər
boyuk_10 = [x for x in reqemler if x > 10]
print("12) 10-dan böyük elementlər:", boyuk_10)
