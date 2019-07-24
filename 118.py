Daily Coding Problem #118
'''
Given a sorted list of integers, square the elements and give the output in sorted order.

For example, given [-9, -2, 0, 2, 3], return [0, 4, 4, 9, 81].
'''
'''
IDEA: 

The given list is sorted already. So divided elements into two lists: 1 for negatives and the other for positives.
Square the two lists, maintaining the order of the elements in ascending order. 
Then merge the two lists using a merge function in merge sort. 

This takes O(N) time. 
'''
def square_sort(lst): 
  negatives = [x for x in lst if x < 0]
  positives = [x for x in lst if x >= 0]

  negatives_square_sorted = [x**2 for x in reversed(negatives)]
  positives_square_sorted = [x**2 for x in positives]

  return _merge(negatives_square_sorted, positives_square_sorted)

def _merge(left, right): 
  result = [] 
  i = j = 0 

  while i < len(left) and j < len(right): 

    if left[i] < right[j]: 
      result.append(left[i])
      i += 1
    elif left[i] > right[j]: 
      result.append(right[j])
      j += 1
    else: 
      result.append(left[i])
      result.append(right[j])
      i += 1
      j += 1
  result.append(left[i:]) #append whatever left over in the left list
  result.append(right[j:]) #append whatever left over in the right list 
  return result
