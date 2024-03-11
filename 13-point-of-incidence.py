with open('13-point-of-incidence-input.txt') as input:

    def find_horizontal_incidence(pattern):
        i = 0
        j = 1

        incidences = []
        while j < len(pattern):
            if pattern[i] == pattern[j]:
                incidences.append((i, j))
            i += 1
            j += 1
        
        for incidence in incidences:   
            found_horizontal_incidence = True
            m = incidence[0]
            n = incidence[1]
            while m >= 0 and n < len(pattern):
                if pattern[m] != pattern[n]:
                    found_horizontal_incidence = False
                    break
                m -= 1
                n += 1

            if found_horizontal_incidence:
                return incidence[1]

        return 0
        
    def find_vertical_incidence(pattern):
        i = 0
        j = 1

        incidences = []

        while j < len(pattern[0]):
            if all(pattern[k][i] == pattern[k][j] for k in range(len(pattern))):
                incidences.append((i,j))
            i += 1
            j += 1
        
        
        for incidence in incidences:
            found_vertical_incidence = True
            m = incidence[0]
            n = incidence[1]   
            while m >= 0 and n < len(pattern[0]) and found_vertical_incidence:
                if not all(pattern[row][m] == pattern[row][n] for row in range(len(pattern))):
                    found_vertical_incidence = False
                m -= 1
                n += 1
            
            if found_vertical_incidence:
                return incidence[1]
        
        return 0

    def find_incidence(pattern):
        rows = find_horizontal_incidence(pattern)
        if rows > 0:
            return rows * 100

        return find_vertical_incidence(pattern)

    pattern = []
    summary = 0
    for line in input:        
        if line == '\n':
            summary += find_incidence(pattern)
            pattern = []
        else:
            pattern.append(line.strip())

    
    summary += find_incidence(pattern)
    
    print(summary)