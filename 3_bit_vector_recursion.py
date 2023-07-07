def gen01(idx, vector):
    if idx >= len(vector):
        print(*vector, sep='')
        return
        # range(2) because we need 0 and 1
    for num in range(2):
        vector[idx] = num
        gen01(idx + 1, vector)


n = int(input())
vector = [0] * n
gen01(0, vector)