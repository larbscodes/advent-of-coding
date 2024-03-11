with open('13-point-of-incidence-input.txt') as input:

    def find_horizontal_incidence(pattern):
        i = 0
        j = 1

        incidences = []
        while j < len(pattern):
            smudges = 0
            for k in range(len(pattern[0])):
                if smudges > 1:
                    break
                if pattern[i][k] != pattern[j][k]:
                    smudges += 1

            if smudges <= 1:
                incidences.append((i, j))
            i += 1
            j += 1
        
        for incidence in incidences:
            smudges = 0
            m = incidence[0]
            n = incidence[1]
            while m >= 0 and n < len(pattern):
                for k in range(len(pattern[0])):
                    if pattern[m][k] != pattern[n][k]:
                        smudges += 1

                if smudges > 1:
                    break
                
                m -= 1
                n += 1

            if smudges == 1:
                return incidence[1]

        return 0
        
    def find_vertical_incidence(pattern):
        i = 0
        j = 1

        incidences = []
        while j < len(pattern[0]):
            smudges = 0
            for k in range(len(pattern)):
                if smudges > 1:
                    break
                if pattern[k][i] != pattern[k][j]:
                    smudges += 1

            if smudges <= 1:
                incidences.append((i, j))
            i += 1
            j += 1
        
        for incidence in incidences:
            smudges = 0
            m = incidence[0]
            n = incidence[1]
            while m >= 0 and n < len(pattern[0]):
                for k in range(len(pattern)):
                    if pattern[k][m] != pattern[k][n]:
                        smudges += 1

                if smudges > 1:
                    break
                
                m -= 1
                n += 1

            if smudges == 1:
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