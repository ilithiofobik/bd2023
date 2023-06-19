def S(s, k, m):
    return 1 - (1 - s**k)**m

eps = 0.0105

if __name__ == "__main__":
    min_diff = 2.0
    min_k = 0
    min_m = 0

    for k in range(100):
        for m in range(1000):
            S1 = S(1.0 / 3.0, k, m)
            S2 = S(0.5, k, m)
            d1 = abs(S1 - 0.1)
            d2 = abs(S2 - 0.9)

            if d1 * d1 + d2 * d2 < min_diff:
                min_diff = d1 * d1 + d2 * d2
                min_k = k
                min_m = m

    min_s1 = S(1.0 / 3.0, min_k, min_m)
    min_s2 = S(0.5, min_k, min_m)    
    print("k = {}, m = {}, S1 = {}, S2 = {}".format(min_k, min_m, min_s1, min_s2))