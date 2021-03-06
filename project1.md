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

To see an overview of the data frame, use the df.describe() function. This will summarize and provide statistics for each column of data. To see how many rows and columns there are, use df.shape. This will return the number of rows followed by the number of columns. The output for the gapminder data set is (1704, 6). To see the actual names of the columns use df.columns. The rows can also be referred to as observations and the columns referred to as variables.

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

The & symbol evaluates a to true if both statements on either side of the operator are true. For example, this expression will result in a new dataframe containing only values for which both country = Europe and year = 2007. It's important to note that both statements have to be in parentheses or it may evaluate to false even when both are true. I'm not entirely sure why this is but it seems like it could lead to unnecessary problems because it evaluates to false instead of raising an error.

```python
data_europe = data[(data['continent'] == 'Europe') & (data['year'] == 2007)]
```

It's important to note that both statements have to be in parentheses or it may evaluate to false even when both are true. I'm not entirely sure why this is but it seems like it could lead to unnecessary problems because it evaluates to false instead of raising an error. For example, the following line of code would evaluate to false even though both statements are true.

```python
1 < 3 & 4 > 2 
```

Tge data_europe expression above also illustrates the == operator. This operator is used to compare the equality of two items or values. It will return true if the values are the same and false if they are not. In this case it returns all values in the dataframe for which the string in the continent column is equal to Europe and the value in the year column is equal to 2007. To show this with a more simple example, the following line of code will evaluate to true because the two strings are identical.

```python
'potato' == 'potato'
```

The | operator will return true if one or both of the statements's is true. For example, the data frame below will contain all values from the gapminder data frame that either have a GDP per capita greater than or equal to 2000 or have Germany as the country listed. These values can overlap.

```python
data_gdp = data[(data['gdpPercap'] >= 2000) | (data['country'] == 'Germany')]
```
The ^ operator is similar to the | operator, but it evaluates to true only when one of the statements is true. If the | symbol in the expression above is replaced with the ^ operator, the data set would be the same except it would not include values for which both the country is Germany and GDP per capita is greater than or equal to 2000.


## Question 7

The .loc() is a method used for selecting data based on data names or indices. For example, it can be used to find all entries that have some value in common. The following code would show only data from Afghanistan.

```python
data.loc[data.country == 'Afghanistan']
```

This method can also be used to extract consecutive rows in a data frame if you know their indicies. For example, the code below would show rows 10-15 of the dataframe. The values can be changed depending on which consecutive rows are desired. 

```python
data.loc[10:15]
```

The .iloc() method is also used for getting particular row/column data but it relies only on indices rather than column names or values. This method can be used to locate consecutive columns. If all rows are desired but only some consecutive columns, use the following code, where the range in the brackets indicates which consecutive columns are shown based on their indices.

```python
display(data.iloc[:, 2:6])
```

## Question 8

An API is a application programming interface. They are essentially remote servers that relay information to and from your code and the provider/website that hosts your data of interest. The API delivers your request to the provider and then sends back their response to you.

Importing data from an API into your workspace requires a few simple steps. 

1. Create a folder to store API data. 

Use the os library to create a new folder in your work space.

```python
data_folder = 'data'
if not os.path.exists(data_folder):
    os.makedirs(data_folder)
```

2. Create a .csv file and get the path to this file. 

Save the name of the new .csv file as an object and join this string to the data folder to get the path to the new .csv file in the folder created in the previous step. This file_name object should now contain the complete path to the .csv where the API data will be written.

```python
file_name = os.path.join(data_folder, file_name_short)
```

3. Write the contents of your API url into the .csv file. 

Save the API link as an object and use the get method from the requests library to retrieve the data and write it to the .csv called file_name.

```python
url = "https://api.covidtracking.com/v1/states/daily.csv"
r = requests.get(url)
with open(file_name, 'wb') as f:
    f.write(r.content)
```
    
4. Convert the .csv data into a dataframe with pandas.

Now that the data is written in a .csv in your work space, simply convert the data into a data frame using the pandas library.

```python
df = pd.read_csv(file_name)
```

## Question 9

Apply() is a pandas method that allows a function to be applied to all rows or all columns in a dataframe. It can be used for mathematical operations, changing the types of entries, and many other applications. Apply() is an alternative to using a loop to perform a function on every item in a dataframe. Apply() is prefereable to using a loop because it is faster as and improves the clarity of the code. Why use a three line for loop when the same command can be accomplished faster with a one line apply() method?

## Question 10

An alternative to using iloc to subset a data frame is to use set the columns equal to a subset of the existing columns. First save a list of the desired columns as an object. Next, set a new variable name equal to the dataframe with only those columns. This creates a new dataframe with only the columns listed in the cols list. It's a good idea to use df[cols].copy() rather than just using df[cols] because this prevents you from making undesired changes to the original data.

```python
cols = ['col1', 'col2','col3', 'col4']
df_filtered = df[cols].copy()
```

It's also possible to select specific consecutive columns by using data.columns[x:x] and setting the range to the columns of interest. For example, the following code would show only the country, continent, and year columns for the gapminder data frame.

```python
data[data.columns[0:3]]
```
The range can be changed to specify the desired columns and it can be saved as a new data frame by setting it equal to a variable name.
