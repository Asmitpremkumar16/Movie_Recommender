# 🎬 Movie Recommender System

A **Movie Recommender System** built using **Python and Machine Learning** that recommends movies similar to the movie selected by the user.

The system uses **content-based filtering** to suggest movies based on similarities between movie features such as **genres, keywords, cast, and overview**.

This project demonstrates how **recommendation systems** work using **Natural Language Processing and similarity algorithms**.

---

## 📌 Features

- Recommend movies based on similarity
- Uses **Content-Based Filtering**
- Fast recommendations using **Cosine Similarity**
- Built using Python Data Science libraries
- Easy to extend for web apps using Streamlit or Flask

---

## 🧠 How It Works

The recommendation system follows these steps:

1. **Data Collection**
   - Dataset containing movie metadata.

2. **Data Preprocessing**
   - Handle missing values
   - Combine important columns (genres, keywords, cast, overview).

3. **Feature Extraction**
   - Convert text data into numerical vectors using **CountVectorizer**.

4. **Similarity Calculation**
   - Calculate similarity between movies using **Cosine Similarity**.

5. **Recommendation**
   - When a user selects a movie, the system finds the most similar movies.

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- NLTK
- Jupyter Notebook

---

## 📂 Project Structure

```
movie-recommender-system
│
├── dataset
│   ├── movies.csv
│   └── credits.csv
│
├── movie_recommender.ipynb
│
├── movies.pkl
├── similarity.pkl
│
└── README.md
```

Example usage:

```python
recommend("Avatar")
```

Example Output:

```
Titanic
Guardians of the Galaxy
Star Trek
Interstellar
The Avengers
```
