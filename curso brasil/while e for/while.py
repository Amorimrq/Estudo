count = 0
while count + 1 <= 20:
    if count % 5 == 0:
        print("skip")
        count += 1
        continue
    print(count)
    count+=1