if __name__ == '__main__':
    file = open("test.txt", "r")	
    for line_number, line in enumerate(file, start=1):
	    if line_number % 2 == 0:
		    print line,
    file.close()