"""Simple Streamlit UI for the Music Recommender Simulation."""

from pathlib import Path

import streamlit as st

from src.recommender import load_songs, recommend_songs


PROFILES = {
    "High-Energy Pop": {
        "genre": "pop",
        "mood": "happy",
        "energy": 0.85,
        "tempo_bpm": 125,
    },
    "Chill Lofi": {
        "genre": "lofi",
        "mood": "chill",
        "energy": 0.35,
        "tempo_bpm": 75,
    },
    "Deep Intense Rock": {
        "genre": "rock",
        "mood": "intense",
        "energy": 0.90,
        "tempo_bpm": 150,
    },
}


def get_song_path() -> Path:
    """Return the path to the CSV file."""
    return Path(__file__).resolve().parent / "data" / "songs.csv"


def main() -> None:
    """Render the Streamlit app."""
    st.title("Music Recommender Simulation")
    st.write(
        "This simple web app uses the existing content-based recommender "
        "to suggest songs for a few example listener profiles."
    )

    profile_name = st.selectbox("Choose a profile", list(PROFILES.keys()))
    top_k = st.slider("Number of recommendations", min_value=1, max_value=5, value=3)

    selected_profile = PROFILES[profile_name]

    st.write("Selected preferences:")
    st.write(
        f"Genre: {selected_profile['genre']} | "
        f"Mood: {selected_profile['mood']} | "
        f"Energy: {selected_profile['energy']:.2f} | "
        f"Tempo: {selected_profile['tempo_bpm']} bpm"
    )

    if st.button("Get Recommendations"):
        songs = load_songs(str(get_song_path()))
        recommendations = recommend_songs(selected_profile, songs, k=top_k)

        st.subheader("Top Recommendations")

        for rank, (song, score, reasons) in enumerate(recommendations, start=1):
            st.markdown(f"### {rank}. {song['title']}")
            st.write(f"Artist: {song.get('artist', 'Unknown Artist')}")
            st.write(f"Score: {score:.2f}")

            if reasons:
                st.write("Reasons:")
                for reason in reasons:
                    st.write(f"- {reason}")
            else:
                st.write("Reasons: no strong matching features")

            st.divider()


if __name__ == "__main__":
    main()

# Run with: streamlit run app.py
