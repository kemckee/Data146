# Midterm Revisions

## Question 18

There are a lot of silly mistakes in my code for the midterm. I think the biggest thing I did wrong was failing to make the features and targets from the California Housing Dataset into a dataframe. I was just trying to work with the numpy arrays like we had in class a few times. This led to quite a few issues, mainly because I created a new variable X_var that was a slice of the dataset and so I had to modify the code to use X_var instead of X, but on top of that there was still the Xs variable which was the standardized X_var slice. I don't think I replaced them all properly because there were some issues with the X variables in particular.

For question 18 I rewrote my script and got a mean R squared value of 0.60198. Originally I got a lower value and I beleive this is because I mixed up the X variables and was still using the MedInc variable instead of the entire dataset. A running theme is that I made this code a lot more complicated than it should have been and ended up confusing myself with exteraneous variables and long, unnecessary chunks of code. I will definitely make an effort to simplify problems and conceptualize them before starting to code in the future to avoid this problem.

## Question 19

For this question I again believe I was still using the MedInc subset because my answer was around 0.47. I recalculated this value using the entire dataset and got a mean R squared value of 0.60201. I was also getting the same value for ridge regression as I did for linear regression and I believe this is because I forgot to change the (initially empty) arrays from the linear regression run to the ridge regression run. I created the arrays in the DoKFold function that looked like this:

```python
train_scores = []
test_scores = []
train_mse = []
test_mse = []
 ```
And I used these same array names when creating the ridge regression rather than creating new arrays to hold the ridge data. I corrected this problem and introduced 4 new arrays:
 
 ```python 
rid_tr = []
rid_te = []
rid_tr_mse = []
rid_te_mse = []
```
I then appended the ridge training, testing, and MSE data to the appropriate array and took the mean of these values to arrive at the R squared value. The combination of creating these new arrays and using the whole dataset rather than just the MedInc data corrected this problem.

