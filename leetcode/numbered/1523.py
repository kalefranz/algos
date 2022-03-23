# 1, 1 => 1 , 0, 0
# 1, 2 => 1 , 1, 0
# 1, 3 => 2 , 2, 1
# 1, 4 => 2 , 3, 1
# 1, 5 => 3 , 4, 2
# 1, 6 => 3 , 5, 2

# 2, 2 => 0 , 0, 0
# 2, 3 => 1 , 1, 0
# 2, 4 => 1 , 2, 1
# 2, 5 => 2, 3, 1
# 2, 6 => 2, 4, 2

# 4, 5 => 1, 1, 0
# 4, 7 => 2, 3, 1

def countOdds(low, high):
    low_even = low % 2 == 0
    high_even = high % 2 == 0
    x = (high - low) // 2
    if low_even and high_even:
        return x
    return x + 1

print(1, countOdds(7, 7))
print(1, countOdds(7, 8))
print(2, countOdds(7, 9))
print(2, countOdds(7, 10))
print(3, countOdds(7, 11))
print(3, countOdds(7, 12))
print()
print(0, countOdds(8, 8))
print(1, countOdds(8, 9))
print(1, countOdds(8, 10))
print(2, countOdds(8, 11))
print(2, countOdds(8, 12))
print(3, countOdds(8, 13))
