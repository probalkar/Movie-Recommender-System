import pickle
import streamlit as st
import pandas as pd

def recommend(movie):
    index = movies[movies['Series_Title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        recommended_movie_posters.append(movies.iloc[i[0]].Poster_Link)
        recommended_movie_names.append(movies.iloc[i[0]].Series_Title)

    return recommended_movie_names,recommended_movie_posters


st.header('Movie Recommender System')
movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))

movie_list = movies['Series_Title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0], width=120)
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1], width=120)

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2], width=120)
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3], width=120)
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4], width=120)