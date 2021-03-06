# Project 3

## Question 1

After importing the Charleston asking price data, I set beds, baths, and square feet as the features and asking price as the target. I then used a for loop and the kfold method from sklearn to separate the data into 10 even folds (roughly 70 entries per fold). The majority of data is used to train the model and then the remaining testing data is reserved for applying the model to see how well it performs on novel data, which helps prevent overfitting. The training score thus serves as a measure of internal validity because it is based on how the model behaves with data from the sample and the testing score serves as a measure of external validity because it tests how effectively the model assesses new data. I got a training score of 0.019 and a testing score of -0.066. I am still not entirely sure how an R squared value can be negative but these are very low values, which indicates a poorly fit model. A perfectly fit model would have an R squared score of 1, so there is lots of room for improvement.

## Question 2

The next step toward improving this model was standardizing the features. I used StandardScaler.fit_transform(X) to standardize beds, baths, and square feet. I then ran the kfold loop again using 10 folds and the standardized X values. Using standardization should theoretically improve the R squared value for the model because it increases the consistancy of the variables' format and content. However, there wasn't a huge improvement here. The training score after standardization was 0.012 and the testing score was 0.028. This is a slight improvement because the testing score is no longer negative, but these values are still pretty low. Only 1-2% of the varaition in the data is explained by the model in this case.

## Question 3

Next I used a ridge regression model to fit the data. I used an alph arange of 0 to 100, which yielded an optimal alpha level of 100. The alpha value is meant to reduce the cost function by adding a regularization term, which should reduce model complexity and prevent overfitting. I still got very small values for training and testing scores, 0.019 and -0.036 respectively. This indicates a poorly fit model and not much improvement from the other two methods. I looked at the graphs for #of folds and R squared, which showed that this method does produce more consistent testing scores compared to the other two methods but the model still doesn't seem to have much predictive value.

## Question 4

I repeated the previous steps with the Charleston selling price data (still using 10 folds). For the linear regression model I got a training score of 0.004 and a testing score of -0.015. After standardizing the data with sklearn StandardScaler(), I got a training score of 0.004 and a testing score of -0.019. With the last technique of using the ridge regression, the training score was still only 0.004 and the test score was -0.055. These values don't show much improvement from one technique to the next. The scores are all very low, which indicates they aren't explainign a lot of the variance in the data. This could be because asking and actual selling price both vary by arbitrary factors like zipe code, which is accounted for below.

## Question 5

Next I added zip code as another feature to test if this would improve the predictive power of the model. This yielded much better results for all three trials, likely because homes of similar size can vary greatly depending on their location/neighborhood. The results for each trial are shown below.

Linear Regression  
Training R squared: 0.333  
Testing R squared: 0.208  

Standardization  
Training R squared: 0.335  
Testing R squared: 0.302  

Ridge Regression  
Training R squared: 0.333  
Testing R squared: 0.219  

The standardization method had the highest training and testing scores in this case, accounting for a little over 30% of the variance in the data in both training and testing. This still isn't ideal but definitely a big improvement from the previous attempts that don't take zip code into account.

## Question 6

THe model that produced the best results was the standardized model because it had the highest internal and external validity (training and testing scores). This mdoel is still far from perfect and appears to be a little overfit because the training score is higher than the testing score, indicating the model performed better with data it encountered during training than with new testing data. In order to further improve the predictive power of this model I would recommend looking at neighborhood data and looking for factors aside from the houses's general specifications that might influence price. Are there ammenities nearby? Does the neighborhood have a housing association to provide services? Is the home in a safe location? Is the home in good condition? How big/well kept is the yard? These are some things (among many others) that could affect the price of a home and should be taken into account when trying to predict the price. Simply using size and number of beds and baths alone isn't a very accurate predictor.



