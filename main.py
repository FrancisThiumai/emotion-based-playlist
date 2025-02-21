import streamlit as st
from transformers import pipeline
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os

load_dotenv()

emotion_classifier = pipeline("text-classification", 
                            model="bhadresh-savani/distilbert-base-uncased-emotion")

def get_spotify_client():
    client_id = os.getenv("SPOTIFY_CLIENT_ID")
    client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
    auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    return spotipy.Spotify(auth_manager=auth_manager)

def get_playlists_by_emotion(emotion, limit=5):
    sp = get_spotify_client()
    results = sp.search(q=emotion, type='playlist', limit=limit)
    return results['playlists']['items']

st.title("Emotion-Based Playlist Generator")
user_input = st.text_area("How are you feeling today?")

if st.button("Generate Playlist"):
    if user_input:
        emotion_result = emotion_classifier(user_input)[0]
        emotion = emotion_result['label']
        confidence = emotion_result['score']
        
        st.success(f"Detected emotion: {emotion} (confidence: {confidence:.2f})")        
        playlists = get_playlists_by_emotion(emotion)
        
        if playlists:
            st.subheader(f"Recommended {emotion} playlists:")
            for playlist in playlists:
                st.markdown(f"""
                **{playlist['name']}**  
                Tracks: {playlist['tracks']['total']}  
                [Open in Spotify]({playlist['external_urls']['spotify']})
                """)
        else:
            st.warning("No playlists found for this emotion")
    else:
        st.error("Please enter your feelings to generate a playlist")