# janatahack-cross-sell-prediction
This repository explores data analysis and machine learning techniques to predict customer interest. Specifically, it focuses on identifying whether a customer is likely to be interested in vehicle insurance based on historical data.

## Dataset
The Customer Dataset taken from the hackathon site. The dataset contains customer details along with their vehicle and policy information. The dataset includes features like:
 Customer ID: Unique identifier for each customer
 Customer Demographics: Age, gender, region, etc.
 Vehicle Details: Vehicle age, damage, etc.
 Policy Details: Premium, sourcing channel, etc.
 Response: Target variable indicating whether the customer is interested in the
policy or not.
  
Step-by-Step Instructions
 Data understanding and observations
Import Libraries, Load Data, Initial Exploration, etc.
 Exploratory Data Analysis (EDA)
Visualize Distributions, Univariate Analysis, Bivariate Analysis, etc.
 Data Cleaning
Check and Handling Missing values, Outlier Detection, Convert data types (if necessary), etc.
 Feature Engineering
Encoding Categorical Data, Feature Scaling Numerical Data, Create New Features from existing columns, etc.
 Model Building
Train-Test Split, Modeling using Pipelining, Ensemble Techniques, Model Training and Prediction.
 Model Evaluation and Tuning
Evaluate Model Performance using Metrics specified (roc_auc_score) in the hackathon site, Optimize model by Hyperparameter Tuning using GridSearch or others, and Compare Models.
 Evaluate Test solution
Use predict_proba (Probability of response 1) and test your solution in hackathon’s website and capture result.
 Interpret Results
Summarize your findings, model performance, and key insights into a final report. Compare models and explain which model were most impactful in predicting promotion and choose it as final model and pickle it for using them in API and UI.
 API Creation
Create a FastAPI endpoint using the pickled final model.
 User Interface UI Development
Create a Web App User Interface with the pickled final model using Streamlit library.
 Deploy API using GCP
Create a new repository in your personal github account and push all the required files (python files, Docker files, Requirements file, pickle file, etc.) and deploy them using GCP for public use and share the URL links.
 Deploy WebApp using GCP or Streamlit
Create a new repository in your personal github account and push the required files (python files, Docker files, Requirements file, pickle file,

etc.) and deploy them using GCP or Streamlit for public use and share the
respective URL links.
 PowerPoint Presentation
Prepare a PowerPoint presentation having all the steps performed along with summarizing the problem, approach, findings, recommendations and deployed links.
 Recorded Demo
Record a brief demo (5 minutes) walking through your code, explaining your methodology, and showcasing results.
