# main.py
import streamlit as st
from transformers import pipeline
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os

# Load environment variables
load_dotenv()

# Initialize sentiment analysis model
emotion_classifier = pipeline("text-classification", 
                            model="bhadresh-savani/distilbert-base-uncased-emotion")

# Spotify API setup
def get_spotify_client():
    try:
        client_id = os.getenv("SPOTIFY_CLIENT_ID")
        client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
        
        if not client_id or not client_secret:
            st.error("Spotify credentials not found. Please check your .env file")
            return None
            
        auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
        return spotipy.Spotify(auth_manager=auth_manager)
    except Exception as e:
        st.error(f"Error connecting to Spotify: {str(e)}")
        return None

# Get playlists based on emotion
def get_playlists_by_emotion(emotion, limit=5):
    try:
        sp = get_spotify_client()
        if not sp:
            return None
            
        results = sp.search(q=emotion, type='playlist', limit=limit)
        if 'playlists' in results and 'items' in results['playlists']:
            return results['playlists']['items']
        return None
    except Exception as e:
        st.error(f"Error searching playlists: {str(e)}")
        return None

# Streamlit UI
st.title("Emotion-Based Playlist Generator")
user_input = st.text_area("How are you feeling today?")

if st.button("Generate Playlist"):
    if user_input:
        try:
            # Sentiment analysis
            emotion_result = emotion_classifier(user_input)[0]
            emotion = emotion_result['label']
            confidence = emotion_result['score']
            
            st.success(f"Detected emotion: {emotion} (confidence: {confidence:.2f})")        
            
            # Get playlists
            playlists = get_playlists_by_emotion(emotion)
            
            if playlists:
                st.subheader(f"Recommended {emotion} playlists:")
                for playlist in playlists:
                    if 'name' in playlist and 'tracks' in playlist and 'external_urls' in playlist:
                        st.markdown(f"""
                        **{playlist['name']}**  
                        Tracks: {playlist['tracks'].get('total', 'N/A')}  
                        [Open in Spotify]({playlist['external_urls'].get('spotify', '#')})
                        """)
            else:
                st.warning("No playlists found for this emotion. Please check your Spotify credentials.")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
    else:
        st.error("Please enter your feelings to generate a playlist")