#!/usr/bin/env python
# coding: utf-8

# In[1]:


import geopandas as gpd
import matplotlib.pyplot as plt

# Load Virginia counties and districts GeoJSON file
va_geojson_file = "va_counties_cd118_2022.geojson"
gdf = gpd.read_file(va_geojson_file)

# Create a plot
fig, ax = plt.subplots(figsize=(12, 12))

# Plot congressional districts with different colors
gdf[gdf['CD118FP'] != 0].plot(ax=ax, column='CD118FP', cmap='tab20', legend=True, legend_kwds={'loc': 'upper left'})

# Set plot title
ax.set_title("Virginia Counties and Congressional Districts 2022")

# Display the plot
plt.axis('off')
plt.show()


# In[2]:


import geopandas as gpd

# Load Virginia counties and districts GeoJSON file
va_geojson_file = "va_counties_cd118_2022.geojson"
gdf = gpd.read_file(va_geojson_file)

# Count the number of unique GeoIDs
unique_geoids = gdf['GEOID'].nunique()

print("Number of unique GeoIDs:", unique_geoids)


# In[3]:


import geopandas as gpd

# Load Virginia counties and districts GeoJSON file
va_geojson_file = "va_counties_cd118_2022.geojson"
gdf = gpd.read_file(va_geojson_file)

# Count the number of unique GeoIDs
unique_counties = gdf['COUNTYFP'].nunique()

print("Number of unique Counties:", unique_counties)


# In[4]:


import geopandas as gpd

# Load Virginia counties and districts GeoJSON file
va_geojson_file = "va_counties_cd118_2022.geojson"
gdf = gpd.read_file(va_geojson_file)

# Group the data by the 'COUNTYFP' and count the unique district values
county_district_counts = gdf.groupby('COUNTYFP')['CD118FP'].nunique()

# Check if any county is in multiple districts
counties_in_multiple_districts = county_district_counts[county_district_counts > 1]

# Print the counties that are in multiple districts
if not counties_in_multiple_districts.empty:
    print("Counties in multiple districts:")
    print(counties_in_multiple_districts)
else:
    print("All counties are in a single district.")


# In[5]:


import geopandas as gpd

# Load the GeoJSON file
geojson_file = "va_counties_cd118_2022.geojson"
gdf = gpd.read_file(geojson_file)

# Check the unique values in the 'CD118FP' column to identify congressional districts
congressional_districts = gdf['CD118FP'].unique()

# Create a dictionary to store counties in each congressional district
counties_in_districts = {district: [] for district in congressional_districts}

# Iterate through the GeoDataFrame and populate the dictionary
for index, row in gdf.iterrows():
    district = row['CD118FP']
    county_fp = row['COUNTYFP']
    counties_in_districts[district].append(county_fp)

# Print the counties in each congressional district
for district, counties in counties_in_districts.items():
    print(f"2022 Congressional District {district}: {', '.join(counties)}")


# In[6]:


import geopandas as gpd

# Load the GeoJSON file
geojson_file = "va_counties_cd118_2022.geojson"
gdf = gpd.read_file(geojson_file)

# Update 'CD118FP' where 'COUNTYFP' is 'nnn' to 'mm'
gdf.loc[gdf['COUNTYFP'] == '013', 'CD118FP'] = '08'
gdf.loc[gdf['COUNTYFP'] == '510', 'CD118FP'] = '08'
gdf.loc[gdf['COUNTYFP'] == '153', 'CD118FP'] = '08'
gdf.loc[gdf['COUNTYFP'] == '683', 'CD118FP'] = '08'
gdf.loc[gdf['COUNTYFP'] == '685', 'CD118FP'] = '08'
gdf.loc[gdf['COUNTYFP'] == '059', 'CD118FP'] = '11'
gdf.loc[gdf['COUNTYFP'] == '600', 'CD118FP'] = '11'
gdf.loc[gdf['COUNTYFP'] == '610', 'CD118FP'] = '11'
gdf.loc[gdf['COUNTYFP'] == '061', 'CD118FP'] = '11'
gdf.loc[gdf['COUNTYFP'] == '003', 'CD118FP'] = '05'
gdf.loc[gdf['COUNTYFP'] == '540', 'CD118FP'] = '05'
gdf.loc[gdf['COUNTYFP'] == '109', 'CD118FP'] = '05'
gdf.loc[gdf['COUNTYFP'] == '113', 'CD118FP'] = '05'
gdf.loc[gdf['COUNTYFP'] == '047', 'CD118FP'] = '05'
gdf.loc[gdf['COUNTYFP'] == '079', 'CD118FP'] = '05'
gdf.loc[gdf['COUNTYFP'] == '137', 'CD118FP'] = '05'
gdf.loc[gdf['COUNTYFP'] == '139', 'CD118FP'] = '05'
gdf.loc[gdf['COUNTYFP'] == '157', 'CD118FP'] = '05'
gdf.loc[gdf['COUNTYFP'] == '019', 'CD118FP'] = '09'
gdf.loc[gdf['COUNTYFP'] == '161', 'CD118FP'] = '09'
gdf.loc[gdf['COUNTYFP'] == '770', 'CD118FP'] = '09'
gdf.loc[gdf['COUNTYFP'] == '775', 'CD118FP'] = '09'
gdf.loc[gdf['COUNTYFP'] == '197', 'CD118FP'] = '09'
gdf.loc[gdf['COUNTYFP'] == '021', 'CD118FP'] = '09'
gdf.loc[gdf['COUNTYFP'] == '520', 'CD118FP'] = '09'
gdf.loc[gdf['COUNTYFP'] == '027', 'CD118FP'] = '09'
gdf.loc[gdf['COUNTYFP'] == '051', 'CD118FP'] = '09'
gdf.loc[gdf['COUNTYFP'] == '640', 'CD118FP'] = '09'
gdf.loc[gdf['COUNTYFP'] == '071', 'CD118FP'] = '09'
gdf.loc[gdf['COUNTYFP'] == '077', 'CD118FP'] = '09'
gdf.loc[gdf['COUNTYFP'] == '105', 'CD118FP'] = '09'
gdf.loc[gdf['COUNTYFP'] == '720', 'CD118FP'] = '09'
gdf.loc[gdf['COUNTYFP'] == '155', 'CD118FP'] = '09'
gdf.loc[gdf['COUNTYFP'] == '750', 'CD118FP'] = '09'
gdf.loc[gdf['COUNTYFP'] == '167', 'CD118FP'] = '09'
gdf.loc[gdf['COUNTYFP'] == '169', 'CD118FP'] = '09'
gdf.loc[gdf['COUNTYFP'] == '173', 'CD118FP'] = '09'
gdf.loc[gdf['COUNTYFP'] == '185', 'CD118FP'] = '09'
gdf.loc[gdf['COUNTYFP'] == '191', 'CD118FP'] = '09'
gdf.loc[gdf['COUNTYFP'] == '195', 'CD118FP'] = '09'
gdf.loc[gdf['COUNTYFP'] == '035', 'CD118FP'] = '09'
gdf.loc[gdf['COUNTYFP'] == '063', 'CD118FP'] = '09'
gdf.loc[gdf['COUNTYFP'] == '121', 'CD118FP'] = '09'
gdf.loc[gdf['COUNTYFP'] == '141', 'CD118FP'] = '09'
gdf.loc[gdf['COUNTYFP'] == '031', 'CD118FP'] = '06'
gdf.loc[gdf['COUNTYFP'] == '680', 'CD118FP'] = '06'
gdf.loc[gdf['COUNTYFP'] == '147', 'CD118FP'] = '06'
gdf.loc[gdf['COUNTYFP'] == '007', 'CD118FP'] = '06'
gdf.loc[gdf['COUNTYFP'] == '011', 'CD118FP'] = '06'
gdf.loc[gdf['COUNTYFP'] == '029', 'CD118FP'] = '06'
gdf.loc[gdf['COUNTYFP'] == '037', 'CD118FP'] = '06'
gdf.loc[gdf['COUNTYFP'] == '049', 'CD118FP'] = '06'
gdf.loc[gdf['COUNTYFP'] == '590', 'CD118FP'] = '06'
gdf.loc[gdf['COUNTYFP'] == '065', 'CD118FP'] = '06'
gdf.loc[gdf['COUNTYFP'] == '075', 'CD118FP'] = '06'
gdf.loc[gdf['COUNTYFP'] == '083', 'CD118FP'] = '06'
gdf.loc[gdf['COUNTYFP'] == '089', 'CD118FP'] = '06'
gdf.loc[gdf['COUNTYFP'] == '111', 'CD118FP'] = '06'
gdf.loc[gdf['COUNTYFP'] == '690', 'CD118FP'] = '06'
gdf.loc[gdf['COUNTYFP'] == '117', 'CD118FP'] = '06'
gdf.loc[gdf['COUNTYFP'] == '135', 'CD118FP'] = '06'
gdf.loc[gdf['COUNTYFP'] == '143', 'CD118FP'] = '06'
gdf.loc[gdf['COUNTYFP'] == '145', 'CD118FP'] = '06'
gdf.loc[gdf['COUNTYFP'] == '165', 'CD118FP'] = '06'
gdf.loc[gdf['COUNTYFP'] == '005', 'CD118FP'] = '06'
gdf.loc[gdf['COUNTYFP'] == '009', 'CD118FP'] = '06'
gdf.loc[gdf['COUNTYFP'] == '015', 'CD118FP'] = '06'
gdf.loc[gdf['COUNTYFP'] == '017', 'CD118FP'] = '06'
gdf.loc[gdf['COUNTYFP'] == '023', 'CD118FP'] = '06'
gdf.loc[gdf['COUNTYFP'] == '530', 'CD118FP'] = '06'
gdf.loc[gdf['COUNTYFP'] == '580', 'CD118FP'] = '06'
gdf.loc[gdf['COUNTYFP'] == '045', 'CD118FP'] = '06'
gdf.loc[gdf['COUNTYFP'] == '660', 'CD118FP'] = '06'
gdf.loc[gdf['COUNTYFP'] == '091', 'CD118FP'] = '06'
gdf.loc[gdf['COUNTYFP'] == '678', 'CD118FP'] = '06'
gdf.loc[gdf['COUNTYFP'] == '125', 'CD118FP'] = '06'
gdf.loc[gdf['COUNTYFP'] == '163', 'CD118FP'] = '06'
gdf.loc[gdf['COUNTYFP'] == '790', 'CD118FP'] = '06'
gdf.loc[gdf['COUNTYFP'] == '820', 'CD118FP'] = '06'
gdf.loc[gdf['COUNTYFP'] == '041', 'CD118FP'] = '04'
gdf.loc[gdf['COUNTYFP'] == '570', 'CD118FP'] = '04'
gdf.loc[gdf['COUNTYFP'] == '053', 'CD118FP'] = '04'
gdf.loc[gdf['COUNTYFP'] == '730', 'CD118FP'] = '04'
gdf.loc[gdf['COUNTYFP'] == '087', 'CD118FP'] = '04'
gdf.loc[gdf['COUNTYFP'] == '760', 'CD118FP'] = '04'
gdf.loc[gdf['COUNTYFP'] == '057', 'CD118FP'] = '01'
gdf.loc[gdf['COUNTYFP'] == '036', 'CD118FP'] = '01'
gdf.loc[gdf['COUNTYFP'] == '097', 'CD118FP'] = '01'
gdf.loc[gdf['COUNTYFP'] == '099', 'CD118FP'] = '01'
gdf.loc[gdf['COUNTYFP'] == '101', 'CD118FP'] = '01'
gdf.loc[gdf['COUNTYFP'] == '103', 'CD118FP'] = '01'
gdf.loc[gdf['COUNTYFP'] == '115', 'CD118FP'] = '01'
gdf.loc[gdf['COUNTYFP'] == '119', 'CD118FP'] = '01'
gdf.loc[gdf['COUNTYFP'] == '127', 'CD118FP'] = '01'
gdf.loc[gdf['COUNTYFP'] == '133', 'CD118FP'] = '01'
gdf.loc[gdf['COUNTYFP'] == '159', 'CD118FP'] = '01'
gdf.loc[gdf['COUNTYFP'] == '193', 'CD118FP'] = '01'
gdf.loc[gdf['COUNTYFP'] == '095', 'CD118FP'] = '01'
gdf.loc[gdf['COUNTYFP'] == '830', 'CD118FP'] = '01'
gdf.loc[gdf['COUNTYFP'] == '199', 'CD118FP'] = '01'
gdf.loc[gdf['COUNTYFP'] == '650', 'CD118FP'] = '01'
gdf.loc[gdf['COUNTYFP'] == '700', 'CD118FP'] = '01'
gdf.loc[gdf['COUNTYFP'] == '735', 'CD118FP'] = '01'
gdf.loc[gdf['COUNTYFP'] == '067', 'CD118FP'] = '02'
gdf.loc[gdf['COUNTYFP'] == '149', 'CD118FP'] = '02'
gdf.loc[gdf['COUNTYFP'] == '670', 'CD118FP'] = '02'
gdf.loc[gdf['COUNTYFP'] == '183', 'CD118FP'] = '02'
gdf.loc[gdf['COUNTYFP'] == '025', 'CD118FP'] = '02'
gdf.loc[gdf['COUNTYFP'] == '595', 'CD118FP'] = '02'
gdf.loc[gdf['COUNTYFP'] == '620', 'CD118FP'] = '02'
gdf.loc[gdf['COUNTYFP'] == '081', 'CD118FP'] = '02'
gdf.loc[gdf['COUNTYFP'] == '093', 'CD118FP'] = '02'
gdf.loc[gdf['COUNTYFP'] == '175', 'CD118FP'] = '02'
gdf.loc[gdf['COUNTYFP'] == '800', 'CD118FP'] = '02'
gdf.loc[gdf['COUNTYFP'] == '181', 'CD118FP'] = '02'
gdf.loc[gdf['COUNTYFP'] == '073', 'CD118FP'] = '03'
gdf.loc[gdf['COUNTYFP'] == '131', 'CD118FP'] = '03'
gdf.loc[gdf['COUNTYFP'] == '001', 'CD118FP'] = '03'
gdf.loc[gdf['COUNTYFP'] == '810', 'CD118FP'] = '03'
gdf.loc[gdf['COUNTYFP'] == '550', 'CD118FP'] = '03'
gdf.loc[gdf['COUNTYFP'] == '710', 'CD118FP'] = '03'
gdf.loc[gdf['COUNTYFP'] == '740', 'CD118FP'] = '03'
gdf.loc[gdf['COUNTYFP'] == '085', 'CD118FP'] = '07'
gdf.loc[gdf['COUNTYFP'] == '177', 'CD118FP'] = '07'
gdf.loc[gdf['COUNTYFP'] == '033', 'CD118FP'] = '07'
gdf.loc[gdf['COUNTYFP'] == '630', 'CD118FP'] = '07'
gdf.loc[gdf['COUNTYFP'] == '179', 'CD118FP'] = '07'
gdf.loc[gdf['COUNTYFP'] == '107', 'CD118FP'] = '10'
gdf.loc[gdf['COUNTYFP'] == '043', 'CD118FP'] = '10'
gdf.loc[gdf['COUNTYFP'] == '069', 'CD118FP'] = '10'
gdf.loc[gdf['COUNTYFP'] == '840', 'CD118FP'] = '10'
gdf.loc[gdf['COUNTYFP'] == '171', 'CD118FP'] = '10'
gdf.loc[gdf['COUNTYFP'] == '187', 'CD118FP'] = '10'

# Save the updated GeoDataFrame to a new GeoJSON file
updated_geojson_file = "va_counties_redistricted.geojson"
gdf.to_file(updated_geojson_file, driver='GeoJSON')


# In[7]:


import geopandas as gpd
import matplotlib.pyplot as plt

# Load Virginia counties and districts GeoJSON file
va_geojson_file = "va_counties_redistricted.geojson"
gdf = gpd.read_file(va_geojson_file)

# Create a plot
fig, ax = plt.subplots(figsize=(12, 12))

# Plot congressional districts with different colors
gdf[gdf['CD118FP'] != 0].plot(ax=ax, column='CD118FP', cmap='tab20', legend=True, legend_kwds={'loc': 'upper left'})

# Set plot title
ax.set_title("Virginia Counties Redistricted")

# Display the plot
plt.axis('off')
plt.show()


# In[ ]:




