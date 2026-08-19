def perfectNums(start, end):
    for num in range(start, end + 1):
        if num == 0:
            print(num) 
            continue
        
        sum_divisors = 0
        for i in range(1, num):
            if num % i == 0:
                sum_divisors += i
        
        if sum_divisors == num and num != 0:
            print(num)


perfectNums(0, 100)