#pyramid card pattern
def CardsPyramid(n):
    if n == 0:
        return -1
    
    total_cards = 2  # Cards required to build a pyramid of level 1
    for level in range(2, n+1):
        cards_for_level = 2 + 3 * (level - 1)
        total_cards += cards_for_level
        
    return total_cards % 1000007

# Test the function
n = int(input())  # Enter the value of 'n'
result = CardsPyramid(n)
print(result)

#pyramid card pattern

def noOfCards(n):

    return n * (3 * n + 1) // 2
 
# Driver Code

n = int(input())

print(noOfCards(n))
