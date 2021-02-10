# Exercise 1: Population Data
 
**Question 1: Get a list of all the years in this data, without any duplicates. How many unique values are there, and what are they?**

I used the .unique() attribute to find the unique years in this data set, which returns an array containing the following 12 values: 
([1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007]) 

**Question 2: What is the largest value for population (pop) in this data? When and where did this occur?**

I first used the .max() attribute to find the maximum value in the population column. Next I used .loc to get the rest of the information for this entry. 

```python
max_pop = data['pop'].max()
max_pop_idx = data.loc[data['pop'] == max_pop].index[0]
print(data.loc[max_pop_idx])
```
