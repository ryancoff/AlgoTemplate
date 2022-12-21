i,j,ans = 0,0,0
A=[]
N=len(A)

def invalid(arg):
  return False

for j in range(N):
  # CODE: use A[j] to update state which might make the window invalid
  while invalid(A,j,i):
    # When INVALID, keep shrinking the left edge 'i' until it's valid again
    i += 1
    # Update state using A[i] # 
  
  # The window [i,j] is the maximum window we've found so far.
  ans = max(ans, j-i+1) # +1 to include A[j]

# return ans

for j in range(N):
  # CODE: use A[j] to update state which might make the window invalid
  if invalid(A,j,i):
    # When INVALID, keep shrinking the left edge 'i' until it's valid again
    i += 1
    # Update state using A[i] # 

# return j - i + 1