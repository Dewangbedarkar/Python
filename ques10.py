for i in range(3,30):
    for j in range(2,i):
        if i%j==0 :
            print(i," Prime")
            break
    else:
        print(i," not Prime")