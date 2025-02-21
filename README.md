# Emotion-Based Playlist Generator

A Streamlit application that analyzes your emotional state and recommends Spotify playlists based on your mood.

## Features
- Emotion detection from text input
- Spotify playlist recommendations based on detected emotion
- Real-time sentiment analysis using DistilBERT model

## Setup Instructions

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv myvenv
   source myvenv/bin/activate  # On Windows: myvenv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root with your Spotify API credentials:
   ```
   SPOTIFY_CLIENT_ID=your_client_id
   SPOTIFY_CLIENT_SECRET=your_client_secret
   ```

5. Run the application:
   ```bash
   streamlit run main.py
   ```

## Deployment

This application can be easily deployed to Streamlit Cloud:

1. Push your code to GitHub
2. Visit [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repository
4. Add your environment variables in the Streamlit Cloud dashboard
5. Deploy!

## Requirements
- Python 3.7+
- Streamlit
- Transformers
- Spotipy
- Python-dotenv

## Note
Make sure to keep your Spotify API credentials secure and never commit them to version control.
# emotion-based-playlist
