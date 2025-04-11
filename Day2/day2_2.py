
# Read the input file
<<<<<<< HEAD
file = open(r'C:\Users\joshu\Documents\AoC\Day2\d2input.txt')

=======
file = open(r'C:\Users\Joshu\Documents\Python_projects\AoC\AoC\Day2\d2input.txt')
>>>>>>> 0af27a358fe1b2303f673281d4357e8c212b900e

safe_count = 0

for report in file:
    
    # Initialise condition flags
    is_safe = True
    ascending = False
    descending = False
    problem = 0

    # create problem dampener counter
    problem_dampener = True
    is_damp_safe = True
    dampened_level = 0
    d_ascending = False
    d_descending = False

    # convert text line to list of integers
    levels = list(map(int, report.split()))
    dampened_levels = levels.copy()

    # Create previous level comparison to first level
    prev_level = levels[0]

    for level in levels[1:]:
        diff = level - prev_level

        if not (1 <= abs(diff) <=3):
<<<<<<< HEAD

            if problem_dampener == True:
                problem_dampener = False
                dampened_level = level
                break 
                            
            is_safe = False
=======
            # is_safe = False
            problem += 1
>>>>>>> 0af27a358fe1b2303f673281d4357e8c212b900e

        if diff > 0:
            ascending = True
        elif diff < 0:
            descending = True


        if ascending and descending:
<<<<<<< HEAD

            if problem_dampener == True:
                problem_dampener = False
                dampened_level = level
                break

            is_safe = False
        
        prev_level = level

    if not problem_dampener:
        dampened_levels.remove(dampened_level)
        prev_level = dampened_levels[0]

        for level in dampened_levels[1:]:
            diff = level - prev_level

            if not (1 <= abs(diff) <=3):
                is_damp_safe = False

            if diff > 0:
                d_ascending = True
            elif diff < 0:
                d_descending = True

            if d_ascending and d_descending:
                is_damp_safe = False
            
            prev_level = level

    if is_damp_safe:
=======
            problem += 1
            # is_safe = False
        
        prev_level = level

    if problem < 2:
>>>>>>> 0af27a358fe1b2303f673281d4357e8c212b900e
        safe_count += 1

print(safe_count)

file.close()
