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
