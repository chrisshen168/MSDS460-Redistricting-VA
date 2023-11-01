import pulp
import pandas as pd

counties_df = pd.read_csv('VA_counties_red_V2.csv')
counties_df = counties_df.reset_index()
counties_df.columns = counties_df.iloc[0]
counties_df = counties_df.drop(counties_df.index[0])
counties_df.head()

counties_df['Pop2023'] = counties_df['Pop2023'].astype("int")
counties_df['Lat'] = counties_df['Lat'].astype("float")
counties_df['Long'] = counties_df['Long'].astype("float")

max_district = 11
max_population = counties_df['Pop2023'].sum() * 0.15 #(counties_df['Pop2023'].sum() / 11) * 1.5
counties = counties_df['Name']

import statistics as stats

counties_Lat_Dic = dict(zip(counties_df.Name, counties_df.Lat))
counties_Long_Dic = dict(zip(counties_df.Name, counties_df.Long))
counties_Pop_Dic = dict(zip(counties_df.Name, counties_df.Pop2023))

def compactness(district):
    lat_list = list( map(counties_Lat_Dic.get, district) )
    long_list = list( map(counties_Long_Dic.get, district) )
    
    lat_sd = stats.stdev(lat_list)
    long_sd = stats.stdev(long_list)
    
    compact_score = lat_sd + long_sd
    
    return compact_score

def total_pop(district):
    pop_list = list( map(counties_Pop_Dic.get, district) )
    population = sum(pop_list)
    return population

from itertools import chain, combinations
min_len = 2
max_len = 3
possible_districts = list(chain.from_iterable(combinations(counties, i) for i in range(min_len, max_len+1)))
len(possible_districts)

#create a binary variable to state that a district is used
x = pulp.LpVariable.dicts('district', possible_districts, 
                            lowBound = 0,
                            upBound = 1,
                            cat = pulp.LpInteger)

redistrict_model = pulp.LpProblem("Redistricting Model", pulp.LpMinimize)

#specify the maximum number of districts
redistrict_model += sum([x[district] for district in possible_districts]) == max_district, "Maximum_number_of_districts"

#specify the population max
for district in possible_districts:
    redistrict_model += total_pop(district) * x[district] <= max_population, f"Max_people_in_{district}"

#A county can be assigned to one and only one district
for county in counties:
    redistrict_model += sum([x[district] for district in possible_districts if county in district]) == 1, "Must_zone_%s"%county

redistrict_model += sum([compactness(district) * x[district] for district in possible_districts])
print(redistrict_model)

redistrict_model.solve()
count_districts = 0
print("The choosen districts are out of a total of %s:"%len(possible_districts))
for district in possible_districts:
    if x[district].value() == 1.0:
        count_districts += 1
        print(district)


print(count_districts)
