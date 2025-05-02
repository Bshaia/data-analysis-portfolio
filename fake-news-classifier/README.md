# Fake News Classifier

This project is a binary text classification tool that detects fake news articles using natural language processing (NLP) and machine learning.

## Overview

Fake news poses a growing threat to public trust and information literacy. This project uses Python and scikit-learn to build a supervised learning model that distinguishes between real and fake news articles based on their content.

## Objectives

- Clean and preprocess real-world text data
- Vectorize article content using TF-IDF
- Train a Naive Bayes classifier
- Evaluate model performance using accuracy and confusion matrix
- Provide a reproducible workflow for fake news detection

## Tools and Technologies

- Python  
- Pandas  
- NumPy  
- scikit-learn  
- TF-IDF Vectorizer  
- Jupyter Notebook or VS Code

## Dataset

The dataset was sourced from [Kaggle](https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset). It contains two CSV files:
- `True.csv`: Articles verified to be real  
- `Fake.csv`: Articles confirmed to be fake  

## Key Steps

1. **Data Cleaning**  
   Combined the datasets and removed duplicate or null entries.

2. **Text Preprocessing**  
   - Lowercased text  
   - Removed stop words  
   - Tokenized articles  

3. **Feature Extraction**  
   Used TF-IDF vectorization to convert text into numerical features.

4. **Model Training**  
   Trained a Naive Bayes classifier on the vectorized data.

5. **Evaluation**  
   - Calculated accuracy score  
   - Generated confusion matrix and classification report

## Results

- **Model:** Multinomial Naive Bayes  
- **Accuracy:** ~92%  
- **Insights:** The model performed well on distinguishing real vs. fake articles, especially with well-tokenized and preprocessed content.

## How to Run

1. Clone the repository  
```bash  
git clone https://github.com/Bshaia/data-analysis-portfolio.git  
cd fake-news-classifier  
```

2. Install dependencies  
```bash  
pip install -r requirements.txt  
```

3. Run the notebook  
```bash  
jupyter notebook fake_news_classifier.ipynb  
```

## Author

**Brett Shaia**  
**Bachelor of Science in Computer Science**  
## Author

**Brett Shaia**  
Bachelor of Science in Computer Science  
Master's in Data Analytics (In Progress)  
Western Governors University  
[GitHub](https://github.com/Bshaia) • [Email](mailto:brettshaia@gmail.com)

Western Governors University, 2024  
[GitHub](https://github.com/Bshaia) • [Email](mailto:brettshaia@gmail.com)
