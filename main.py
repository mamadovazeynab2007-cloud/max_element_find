def find_max(numbers):
    if not numbers:
        return "Xəta: Massiv boşdur!"
    
    max_element = numbers[0]
    for num in numbers:
        if num > max_element:
            max_element = num
    return max_element
