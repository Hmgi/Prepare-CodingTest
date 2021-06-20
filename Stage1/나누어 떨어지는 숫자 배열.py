def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0:
            answer.append(i)

    if not answer:
        answer.append(-1)

    answer.sort()

    return answer


print(solution([5, 9, 7, 10]))
print(solution([2, 36, 1, 3]))
print(solution([3, 2, 6]))
