import random
print("** 로또 추첨을 시작합니다. **")
print("\n추첨된 로또 번호 ==>",end=" ")
for a in range(1,7):
    print(random.randrange(1,46),end=" ")