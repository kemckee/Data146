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
I then appended the ridge training, testing, and MSE data to the appropriate array and took the mean of these values to arrive at the R squared value. The combination of creating these new arrays and using the whole dataset rather than just the MedInc data corrected this problem. I also wasn't totally sure on how to get the alpha value itself, so I fixed that by using the argmax value for all of the values tested in the alpha range given in the question, which yielded an ideal alpha of 25.8 (the first value in the print line below).

```python
idx = np.argmax(rid_te)
print(rid_a_range[idx], rid_tr[idx], rid_te[idx], rid_tr_mse[idx], rid_te_mse[idx])
```

## Question 20

For the lasso regression I made different empty arrays, but I was still using the MedInc data because of an issue with different X variables all over the place. I fixed this by including the whole dataset, which yielded a mean R squared value of 0.60213 for the lasso regression. I also believe I had some issues getting the exact right value for alpha, which I corrected similarly to question 19 by using np.argmax to find the index of alpha. Plotting the graph this time also helped me see where the maximum value of R squared was so I could confirm the correct alpha.

## Question 22

I used the DoKFold values rather than looking at a simple standardized and fit model for each type of regression. I thought this question was a lot harder than it really is and again there seemed to be soem mixed up X vs X_var variables in there that were messing up these values. I used the following code to first set the alphas to those determined in previous questions and define the regression functions as objects. I then fit each model using the standardized X values (Xs) and got the coefficient for each type of regression for only the MedInc variable (which is the most correlated) using index 0 because it is the first feature in the dataframe. 

```python
lin = LR(); rid = Ridge(alpha = 25.8); las = Lasso(alpha = 0.00186)
lin.fit(Xs,y); rid.fit(Xs,y); las.fit(Xs,y)
lin.coef_[0], rid.coef_[0], las.coef_[0]
```
This yielded coefficients of 0.82961930428045, 0.8288892465528181, and 0.8200140807502059 for the linear, ridge, and lasso regressions respectively. Based on this analysis the Lasso regression estimates the smallest coefficient for MedInc.

## Question 23

For some reason I tried to use the DoKFold function instead of just fitting the models using model.coef_[], which yielded values that were very similar to one another but lasso was the lowest. I answered that two or more were the same because I wasn't sure how much to round. I cleaned up the code for this question and it is posted in the file below.

## Question 24

I ran into a similar problem here as I did in question 19 because I wasn't totally sure how to get the value for alpha. I found a problem in my DoKFold function that was producing really really small values for average MSE, so I fixed that problem by replacing the original statement I used to append the MSE with the following code:

```python
train_mse.append(np.square(np.subtract(ytrain, ytrain_pred)).mean())
test_mse.append(np.square(np.subtract(ytest, ytest_pred)).mean())
```
This makes all of the operations very clear to me, which helped remedy the error I was getting in the function that I beleive was due to a problem with order of operations. The values were being squared and averaged in the wrong order because of some missed parentheses.  

## Revised Script: 
