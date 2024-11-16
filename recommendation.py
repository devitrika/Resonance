import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MinMaxScaler

# Load datasets
@st.cache_data
def load_data():
    all_posts = pd.read_csv("all_posts.csv")
    all_users = pd.read_csv("all_users.csv")
    liked_posts = pd.read_csv("liked_posts.csv")
    viewed_posts = pd.read_csv("viewed_posts.csv")
    user_ratings = pd.read_csv("user_ratings.csv")
    return all_posts, all_users, liked_posts, viewed_posts, user_ratings

# Preprocess datasets
@st.cache_data
def preprocess_data():
    all_posts, all_users, liked_posts, viewed_posts, user_ratings = load_data()
    
    # Ensure all IDs are consistent
    all_posts['id'] = all_posts['id'].astype(str)
    liked_posts['id'] = liked_posts['id'].astype(str)
    viewed_posts['id'] = viewed_posts['id'].astype(str)
    user_ratings['id'] = user_ratings['id'].astype(str)

    # Merge datasets where needed
    liked_posts['interaction_type'] = 'liked'
    viewed_posts['interaction_type'] = 'viewed'
    interactions = pd.concat([liked_posts, viewed_posts], ignore_index=True)

    all_posts['combined_features'] = all_posts['title'].fillna("").astype(str) + " " + all_posts['genre'].fillna("").astype(str)

    # Normalize numeric features
    scaler = MinMaxScaler()
    all_posts[['upvote_count', 'view_count', 'average_rating']] = scaler.fit_transform(
        all_posts[['upvote_count', 'view_count', 'average_rating']]
    )

    return all_posts, interactions

# Define recommendation functions
def content_based_recommendation(all_posts, video_id, top_n=5):
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(all_posts['combined_features'])
    content_similarity = cosine_similarity(tfidf_matrix, tfidf_matrix)
    video_idx = all_posts[all_posts['id'] == video_id].index[0]
    similar_indices = content_similarity[video_idx].argsort()[-top_n-1:-1][::-1]
    similar_videos = all_posts.iloc[similar_indices]
    return similar_videos[['id', 'title', 'genre']]

def collaborative_recommendation(user, interactions, all_posts, top_n=5):
    user_item_matrix = interactions.pivot_table(
        index='username', columns='id', values='interaction_type', aggfunc='count'
    ).fillna(0)
    user_similarity = cosine_similarity(user_item_matrix)
    user_similarity_df = pd.DataFrame(user_similarity, index=user_item_matrix.index, columns=user_item_matrix.index)
    if user not in user_similarity_df.index:
        return "No data available for this user."
    similar_users = user_similarity_df[user].sort_values(ascending=False)[1:top_n+1].index
    recommendations = interactions[interactions['username'].isin(similar_users)]
    recommended_posts = recommendations['id'].value_counts().head(top_n).index
    return all_posts[all_posts['id'].isin(recommended_posts)][['id', 'title', 'genre']]

def hybrid_recommendation(user, video_id, all_posts, interactions, top_n=5):
    content_recs = content_based_recommendation(all_posts, video_id, top_n)
    collab_recs = collaborative_recommendation(user, interactions, all_posts, top_n)
    if isinstance(collab_recs, str):  # Handle case with no collaborative data
        return content_recs
    combined_recs = pd.concat([content_recs, collab_recs]).drop_duplicates().head(top_n)
    return combined_recs

# Streamlit UI
st.title("Resonance: Find Your Spark 🔥, Unlock Your Potential 💪")
st.sidebar.header("User Input")

# Select recommendation type
rec_type = st.sidebar.radio(
    "Select Recommendation Type:",
    options=["Content-Based", "Collaborative", "Hybrid"]
)

# Input fields
user = st.sidebar.text_input("Enter Username (for Collaborative/Hybrid):", value="kinha")
video_id = st.sidebar.text_input("Enter Video ID (for Content-Based/Hybrid):", value="11")

# Load and preprocess data
all_posts, interactions = preprocess_data()

# Perform recommendations

def display_recommendations(recommendations):
    if recommendations.empty:
        st.write("No recommendations available.")
        return
    
    for _, row in recommendations.iterrows():
        st.write(f"### {row['title']}")
        st.write(f"**Genre**: {row['genre']}")
        
        # Display the thumbnail as an image
        if 'thumbnail_url' in row:
            st.image(row['thumbnail_url'], use_column_width=True, caption=row['title'])
        else:
            st.write("Thumbnail not available.")
        
        st.write("---")  # Separator

if rec_type == "Content-Based":
    st.header("Content-Based Recommendations")
    recommendations = content_based_recommendation(all_posts, video_id)
    display_recommendations(recommendations)

elif rec_type == "Collaborative":
    st.header("Collaborative Recommendations")
    recommendations = collaborative_recommendation(user, interactions, all_posts)
    display_recommendations(recommendations)

elif rec_type == "Hybrid":
    st.header("Hybrid Recommendations")
    recommendations = hybrid_recommendation(user, video_id, all_posts, interactions)
    display_recommendations(recommendations)
