import pandas as pd

### Part One ###
# get input
df_input = pd.read_csv("input.txt", sep = '   ', header = None)

left_list = df_input[0].to_list()
right_list = df_input[1].to_list()

# sort lists
left_list.sort()
right_list.sort()

# create dataframe from lists
df_result = pd.DataFrame({"left_list": left_list,
                          "right_list": right_list})

# calculate distance
df_result["distance"] = abs(df_result["left_list"] - df_result["right_list"])
total_distance = df_result["distance"].sum()

print(f"Answer: The total distance between my lists is {total_distance}.")

### Part Two ###

total_similarity_score = 0

for element in left_list:
    cnt = right_list.count(element)
    total_similarity_score += element * cnt

print(f"Answer: The similarity score of my lists is {total_similarity_score}.")