# Project 5.1

## WealthC Analysis

For the first set of tests I set WealthC as the target and the rest of the dataset (excluding WealthC and WealthI) as the features. I removed the NaN data, which only constituted 83 out of over 47,000 values so doing so didn't introduce a big risk of biasing the dataset.  

The first test I ran was a linear regression, which yielded training and testing R squared values of 0.7358365784782854 and 0.7350536560539934 respectively. The mean squared error was 0.4437568673467586 for the testing data and 0.4427858616687968 for the training data. Next, I standardized teh results using StandardScaler by changing the standardize argument in the KFold function to True, which produced very similar results. Standardizing the data yielded a training R squared of 0.7358196018893879 and a testing R squared of 0.7350372348316933. These values are actually slightly lower than the non-standardized ones but only if they're compared out to the 5th decimal place and beyond, so there isn't functionally a large difference between them. The MSE for the standardized data was also very similar. The training MSE was 0.44281428271086326 and the testing MSE was 0.4437849039355669 and these values are extremely close to the non-standardized MSE values.



0.00026333333333333336 0.7358346356402806 0.7350562589633233
