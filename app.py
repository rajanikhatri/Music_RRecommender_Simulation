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


def inject_styles() -> None:
    """Add custom styles for the Streamlit page."""
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #f8f7f2;
            color: #243126;
        }

        h1, h2, h3 {
            color: #4f7f5a;
        }

        .card {
            background: #ffffff;
            border-radius: 14px;
            padding: 18px;
            margin-bottom: 16px;
            border: 1px solid #e3eadf;
            box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        }

        .card-rank {
            font-size: 0.95rem;
            color: #6b7d6d;
            margin-bottom: 6px;
        }

        .card-title {
            font-size: 1.2rem;
            font-weight: 700;
            color: #243126;
            margin-bottom: 4px;
        }

        .card-artist {
            font-size: 0.95rem;
            color: #5f6f61;
            margin-bottom: 12px;
        }

        .score-badge {
            display: inline-block;
            background-color: #dcefe0;
            color: #4f7f5a;
            padding: 4px 10px;
            border-radius: 8px;
            font-size: 0.95rem;
            font-weight: 600;
            margin-bottom: 10px;
        }

        .reason-tag {
            display: inline-block;
            margin: 6px 6px 0 0;
            padding: 4px 10px;
            border-radius: 999px;
            background: #eef4ef;
            color: #47614d;
            font-size: 0.82rem;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def get_song_path() -> Path:
    """Return the path to the CSV file."""
    return Path(__file__).resolve().parent / "data" / "songs.csv"


def format_reason_tags(reasons: list[str]) -> str:
    """Turn full reason strings into short tag labels."""
    tags = []

    for reason in reasons:
        tag_text = reason.split(" (")[0]
        tags.append(
            f"<span class='reason-tag'>{tag_text}</span>"
        )

    return "".join(tags)


def render_recommendation_card(rank: int, song: dict, score: float, reasons: list[str]) -> None:
    """Show one recommendation in a card-style block."""
    artist_name = song.get("artist", "Unknown Artist")
    tags_html = format_reason_tags(reasons) if reasons else (
        "<span class='reason-tag'>no strong matching features</span>"
    )

    st.markdown(
        f"""
        <div class="card">
            <div class="card-rank">#{rank}</div>
            <div class="card-title">
                {song['title']}
            </div>
            <div class="card-artist">
                {artist_name}
            </div>
            <div class="score-badge">
                Score: {score:.2f}
            </div>
            <div>{tags_html}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def main() -> None:
    """Render the Streamlit app."""
    st.set_page_config(page_title="Music Recommender Simulation", layout="wide")
    inject_styles()
    st.title("Music Recommender Simulation")
    st.write(
        "This simple web app uses the existing content-based recommender "
        "to suggest songs for a few example listener profiles."
    )

    left_col, right_col = st.columns([1, 1.5], gap="large")

    with left_col:
        st.subheader("Select Profile")
        profile_name = st.selectbox("Profile", list(PROFILES.keys()))
        top_k = st.slider(
            "Number of Recommendations",
            min_value=1,
            max_value=10,
            value=3,
        )

        selected_profile = PROFILES[profile_name]

        st.write("Current profile:")
        st.write(
            f"Genre: {selected_profile['genre']} | "
            f"Mood: {selected_profile['mood']}"
        )
        st.write(
            f"Energy: {selected_profile['energy']:.2f} | "
            f"Tempo: {selected_profile['tempo_bpm']} bpm"
        )

        if st.button("Get Recommendations", use_container_width=True):
            songs = load_songs(str(get_song_path()))
            st.session_state["recommendations"] = recommend_songs(
                selected_profile,
                songs,
                k=top_k,
            )
            st.session_state["selected_profile_name"] = profile_name

    with right_col:
        st.subheader("Recommendation Results")

        if "recommendations" in st.session_state:
            st.caption(
                f"Showing results for {st.session_state.get('selected_profile_name', profile_name)}"
            )

            for rank, (song, score, reasons) in enumerate(
                st.session_state["recommendations"],
                start=1,
            ):
                render_recommendation_card(rank, song, score, reasons)
        else:
            st.info("Choose a profile and click Get Recommendations to see results.")


if __name__ == "__main__":
    main()

# Run with: streamlit run app.py
