"""Command line demo for the Music Recommender Simulation."""

from pathlib import Path
from typing import Dict, List, Tuple

from src.recommender import load_songs, recommend_songs


def print_profile_results(
    profile_name: str,
    user_prefs: Dict,
    songs: List[Dict],
    k: int = 3,
) -> None:
    """Print recommendations for one example user profile."""
    recommendations = recommend_songs(user_prefs, songs, k=k)

    print("=" * 68)
    print(f"Profile: {profile_name}")
    print(
        "Preferences: "
        f"genre={user_prefs['genre']}, "
        f"mood={user_prefs['mood']}, "
        f"energy={user_prefs['energy']:.2f}, "
        f"tempo={user_prefs['tempo_bpm']} bpm"
    )
    print("-" * 68)

    for index, (song, score, reasons) in enumerate(recommendations, start=1):
        artist_text = f" - {song['artist']}" if song.get("artist") else ""
        print(f"{index}. {song['title']}{artist_text}")
        print(f"   Score: {score:.2f}")

        if reasons:
            print("   Reasons:")
            for reason in reasons:
                print(f"   - {reason}")
        else:
            print("   Reasons: no strong matching features")

        print()


def main() -> None:
    """Run the recommender with a few sample profiles."""
    project_root = Path(__file__).resolve().parent.parent
    csv_path = project_root / "data" / "songs.csv"
    songs = load_songs(str(csv_path))

    user_profiles: List[Tuple[str, Dict]] = [
        (
            "High-Energy Pop",
            {"genre": "pop", "mood": "happy", "energy": 0.85, "tempo_bpm": 125},
        ),
        (
            "Chill Lofi",
            {"genre": "lofi", "mood": "chill", "energy": 0.35, "tempo_bpm": 75},
        ),
        (
            "Deep Intense Rock",
            {"genre": "rock", "mood": "intense", "energy": 0.90, "tempo_bpm": 150},
        ),
    ]

    print("\nMusic Recommender Simulation")
    print("=" * 68)
    print(f"Loaded {len(songs)} songs from {csv_path.name}\n")

    for profile_name, user_prefs in user_profiles:
        print_profile_results(profile_name, user_prefs, songs)


if __name__ == "__main__":
    main()
