import pandas as pd

# 1) 10, 20, 30, 40 elementlərindən ibarət Series yaradın
s1 = pd.Series([10, 20, 30, 40])

# 2) s1-ə 'w', 'x', 'y', 'z' indekslərini təyin edin
s1.index = ['w', 'x', 'y', 'z']
print("1-2) s1:\n", s1)

# 3) Dictionary-dən Series yaradın
s2 = pd.Series({'p': 5, 'q': 10, 'r': 15})
print("\n3) s2:\n", s2)

# 4) s2-dən 'q' indeksli elementi seçin
print("\n4) s2['q']:", s2['q'])

# 5) s1-dən 25-dən böyük elementləri seçin
print("\n5) s1 > 25:\n", s1[s1 > 25])

# 6) s1-də 20-dən böyük elementləri 10-a bölün
print("\n6) s1 > 20, sonra /10:\n", s1[s1 > 20] / 10)

# 7) ((1, 2), (3, 4)) listindən DataFrame yaradın
df1 = pd.DataFrame([(1, 2), (3, 4)])

# 8) df1-ə sətir və sütun adlarını təyin edin
df1.index = ['r1', 'r2']
df1.columns = ['c1', 'c2']
print("\n7-8) df1:\n", df1)

# 9) Dictionary-dən df2 yaradın
df2 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
print("\n9) df2:\n", df2)

# 10) df2-də 'A' sütunu 1-dən böyük olan sətirləri seçin
print("\n10) df2[df2['A'] > 1]:\n", df2[df2['A'] > 1])
