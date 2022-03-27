'''
Levenshtein Edit Distance
The levenshtein distance calculates the number of steps (insertions, deletions or substitutions) required to go from source string to target string.
'''
def lev_distance(source='', target=''):
    """Make a Levenshtein Distances Matrix"""
    
    # get length of both strings
    n1, n2 = len(source), len(target)
    
    # create matrix using length of both strings - source string sits on columns, target string sits on rows
    matrix = [ [ 0 for i1 in range(n1 + 1) ] for i2 in range(n2 + 1) ]
    
    # fill the first row - (0 to n1-1)
    for i1 in range(1, n1 + 1):
        matrix[0][i1] = i1
    
    # fill the first column - (0 to n2-1)
    for i2 in range(1, n2 + 1):
        matrix[i2][0] = i2
    
    # fill the matrix
    for i2 in range(1, n2 + 1):
        for i1 in range(1, n1 + 1):
            
            # check whether letters being compared are same
            if (source[i1-1] == target[i2-1]):
                value = matrix[i2-1][i1-1]               # top-left cell value
            else:
                value = min(matrix[i2-1][i1]   + 1,      # left cell value     + 1
                            matrix[i2][i1-1]   + 1,      # top cell  value     + 1
                            matrix[i2-1][i1-1] + 1)      # top-left cell value + 1
            
            matrix[i2][i1] = value
    
    # return bottom-right cell value
    return matrix[-1][-1]

print(lev_distance('cat','cta'))

# Levenshtein distance in nltk library
# import library
from nltk.metrics.distance import edit_distance
dist= edit_distance("apple", "appel")
print("Levenshtein Distance NLTK:", dist)

# Damerau-Levenshtein Distance¶
# The Damerau-Levenshtein distance allows transpositions 
# (swap of two letters which are adjacent to each other) as well.
tran_dist = edit_distance("perspective", "prospective", transpositions=False)
print("Damerau-Levenshtein Distance:",tran_dist)