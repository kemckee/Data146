# Project 1

## Question 1

A package is a collection of related modules that are often used together. A Library is a collection of packages. To make a package accessible in python one must first make sure it is available for the current project. To do this in Pycharm, click on python interpreter in preferences and hit the + in the bottom corner if the desired package does not already appear on the list. Add the package and return to the coding screen. An import statement is then used to make the modules from the package available in the program. For example, we have used pandas and numpy, which are imported with this line of code:

```python
import pandas
import numpy as np
```

Notice that an alias is used to import numpy. This allows us to use np in place of numpy in the code, which can save space and time when writing programs. 

## Question 2 

A python data frame is a colleciton of rows and columns that contain data. The columns represent different categories and each row represents one entry for all of those categories. Pandas is a particularly useful library for data frames because it contains lots of modules that can pull out individual pieces of data or provide information about the data frame as a whole. 

In order to read a file in a remote location, use the pandas.read_x() function, where x is the type of file. For example, you can use pandas.read_csv() for a csv file or pandas.read_excel() for an excel spreadsheet. It is important to specify the file type for it to be imported properly. It is also important to insert the path to the file as well as give the data frame a name in order to manipuate it further. 

For example, to import the gapminder file (located on my desktop) I would use these two lines of code:

``` python
path_to_data = '/Users/kellynmckee/Desktop/gapminder.tsv'
df = pd.read_csv(path_to_data, sep = '\t')
```
The first line sets the path to the document and the second line saves the data as a dataframe called df.

Notice that an additional argument is given to the function specifying the seperation of each peice of data. This is important because the default assumption is that the data is separated by commas. If this is not the case, it should be specified to facilitate smooth import. In this dataset the data is separated by tabs instead of commas, which is indicated by the sep = '\t'.

To see an overview of the data frame, use the df.describe() function. This will summarize and provide statistics for each column of data. To see how many rows and columns there are, use df.shape. This will return the number of rows followed by the number of columns. The output for the gapminder data set is (1704, 6). To see the actual names of the columns use df.columns. The rows can also be referred to as items and the columns referred to as properties.

## Question 3

It appears that the years in the gapminder data frame run in incrememnts of 5, with 1952 being the earliest and 2007 being the most recent. To make this data set more current, the years 2012 and 2017 should be added. Using the code below (testing multiple years) I found that there are 142 items for each year, so adding 2 more years would add a total of 284 new rows.

```python
idx_year = data['year'] == 2007
data[idx_year]
```

## Question 4

I used these three lines of code to get the entry with the lowest life expectancy.

```python
lifeExp_min = data['lifeExp'].min()
idx_min = data['lifeExp'] == lifeExp_min
data[idx_min]
```
This yielded an entry from Rwanda in 1992 with an average life expectancy of only 23.599 years. This low life expectancy was likely due to the genocide and civil war occurring in Rwanda at this time.

## Question 5

I first created the gdp variable by multiplying population by gdp per capita and created a new column with this information. I created a new dataframe by subsetting the dataframe to only include entries from France, Italy, Germany, and Spain from the year 2007. I then sorted the output by gdp using sort_values.

```python
data['gdp'] = data['pop'] * data['gdpPercap']
euro_data = data[(data['country'].isin(['Germany', 'Italy', 'France', 'Spain'])) & (data['year'] == 2007)]
euro_sorted = euro_data.sort_values('gdp', ascending = False)
```
The results are shown in the following table. 

| Country | Continent | Year | Population | GDP per Capita | GDP          |  
| ------- | --------- | ---- | ---------- | -------------- | ------------ |
| Germany | Europe    | 2007 | 82400996   | 32170.37442    | 2.650871e+12 |
| France  | Europe    | 2007 | 61083916   | 30470.01670    | 1.861228e+12 |
| Italy   | Europe    | 2007 | 58147733   | 28569.71970    | 1.661264e+12 |
| Spain   | Europe    | 2007 | 40448191   | 28821.06370    | 1.165760e+12 |

## Question 6

The & symbol is used in boolean expressions and returns true only if both statements are true. For example, this expression will result in a new dataframe containing only values for which both country = Europe and year = 2007.

```python
data_europe = data[(data['continent'] == 'Europe') & (data['year'] == 2007)]
```

This expression also illustrates the == operator. This operator is used to compare the equality of two items or values. In a boolean expression it will return true if the values are the same and false if they are not. In this case it returns all values in the dataframe for which the string in the continent column is equal to Europe and the value in the year column is equal to 2007. 

The | operator will return true in a boolean expression if one or both of the statements on either side of the operator is true. For example, the data frame below will contain all values from the gapminder data frame that either have a GDP per capita greater than or equal to 2000 or have Germany as the country listed. These values can overlap.

```python
data_gdp = data[(data['gdpPercap'] >= 2000) | (data['country'] == 'Germany')]
```
