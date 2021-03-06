def solution(num):
    answer = 0

    # 3. 결과로 나온 수에 같은 작업을 1이 될 때까지 반복한다.
    while num != 1:
        # 1. 입력된 수가 짝수라면 2로 나눕니다.
        if num % 2 == 0:
            num = num / 2
            answer += 1

        # 2. 입력된 수가 홀수라면 3을 곱하고 1을 더합니다.
        elif num % 2 == 1:
            num = num * 3 + 1
            answer += 1

        if answer == 500:
            return -1

    return answer


print(solution(6))
print(solution(16))
print(solution(626331))