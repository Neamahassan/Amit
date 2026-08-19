def perfectNums(start: int, end: int) -> list:
    """
    Finds and prints all perfect numbers within a given range [start, end].
    
    Args:
        start (int): The starting integer of the range.
        end (int): The ending integer of the range.
        
    Returns:
        list: An array containing all perfect numbers found in the range.
        
    Note:
        The function iterates through the range and checks for perfect numbers.
        It also handles the edge case of 0 as specified.
    """
    perfect_numbers = []
    
    for num in range(start, end + 1):
        if num == 0:
            print(num)
            perfect_numbers.append(num)
            continue
        
        sum_divisors = 0
        for i in range(1, num):
            if num % i == 0:
                sum_divisors += i
        
        if sum_divisors == num and num != 0:
            print(num)
            perfect_numbers.append(num)
    
    return perfect_numbers


if __name__ == "__main__":
    print("Testing perfectNums from 0 to 100:")
    result = perfectNums(0, 100)
    print("Array of perfect numbers:", result)