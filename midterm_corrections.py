# A. Import the libraries you will need
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# B. Create your DoKFold

def DoKFold(model, X, y, k, standardize=False, random_state=146):
        import numpy as np
        from sklearn.model_selection import KFold
        kf = KFold(n_splits=k, shuffle=True, random_state=random_state)

        train_scores = []
        test_scores = []

        train_mse = []
        test_mse = []


        for idxTrain, idxTest in kf.split(X):
            Xtrain = X[idxTrain, :]
            Xtest = X[idxTest, :]
            ytrain = y[idxTrain]
            ytest = y[idxTest]

            if standardize:
                from sklearn.preprocessing import StandardScaler as SS
                ss = SS()
                Xtrain = ss.fit_transform(Xtrain)
                Xtest = ss.transform(Xtest)


            model.fit(Xtrain, ytrain)

            train_scores.append(model.score(Xtrain, ytrain))
            test_scores.append(model.score(Xtest, ytest))

            ytrain_pred = model.predict(Xtrain)
            ytest_pred = model.predict(Xtest)

            train_mse.append(np.square(np.subtract(ytrain, ytrain_pred)).mean())
            test_mse.append(np.square(np.subtract(ytest, ytest_pred)).mean())


        return train_scores,test_scores,train_mse,test_mse

# C. Import the the California Housing data

from sklearn.datasets import fetch_california_housing


# D.    # 1. set up X as your features from data.data
        # 2. create a names object from data.feature_names
        # 3. set up y as your target from data.target
        # 4. use pandas to create a data frame from your features and names object

data = fetch_california_housing()

X = data.data
x_names = data.feature_names
y = data.target

X_df = pd.DataFrame(X, columns = x_names)



### 15. ###

# Which of the below features is most strongly correlated with the target?

Xy = X_df.copy()
Xy['y'] = y
Xy.corr()

# ANSWER: MedInc

### 16. ###

# If the features are standardized, the correlations from the previous question do not change.

from sklearn.preprocessing import StandardScaler as SS
ss = SS()
Xs = ss.fit_transform(X)
Xs_df = pd.DataFrame(X, columns = x_names)
Xsy_df = Xs_df.copy()
Xsy_df['y'] = y
Xsy_df.corr()

# ANSWER: True

### 17 ###

# If we were to perform a linear regression using only the feature identified in question 15,
# what would be the coefficient of determination?
# Enter your answer to two decimal places, for example: 0.12

np.round(np.corrcoef(X_df['MedInc'], y)[0][1]**2,2)

from sklearn.linear_model import LinearRegression as LR

lin_reg = LR()
lin_reg.fit(X_df['MedInc'].values.reshape(-1,1), y)
np.round(lin_reg.score(X_df['MedInc'].values.reshape(-1,1), y), 2)

# ANSWER: 0.47

### 18 ###

# Let's take a look at how a few different regression methods perform on this data.
#
# Start with a linear regression.
#
# Standardize the data
# Perform a K-fold validation using:
# k=20
# shuffle=True
# random_state=146
# What is the mean R2 value on the test folds?  Enter your answer to 5 decimal places, for example: 0.12345


k = 20

train_scores, test_scores, train_mse, test_mse = DoKFold(LR(),X, y, k, standardize=True)
print('Training R^2:', np.mean(train_scores), 'Testing R^2:', np.mean(test_scores))
print('Training MSE:', np.mean(train_mse), 'Testing MSE:', np.mean(test_mse))

# ANSWER: 0.60198

### 19 ###

# Next, try Ridge regression.
#
# To save you some time, I've determined that you should look at 101 equally spaced values between 20 and 30 for alpha.
#
# Use the same settings for K-fold validation as in the previous question.
#
# For the optimal value of alpha in this range, what is the mean R2 value on the test folds?
# Enter your answer to 5 decimal places, for example: 0.12345

from sklearn.linear_model import Ridge, Lasso

rid_a_range = np.linspace(20,30,101)

rid_tr = []
rid_te = []
rid_tr_mse = []
rid_te_mse = []

for a in rid_a_range:
    mdl = Ridge(alpha = a)
    train, test, train_mse, test_mse = DoKFold(mdl, X, y, k, True)

    rid_tr.append(np.mean(train))
    rid_te.append(np.mean(test))
    rid_tr_mse.append(np.mean(train_mse))
    rid_te_mse.append(np.mean(test_mse))

idx = np.argmax(rid_te)
print(rid_a_range[idx], rid_tr[idx], rid_te[idx], rid_tr_mse[idx], rid_te_mse[idx])

plt.plot(rid_a_range, rid_te,'or')
plt.xlabel('$\\alpha$')
plt.ylabel('Avg $R^2$')
plt.show()

# ANSWER: 0.60201

### 20 ###

# Next, try Lasso regression.  Look at 101 equally spaced values between 0.001 and 0.003.
las_a_range = np.linspace(0.001, 0.003, 101)

las_tr = []
las_te = []
las_tr_mse = []
las_te_mse = []
# For the optimal value of alpha in this range, what is the mean R2 value on the test folds?
# Enter you answer to 5 decimal places, for example: 0.12345

for a in las_a_range:
    mdl = Lasso(alpha=a)
    train, test, train_mse, test_mse = DoKFold(mdl, X, y, k, True)

    las_tr.append(np.mean(train))
    las_te.append(np.mean(test))
    las_tr_mse.append(np.mean(train_mse))
    las_te_mse.append(np.mean(test_mse))

idx = np.argmax(las_te)
print(las_a_range[idx], las_tr[idx], las_te[idx], las_tr_mse[idx], las_te_mse[idx])

plt.plot(las_a_range, las_te)
plt.xlabel('$\\alpha$')
plt.ylabel('Avg $R^2$')
plt.show()

# ANSWER: optimal alpha is 0.00186

### 21 ###

# Let's look at some of what these models are estimating.
#
# Refit a linear, Ridge, and Lasso regression to the entire (standardized) dataset.
# No need to do any train/test splits or K-fold validation here. Use the optimal alpha values you found previously.

# Which of these models estimates the smallest coefficient for the variable that is least correlated
# (in terms of absolute value of the correlation coefficient) with the target?

print(x_names[5])
lin = LR(); rid = Ridge(alpha=25.8); las = Lasso(alpha = 0.00186)
lin.fit(Xs, y); rid.fit(Xs, y); las.fit(Xs, y);
lin.coef_[5], rid.coef_[5], las.coef_[5]

# ANSWER: LASSO

### 22 ###

# Which of the above models estimates the smallest coefficient for the variable that is most correlated
# (in terms of the absolute value of the correlation coefficient) with the target?

print(x_names[0])
lin.coef_[0], rid.coef_[0], las.coef_[0]

# ANSWER: LASSO

### 23 ###

# If we had looked at MSE instead of R2 when doing our Ridge regression (question 19),
# would we have determined the same optimal value for alpha, or something different?

idx = np.argmin(rid_te_mse)
print(rid_a_range[idx], rid_tr[idx], rid_te[idx], rid_tr_mse[idx], rid_te_mse[idx])

plt.plot(rid_a_range, rid_te_mse,'or')
plt.xlabel('$\\alpha$')
plt.ylabel('Avg MSE')
plt.show()

# ANSWER: Alpha = 26.1 (different than R2 value of 25.8)

### 24 ###

# If we had looked at MSE instead of R2 when doing our Lasso regression (question 20),
# what would we have determined the optimal value for alpha to be?
#
# Enter your answer to 5 decimal places, for example: 0.12345

idx = np.argmin(las_te_mse)
print(las_a_range[idx], las_tr[idx], las_te[idx], las_tr_mse[idx], las_te_mse[idx])

plt.plot(las_a_range, las_te_mse,'or')
plt.xlabel('$\\alpha$')
plt.ylabel('Avg MSE')
plt.show()

# ANSWER: alpha = 0.00186



