import streamlit as st
import pickle
import gdown
import os


movies= pickle.load(open('movies.pkl','rb'))
file_id = "1-EHGBW_MGdvZFpQGsIcNvq4dXRVbcwxG"
file_path = "similarity.pkl"

# Download only if not already present
if not os.path.exists(file_path):
    url = f"https://drive.google.com/uc?id={file_id}"
    gdown.download(url, file_path, quiet=False)

# Load the pickle file
similarity = pickle.load(open(file_path, "rb"))
movies_list= movies['title'].values


st.set_page_config(page_title="Movie Recommender", layout="wide")
st.header("Movie Recommender System")

selected_movie= st.selectbox('Select a movie',movies_list)


def recommend(selected_movie, n=5):
    if selected_movie not in movies['title'].values:
        print("Movie not found")
        return

    movie_index = movies[movies['title'] == selected_movie].index[0]
    distances = similarity[movie_index]

    movie_list = sorted(
        enumerate(distances),
        key=lambda x: x[1],
        reverse=True
    )[1:n+1]

    recommended_movies = []
    

    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        

    return recommended_movies


if st.button('Show Recommendation'):
    movie_name= recommend(selected_movie)           
    col1, col2, col3, col4, col5 = st.columns(5)    
    with col1:
        st.text(movie_name[0])
        

    with col2:
        st.text(movie_name[1])
        

    with col3:
        st.text(movie_name[2])
        
    
    with col4:
        st.text(movie_name[3])
        
        
    with col5:
        st.text(movie_name[4])
        
