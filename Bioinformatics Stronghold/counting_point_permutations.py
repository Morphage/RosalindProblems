import itertools

def hamming_distance(str1, str2):
    """ Generate list of boolean values, True when characters match
        and False otherwise. izip creates an iterator which means 
        the list is not built, and instead a function is returned, 
        which gives you the tuples one-by-one, so you only ever
        have a single tuple in memory. Since True=1 and False=0,
        we just sum up the list to find the number of non matching
        characters
    """
    return sum(a != b for a, b in itertools.izip(str1, str2))

if __name__ == '__main__':
    print hamming_distance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT")