# Reversing a list using reversed() 
#def Reverse(lst): 
	#return [ele for ele in reversed(lst)] 
	
# Driver Code 
lst = [10, 11, 12, 13, 14, 15] 
 
print(reversed(lst)) 

# Reversing a list using reverse() 
def Reverse(lst): 
	lst.reverse() 
	return lst 
print(Reverse(lst))	
lst = [10, 11, 12, 13, 14, 15] 
print(Reverse(lst)) 
