# 행렬의 곱셈
def productMatrix(A, B):
    answer = []

    for i in range(len(A)):
        answer.append([])
        for j in range(len(B[0])):
            answer[i].append(0)
            for k in range(len(B)):
                answer[i][j] += A[i][k] * B[k][j]

    return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
a = [[1, 2], [2, 3]];
b = [[3, 4], [5, 6]];
print("결과 : {}".format(productMatrix(a, b)));