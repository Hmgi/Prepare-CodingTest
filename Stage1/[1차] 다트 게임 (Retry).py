# 1.다트 게임은 총 3번의 기회로 구성된다.
# 2.각 기회마다 얻을 수 있는 점수는 0점에서 10점까지이다.
# 3.점수와 함께 Single(S), Double(D), Triple(T) 영역이 존재하고 각 영역 당첨 시 점수에서 1제곱, 2제곱, 3제곱 (점수1 , 점수2 , 점수3 )으로 계산된다.
# 4.옵션으로 스타상(*) , 아차상(#)이 존재하며 스타상(*) 당첨 시 해당 점수와 바로 전에 얻은 점수를 각 2배로 만든다. 아차상(#) 당첨 시 해당 점수는 마이너스된다.
# 5.스타상(*)은 첫 번째 기회에서도 나올 수 있다. 이 경우 첫 번째 스타상(*)의 점수만 2배가 된다. (예제 4번 참고)
# 6.스타상(*)의 효과는 다른 스타상(*)의 효과와 중첩될 수 있다. 이 경우 중첩된 스타상(*) 점수는 4배가 된다. (예제 4번 참고)
# 7.스타상(*)의 효과는 아차상(#)의 효과와 중첩될 수 있다. 이 경우 중첩된 아차상(#)의 점수는 -2배가 된다. (예제 5번 참고)
# 8.Single(S), Double(D), Triple(T)은 점수마다 하나씩 존재한다.
# 9.스타상(*), 아차상(#)은 점수마다 둘 중 하나만 존재할 수 있으며, 존재하지 않을 수도 있다.
def solution(dartResult):
    answer = 0
    score = [0, 0, 0]
    flag = -1
    calScore = 0
    dartResult = list(dartResult)

    for i in range(len(dartResult)):
        if dartResult[i].isdigit() and dartResult[i+1].isdigit():
            calScore = 10
            flag += 1
        elif dartResult[i].isdigit():
            calScore = dartResult[i]





    return answer


print(solution("1S2D*3T"))
# print(solution("1D2S#10S"))
# print(solution("1D2S0T"))
# print(solution("1S*2T*3S"))
# print(solution("1D#2S*3S"))
# print(solution("1T2D3D#"))
# print(solution("1D2S3T*"))
