
# Read the input file
file = open(r'C:\Users\Joshu\Documents\Python_projects\AoC\AoC\Day2\d2input.txt')

safe_count = 0

for report in file:
    
    # Initialise condition flags
    is_safe = True
    ascending = False
    descending = False
    problem = 0


    # convert text line to list of integers
    levels = list(map(int, report.split()))

    # Create previous level comparison to first level
    prev_level = levels[0]

    for level in levels[1:]:
        diff = level - prev_level

        if not (1 <= abs(diff) <=3):
            # is_safe = False
            problem += 1

        if diff > 0:
            ascending = True
        elif diff < 0:
            descending = True

        if ascending and descending:
            problem += 1
            # is_safe = False
        
        prev_level = level

    if problem < 2:
        safe_count += 1

print(safe_count)

file.close()
