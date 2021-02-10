# Exercise 1: Population Data
 
**Question 1: Get a list of all the years in this data, without any duplicates. How many unique values are there, and what are they?**

I used the .unique() attribute to find the unique years in this data set, which returns an array containing the following 12 values: 
([1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007]) 

**Question 2: What is the largest value for population (pop) in this data? When and where did this occur?**

I first used the .max() attribute to find the maximum value in the population column. Next I used .loc to get the rest of the information for the entry with the highest population value. The maximum population listed is 1318683096 describing China in 2007. 

```python
max_pop = data['pop'].max()
max_pop_idx = data.loc[data['pop'] == max_pop].index[0]
print(data.loc[max_pop_idx])
```

**Question 3: Extract all the records for Europe. In 1952, which country had the smallest population, and what was the population in 2007?**

I took out the year specification from the getdatabycont function we wrote in class and used this to isolate the values from Europe. 

```python
def getdatabycont(data, continent):
    indxCont = data['continent'] == continent
    temp = data[indxCont]
    return temp
```

I used this function to create a new dataframe called euro_data and further subsetted this data frame to contain only values from 1952. I then took the minimum population value from this data frame using the .min() attribute and found that Iceland had the smallest population in Europe in 1952. 

```python
euro_52 = euro_data[euro_data['year'] == 1952]
euro_52[euro_52['pop'] == euro_52['pop'].min()]
```

Finally, I used the original euro_data dataframe to find Iceland's population in 2007. I just subsetted the dataframe to specify Iceland as the country, 2007 as the year, and pop as the column, which returned the population of 301931.

```python
ice_data = euro_data[euro_data['country'] == 'Iceland']
ice_data[ice_data['year'] == 2007]['pop']
```
