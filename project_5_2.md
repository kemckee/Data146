# Project 5.2

## Qeustion 1

First I imported the city persons CSV file, removed NaN values, and changed education and age to integers. Next I set X to everything except WealthC and y equal to WealthC. 

For the K nearest neighbors test I used a narrowed in on a range from 70 to 80 for k. From this range the best value of k was 72, which yielded a testing score of 0.5622254758418741, which was very close to the training score and indicates the model was not overfit. I then ran the same analysis after adding weights = distance, which returned a best k value of 73 and a testing score of 0.5012201073694486. This is slightly lower than the unweighted testing score but fairly similar. 

## Question 2

Next I implemented a logistic regression using WealthC as the target to see how this compared to the KNN output. The logistic regression yielded a training score of 0.548828125 and a testing score of 0.5436798438262567. These scores are slightly lower than the unweighted KNN model but the training and testing scores are very close which again indicated the model is not overfit.

## Question 3

Next I used a random forest with 100, 500, 1000, and 5000 estimators using both the raw and scaled data.

Raw data training and testing values:  
100 trees: [0.7890625, 0.5012201073694486]  
500 trees: [0.7890625, 0.509028794533919]  
1000 trees: [0.7890625, 0.49829184968277207]  
5000 trees: [0.7890625, 0.5046364080039043]  

Scaled data training and testing values:  
100 trees: [0.7981770833333334, 0.4992679355783309]  
500 trees: [0.7981770833333334, 0.5031722791605662]  
1000 trees: [0.7981770833333334, 0.5065885797950219]  
5000 trees: [0.7981770833333334, 0.5080527086383602]  

The scaled data produced slightly higher training and testing results, with the 5000 tree run producing the highest scores.
