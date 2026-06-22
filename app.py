import streamlit as st
import pickle

# -------------------
# Page Configuration
# -------------------
st.set_page_config(
    page_title="CineMatch AI",
    page_icon="🎬",
    layout="wide"
)

# -------------------
# Custom CSS
# -------------------
st.markdown("""
<style>

.stApp {
    background: linear-gradient(
        135deg,
        #0f172a,
        #111827,
        #1e1b4b
    );
    color: white;
}

.hero {
    text-align: center;
    padding: 2rem;
}

.hero h1 {
    font-size: 4rem;
    color: white;
}

.hero p {
    font-size: 1.2rem;
    color: #d1d5db;
}

.card {
    background: rgba(255,255,255,0.08);
    border-radius: 20px;
    padding: 25px;
    text-align: center;
    backdrop-filter: blur(15px);
    margin-top: 20px;
    transition: 0.3s;
}

.card:hover {
    transform: scale(1.05);
}

.match {
    color: #60a5fa;
    font-weight: bold;
    font-size: 20px;
}

div.stButton > button {
    width: 100%;
    height: 60px;
    border-radius: 15px;
    border: none;
    background: linear-gradient(
        90deg,
        #6366f1,
        #8b5cf6
    );
    color: white;
    font-size: 20px;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

# -------------------
# Load Data
# -------------------
movies = pickle.load(
    open("movies.pkl", "rb")
)

similarity = pickle.load(
    open("similarity.pkl", "rb")
)

# -------------------
# Recommendation Function
# -------------------
def recommend(movie):

    movie_index = movies[
        movies['title'] == movie
    ].index[0]

    distances = similarity[movie_index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []
    similarity_scores = []

    for i in movies_list:
        recommended_movies.append(
            movies.iloc[i[0]].title
        )

        score = round(i[1] * 100)
        similarity_scores.append(score)

    return recommended_movies, similarity_scores


# -------------------
# Hero Section
# -------------------
st.markdown("""
<div class='hero'>
<h1>🎬 CineMatch AI</h1>
<p>
Discover your next favorite film
using Machine Learning and AI
</p>
</div>
""", unsafe_allow_html=True)

# -------------------
# Search Box
# -------------------
selected_movie = st.selectbox(
    "🔍 Search a Movie",
    movies['title'].values
)

# -------------------
# Button
# -------------------
if st.button("🚀 Recommend"):

    names, scores = recommend(
        selected_movie
    )

    st.markdown("## Recommended Movies")

    cols = st.columns(5)

    for i in range(5):
        with cols[i]:
            st.markdown(
                f"""
                <div class='card'>
                <h3>🎬</h3>
                <h4>{names[i]}</h4>
                <p class='match'>
                ⭐ {scores[i]}% Match
                </p>
                </div>
                """,
                unsafe_allow_html=True
            )

# Footer
st.markdown("---")
st.markdown(
    """
    <center>
    Built with ❤️ using
    Python • NLP • Scikit-learn • Streamlit
    </center>
    """,
    unsafe_allow_html=True
)