# Data Analyst Salary Prediction

## data

Data set used - https://www.kaggle.com/andrewmvd/data-analyst-jobs

The data set contains more than 2000 job listing for data analyst positions, with features such as:

* Salary Estimate
* Location
* Company Rating
* Job Description
* Job title
* Industry
* Sector

The salary estimate column was cleaned and transformed into the average salary column.<br>
From the 'location' column I created two additional columns 'city' and 'state'. <br>
The 'Job Description' text column was transformed into categorical data. <br>
The description was checked if it contained some of the most sought after skills like python, spark, sas, excel, etc. <br>
As all the jobs are for data analyst positions, I just parsed for seniority. <br>

## model

I tried two different models and evaluated them using Mean Absolute Error.

* Linear Regression: MAE = 15.541 (15541 $ off)
* Random Forest: MAE = 14.782 (14782 $ off)
