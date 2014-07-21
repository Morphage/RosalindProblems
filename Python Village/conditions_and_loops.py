def sum_odd(a, b):
    sum = 0
    for n in range(a, b+1):
	    if n % 2 == 1:
		    sum += n
    return sum

if __name__ == '__main__':
    print sum_odd(4277, 8337)