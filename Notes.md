
# Instructor Workshop notes
-------------------------------------
Course name ideas
Here are some sober and professional name ideas for your AI course:

1. **Foundations of AI**

2. **AI & Machine Learning Essentials**

3. **AI Fundamentals for Middle Schoolers**

4. **Practical AI: From Basics to Applications**

5. **Introduction to AI & Machine Learning**

6. **AI & Computer Vision for Young Learners**

7. **Exploring AI: Concepts & Applications**

8. **Hands-on AI for Middle School**

9. **Understanding AI: A Beginner’s Course**

10. **AI & Generative Models: A Practical Approach**

  
Based on the discussion, the following are the 4 broad sub-domains under AI we need to create a curriculum. I am assigning one area to each of you, let me know if you are ok

1. Predictive Analytics (Classical Machine Learning) - Scikit Learn etc. -- Shikha
2. Deep Learning (Computer Vision)- PyTorch / TensorFlow etc. -- Shweta
3. Generative AI (LLMs)- OpenAI, LangChain etc. -- Abhinav
4. NLP / Sentiment Analysis - NLTK etc. -- Premlata
5. Q-Learning etc. -- Chhavi


- Classification
- Regression
- Clustering
- Dimensionality Reduction
- Model selection
- Pre-processing


#### Regression
Purpose: Predicting a continuous-valued attribute associated with an object
Applications: House Price Prediction, Stock Price Prediction, Drug Response
Algorithms: Gradient Boosting, Nearest Neighbors, Random Forest

Starting Point: Linear Regression / House Price Prediction based on size, configuration and location

Steps
	1.	Dataset
Create or use an existing dataset to train your regression model, like a dataset with house sizes and prices.
	2.	Train a Linear Regression Model
Split the dataset into training and test sets, and then train a Linear Regression model using scikit-learn.
	3.	Visualize the Result
Plot the regression line along with the data points using a library like matplotlib to visualize how well the model fits the data.
	4.	Evaluate the Model
Evaluate the model’s performance using metrics such as Mean Squared Error (MSE) to measure how close the predicted values are to the actual values.


Libraries
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


Other Types of Regressions
	•	Polynomial Regression
	•	Ridge Regression
	•	Lasso Regression
	•	Decision Tree Regression


Reason for Other type of Regression models:
While Linear Regression works well in many situations, it assumes that the relationship between the independent variables (features) and the dependent variable (target) is linear, which is not always the case in real-world scenarios. When this assumption doesn’t hold, or when other complexities arise, other types of regression models become useful. Here’s why we need these other types of regressions and when to use them:

	•	Polynomial Regression: When data shows non-linear relationships.
	•	Ridge Regression: When you have multicollinearity (correlated features) or overfitting.
	•	Lasso Regression: When you want to prevent overfitting and perform feature selection.
	•	Elastic Net Regression: When you need a balance between Ridge and Lasso for highly correlated features.
	•	Logistic Regression: When solving a classification problem, not regression.



Good Examples of Linear Regression
	1.	Predicting House Prices
	•	Example: Predicting the price of a house based on its size (square footage).
	2.	Predicting Exam Scores Based on Study Hours
	•	Example: Predicting a student’s exam score based on the number of hours they studied.
	3.	Predicting Car Mileage Based on Engine Size
	•	Example: Predicting the fuel efficiency (miles per gallon) of a car based on engine size (displacement).
	4.	Predicting Salary Based on Years of Experience
	•	Example: Predicting an employee’s salary based on their years of experience.
	5.	Predicting Temperature Based on Time of Day
	•	Example: Predicting outdoor temperature based on the time of day (morning, afternoon, evening).
	6.	Predicting Weight Based on Height
	•	Example: Predicting a person’s weight based on their height.
	7.	Predicting Sales Based on Advertising Spend
	•	Example: Predicting the sales of a product based on the money spent on advertising.
	8.	Predicting the Height of a Plant Based on Time
	•	Example: Predicting the growth of a plant over time (height vs. time in days or weeks).



Machine Learning Workflow
=======================
	1.	Understanding the problem
	2.	Loading Data
	3.	Data Preprocessing
			Splitting into features and labels, and training and testing
	4.	Choosing a Model
	5.	Training the Model
	6.	Making Predictions
	7.	Evaluating the Model
	8.	Improving the Model


Classification
==========
Identifying which category an object belongs to.

Applications: Spam detection, image recognition.
Algorithms: Gradient boosting, nearest neighbors, random forest, logistic regression, K-NN, SVM, decision trees
Most Common: Logistic Regression
Other Concepts: Confusion Matrix, Hyperparameter Tuning

