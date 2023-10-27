import pulp
import pandas as pd

max_district = 11
max_district_size = 133
counties = #List of Counties

def compactness(district):
    """
    Find the compactness of the district
    - by calculating the average distance between the counties in districts
    - will likely need to make a matrix and average across
    - could be good to make a matrix and then index into it
    """
    return #FILL
                
#create list of all possible districts
possible_districts = [tuple(c) for c in pulp.allcombinations(counties, 
                                        max_district_size)]

#create a binary variable to state that a district is used
x = pulp.LpVariable.dicts('district', possible_districts, 
                            lowBound = 0,
                            upBound = 1,
                            cat = pulp.LpInteger)

redistrict_model = pulp.LpProblem("Redistricting Model", pulp.LpMinimize)

redistrict_model += sum([compactness(district) * x[district] for district in possible_districts])

#specify the maximum number of districts
redistrict_model += sum([x[district] for district in possible_districts]) <= max_district, "Maximum_number_of_districts"


#A county can be assigned to one and only one district
for county in counties:
    redistrict_model += sum([x[district] for district in possible_districts
                                if county in district]) == 1, "Must_zone_%s"%county

    
redistrict_model.solve()

print "The choosen districts are out of a total of %s:"%len(possible_districts)
for district in possible_districts:
    if x[district].value() == 1.0:
        print district
