def find_all(str, pattern):
    start = 0
    positions = []
    
    while True:
        start = str.find(pattern, start)
        
        if start == -1: 
            break
        
        positions.append(start)
        start += 1

    return positions

if __name__ == '__main__':
    s = "GATATATGCATATACTT"
    t = "ATAT"
    positions = find_all(s, t)

    for pos in positions:
        print pos + 1,