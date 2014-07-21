def string_slice(s, a, b, c, d):
	return s[a:b+1] + " " + s[c:d+1]

if __name__ == '__main__':
    print string_slice("random string......", 69, 77, 152, 162)