##################################################
# Name: Abygale Brien
# Collaborators: Quinn Varnell, QUAD, and CHAT GPT(https://chatgpt.com/c/671fc7fb-10fc-800f-b6a5-eeb057e1e902)
# Estimate of time spent (hr): 2 hours
##################################################

def is_magic_square(array:list[list[int]]) -> bool:
    n = len(array)  # Get the number of rows
    for row in array: # Check if all rows have the same length
        if len(row) != n:
            return False

    target_sum = sum(array[0]) # Calculate sum of first row

    # Check the sum of each row
    for i in range(n):
        if sum(array[i]) != target_sum:
            return False  # If any row sum doesn't match --> return False
        
        if sum(array[j][i] for j in range(n)) != target_sum:
            return False  # If any column sum doesn't match, return False

    # Check sum of the main diagonal
    if sum(array[i][i] for i in range(n)) != target_sum:
        return False  # If main diagonal sum does not match, return False
    
    # Check sum of the anti-diagonal
    if sum(array[i][n - 1 - i] for i in range(n)) != target_sum:
        return False  # If anti-diagonal sum does not match, return False

    return True  # if passed --> it's a wonderful magic square
    
small = [[8,1,6],[3,5,7],[4,9,2]]
print(is_magic_square(small))

