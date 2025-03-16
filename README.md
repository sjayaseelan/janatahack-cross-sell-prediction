# JanataHack Cross-Sell Prediction

This repository explores data analysis and machine learning techniques to predict customer interest. Specifically, it focuses on identifying whether a customer is likely to be interested in vehicle insurance based on historical data.

## Dataset

The Customer Dataset is sourced from the hackathon site. It contains customer details along with their vehicle and policy information. The dataset includes the following features:

- **Customer ID**: Unique identifier for each customer  
- **Customer Demographics**: Age, gender, region, etc.  
- **Vehicle Details**: Vehicle age, damage, etc.  
- **Policy Details**: Premium, sourcing channel, etc.  
- **Response**: Target variable indicating whether the customer is interested in the policy or not.  

## Step-by-Step Instructions

### 1. Data Understanding and Observations
- Import Libraries  
- Load Data  
- Initial Exploration  

### 2. Exploratory Data Analysis (EDA)
- Visualize Distributions  
- Univariate Analysis  
- Bivariate Analysis  

### 3. Data Cleaning
- Check and handle missing values  
- Outlier Detection  
- Convert data types (if necessary)  

### 4. Feature Engineering
- Encoding categorical data  
- Feature scaling for numerical data  
- Create new features from existing columns  

### 5. Model Building
- Train-Test Split  
- Modeling using Pipelining  
- Ensemble Techniques  
- Model Training and Prediction  

### 6. Model Evaluation and Tuning
- Evaluate model performance using **roc_auc_score**  
- Optimize model by Hyperparameter Tuning (GridSearch or other methods)  
- Compare different models  

### 7. Evaluate Test Solution
- Use `predict_proba` (Probability of response = 1)  
- Test the solution on the hackathon website and capture the result  

### 8. Interpret Results
- Summarize findings, model performance, and key insights in a final report  
- Compare models and explain which model was most impactful in predicting customer interest  
- Choose the final model and **pickle it** for API and UI usage  

### 9. API Creation
- Create a **FastAPI** endpoint using the pickled final model  

### 10. User Interface (UI) Development
- Develop a **Web App** user interface with the pickled final model using **Streamlit**  

### 11. Deploy API Using GCP
- Create a new **GitHub repository** and push all required files (Python files, Docker files, requirements.txt, pickle file, etc.)  
- Deploy the API on **Google Cloud Platform (GCP)** for public use  
- Share the deployed API URL  

### 12. Deploy Web App Using GCP or Streamlit
- Create a new **GitHub repository** and push all required files  
- Deploy the web app using **GCP or Streamlit**  
- Share the public URL of the deployed web app  

### 13. PowerPoint Presentation
- Prepare a **PowerPoint presentation** summarizing:
  - Problem statement  
  - Approach  
  - Findings  
  - Recommendations  
  - Deployed links  

### 14. Recorded Demo
- Record a **5-minute demo** showcasing:
  - Code walkthrough  
  - Methodology explanation  
  - Results demonstration  

---

This structured approach ensures a complete workflow from data analysis to deployment and presentation. 🚀

