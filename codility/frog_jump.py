def solution(X, Y, D):
    distance = Y-X
    return distance//D+1 if distance%D != 0 else distance//D
