#Dictionary Filtering Based on Conditions

# Example dictionary


# Filtering to retain scores >= 80
#filtered_scores = {name: score for name, score in scores.items() if score >= 80}
#print('Filtered Scores:', filtered_scores)

def filter(dic):
    new_dic={}
    for name, score in dic.items():
        if score >= 80:
            new_dic[name]= score
    return new_dic


scores = {'Sajib': 80, 'Khan': 70, 'Shohel': 90, 'Ryhan': 78}
res = filter(scores)
print(res)
