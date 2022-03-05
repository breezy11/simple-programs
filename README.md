# Simple Programs

## stock price forecast
This program uses an artificial recurrent neural network called Long Short Term Memory (LSTM - multivariate)<br/>to predict the opening stock price of 'Apple' for 30 days using the past 60-day stock price.

### data

The stock data was gathered from yahoo finance using the pandas_datareader package. <br>
The stock used in this example is 'Apple' (AAPL). <br>
The timeframe is from the 1st of January 2016 to the 1st of January 2021.

### model

#### prediction

![Plot of the predicted vs actual prices](https://github.com/breezy11/simple-programs/stock-predictor/blob/master/plots/predicted.png)

#### loss

![Plot of the training and validation loss](https://github.com/breezy11/simple-programs/stock-predictor/blob/master/plots/training-validation-loss.png)



## data analyst salary prediction

### data

Data set used - https://www.kaggle.com/andrewmvd/data-analyst-jobs
The data set contains more than 2000 job listing for data analyst positions.

### model

I tried two different models and evaluated them using Mean Absolute Error.

* Linear Regression: MAE = 15.541 (15541 $ off)
* Random Forest: MAE = 14.782 (14782 $ off)


## stock sentiment analysis

This is a repository containing all the simple programs I haven't deleted.

This program predicts if the stock index price will increase or decrease based on top news headlines. <br>
Predictions are based on sentiment scores. The headlines are fed as blocks of texts to TextBlob to get the subjectivity and polarity scores. <br>

### data

Data set used - https://www.kaggle.com/aaron7sun/stocknews

The timeframe is from the 6th of August 2008 to the 1st of July 2016.
The stock used is Dow Jones Industrial Average (DJIA).
The news are ranked by reddit users votes, and only the top 25 headlines are considered for a single date.

### model metrics

|              | precision | recall | f1-score | support |
|--------------|-----------|--------|----------|---------|
| 0            | 0.56      | 0.20   | 0.29     | 193     |
| 1            | 0.53      | 0.85   | 0.65     | 205     |

## cross-the-road

Language: C++

Cross the road game written in C++. <br>
A classic arcade game where the goal is to cross the street without getting hit by a car.

## heart-disease-classification

Language: Python <br>
Data: https://www.kaggle.com/ronitf/heart-disease-uci.

The goal was to classify how severe the disease was. <br>
I created a simple K-means and Knn models and tested how accurate they were.

K-Nearest-Neighbor accuracy : 0.819672131147541 <br>
K-Means accuracy: 0.7049180327868853

## iris-machine-learning

Language: R <br>
Data: iris

The hello world program of machine learning in r. <br>
I created five models and tested their accuracies.

![Accuracy plot](https://github.com/breezy11/simple-programs/blob/master/iris-machine-learning/accuracy-plot.png)

## tic-tac-toe

Language: Python

A classic game of tic tac toe wrote in Python. <br>

![Game image](https://github.com/breezy11/simple-programs/blob/master/tic-tac-toe/game.png)


