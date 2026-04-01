a = int(input("1. 입력한 수식을 계산 2. 두 수 사이의 합계 : "))

if a == 1 :
    num = input("수식을 입력하세요 : ")
    answer = eval(num)
    print(num,"결과는", answer,"입니다.")

elif a == 2 :
    num1 = int(input("첫 번째 수를 입력하세요 : "))
    num2 = int(input("두 번째 수를 입력하세요 : "))
    answer = 0
    for b in range(num1, num2+1) : 
        answer = answer + b
    print(num1,"+...+",num2," 결과는 ",answer,"입니다.")

else : 
    print("1 또는 2만 입력하세요.")
