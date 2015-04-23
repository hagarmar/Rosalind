def insertion_sort(num,narr): # simple O(n^2) solution
	count_swap = 0 # init counter 
	for n in range(1,num): # go over all elements in arr except 1st
		k = n
		while k>0 and narr[k]<narr[k-1]: # go over all other elements, if not in order then sort
			narr[k-1], narr[k] = narr[k], narr[k-1] # swap
			k = k-1
			count_swap+=1
	return count_swap

# read file and 
def main(file_name):
	f = open(file_name, 'r')
	num = int(f.readline())
	narr = list(int(x) for x in f.readline().split())

	f.close()

	print insertion_sort(num,narr)