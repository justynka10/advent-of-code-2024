# ### Part One ###

safe_reports = 0

with open("input.txt", 'r') as input:
    for line in input:
        report = [int(level) for level in line.split()]
        # check rules by checking differnecies between adjacent elements
        differencies = [report[i+1] - report[i] for i in range(len(report) - 1)]
        if(all(diff >= 1 and diff <= 3 for diff in differencies)):
            safe_reports += 1
        elif(all(diff <= -1 and diff >= -3 for diff in differencies)):      
            safe_reports += 1

print(f"Answer: Number of safe reports is {safe_reports}.")

### Part Two ###

# separate function to check base safety of one report;
def check_if_report_is_safe(differencies):

    if(all(diff >= 1 and diff <= 3 for diff in differencies)):
        return True
    elif(all(diff <= -1 and diff >= -3 for diff in differencies)):      
        return True

safe_reports = 0

with open("input.txt", 'r') as input:
    for line in input:
        report = [int(level) for level in line.split()]

        # check differnecies between adjacent elements like before
        differencies = [report[i+1] - report[i] for i in range(len(report) - 1)]
       
        if(check_if_report_is_safe(differencies)):
            safe_reports += 1
        # check The Problem Dampener rules by removing level by level
        else:              
            for idx in range(len(report)):
                report_new = [report[i] for i in range(len(report)) 
                              if i != idx]
                differencies = [report_new[i+1] - report_new[i] 
                                for i in range(len(report_new) - 1)]
                if(check_if_report_is_safe(differencies)):
                    safe_reports += 1
                    break

print(f"Answer: Number of safe reports is {safe_reports} now.")