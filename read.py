data = []
count = 0
with open("reviews.txt", "r") as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 1000 == 0:
            print(len(data))
print("檔案讀取完了，總共有", len(data), "筆資料")


#計數功能
sum_len = 0
for d in data:
    sum_len += len(d)
print("每筆留言平均長度為", sum_len/len(data))

new = []
for d in data:
    if len(d) < 100:
        new.append(d)
print("一共有", len(new), "筆留言長度小於 100")

good = []
for d in data:
    if "good" in d:
        good.append(d)
print("一共有", len(good), "筆資料含有good")

print(data[0])


#留言分析程式
wc ={}
for d in data:
    words = d.split()#split的預設值是空白鍵，所以可以不要寫，就會自動用空白鍵當切割的基準
    for word in words:
        if word in wc:
            wc[word] += 1
        else:
            wc[word] = 1 #新增新的key進字典

for word in wc:
    if wc[word] > 1000000:
        print(word, wc[word])

print(len(wc))


while True:
    word = input("請問你想查什麼字：")
    if word == "q":
        break
    if word in wc:
        print(word, "出現過的次數為：", wc[word])
    else:
        print("這個字沒有出現過喔！")

print("感謝使用本功能")



