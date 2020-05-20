# conclave_predict
Project aiming to predict conclave result on the basis of several factors such as: participants, time, etc.

Status: On Hold

Following steps were undertaken during project preparation:

1. Data from 8 conclaves (1922 - 2013) was downloaded from Wikipedia pages
2. Conclaves data was transformed:
	- adding boolean variable 'Elected'
	- calculating cardinal's age and seniority at the start of conclave
	- flagging whether a given cardinal was Italian
	- assigning a cardinal into particular rank (Cardinal Bishop / Priest / Deacon)
3. Similar transformations (except for Elected' flag) were conducted for 'Living cardinals' data set, obtained from Wikipedia as well.
4. Logistic regression model was trained on 'Conclaves' data set.
5. Prediction was made on 'Living cardinals' data set:
	- it was assummed that next conclave would take place on 1st July 2020
	- top 10 cardinals with the highest probability to be elected the next Pope were selected

Due to the small number of variables used in the project (8) and its complex nature - it was decided that unless additional, reliable features are available, further development and analysis will be suspended.
