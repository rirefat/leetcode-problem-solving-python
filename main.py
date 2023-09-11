x=36
if x < 2:
    print(x)

left, right = 0, x
while left < right:
    mid = left + (right - left) // 2
    square = mid * mid

    if square == x:
        print(mid)
        break
    elif square < x:
        left = mid + 1
    else:
        right = mid

print(left - 1)