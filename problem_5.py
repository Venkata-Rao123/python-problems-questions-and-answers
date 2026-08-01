# decimal to binary 
def coronaForComputer(arr, spikes):
    result = []
    for num in arr: 
        new_value = num // (2 ** spikes)
        result.append(new_value)
    return result

# Example usage
print(coronaForComputer([1, 2, 3, 4, 5], 2))  
print(coronaForComputer([8, 16, 32], 3))  


