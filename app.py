import tkinter as tk
from tkinter import ttk, Scrollbar
import random
import webbrowser
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# ---------------- Spotify API Setup ----------------
client_id = "b36b68282a4849eab3a2e7101f56b50f"
client_secret = "3e09e6f7122644469e6a6b1724cf8147"

auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

# ---------------- Fun Quotes ----------------
fun_quotes = [
    "Life is better with music 🎧",
    "Vibe check: Loading songs...",
    "Music speaks what words can’t ✨",
    "Turn the volume up! 🔥",
    "Let the beat drop 🎶"
]

# ---------------- Functions ----------------
def show_songs(mood):
    songs_text.config(state=tk.NORMAL)
    songs_text.delete("1.0", tk.END)

    query = f"{mood} songs"
    result = sp.search(q=query, type="playlist", limit=1)

    if result['playlists']['items']:
        playlist = result['playlists']['items'][0]
        playlist_name = playlist['name']
        playlist_url = playlist['external_urls']['spotify']

        songs_text.insert(tk.END, f"🎶 {mood.capitalize()} Playlist 🎶\n\n")
        songs_text.insert(tk.END, f"Name: {playlist_name}\n\n")

        link_label.config(text="Open Playlist on Spotify", fg="blue", cursor="hand2")
        link_label.bind("<Button-1>", lambda e: webbrowser.open_new(playlist_url))
    else:
        songs_text.insert(tk.END, "No playlist found for this mood!")
        link_label.config(text="")  # Hide link if not found

    songs_text.config(state=tk.DISABLED)

# ---------------- UI Setup ----------------
root = tk.Tk()
root.title("Mood-Based Song Recommender")
root.geometry("420x420")
root.config(bg="#FCE4EC")

# Fun Quote Label
random_quote = random.choice(fun_quotes)
quote_label = tk.Label(root, text=random_quote, font=("Helvetica", 10, "italic"), bg="#FCE4EC", fg="#666")
quote_label.pack(pady=(10, 0))

# Welcome Label
welcome_label = tk.Label(root, text="🎵 Select Your Mood 🎵", font=("Helvetica", 16, "bold"), bg="#FCE4EC", fg="#333")
welcome_label.pack(pady=15)

# Button Styles
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12, "bold"), padding=5)

# Mood Buttons
btn_romantic = ttk.Button(root, text="💖 Romantic", command=lambda: show_songs("romantic"))
btn_romantic.pack(pady=5)

btn_sad = ttk.Button(root, text="😢 Sad", command=lambda: show_songs("sad"))
btn_sad.pack(pady=5)

btn_gym = ttk.Button(root, text="💪 Gym", command=lambda: show_songs("gym"))
btn_gym.pack(pady=5)

btn_rap = ttk.Button(root, text="🎤 Rap", command=lambda: show_songs("rap"))
btn_rap.pack(pady=5)

# Text Frame for Songs + Scrollbar
text_frame = tk.Frame(root, bg="#FCE4EC")
text_frame.pack(pady=10)

scrollbar = Scrollbar(text_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

songs_text = tk.Text(text_frame, height=8, width=40, font=("Helvetica", 10), yscrollcommand=scrollbar.set, wrap="word")
songs_text.pack(side=tk.LEFT)

scrollbar.config(command=songs_text.yview)

# Link Label
link_label = tk.Label(root, text="", font=("Helvetica", 11, "underline"), bg="#FCE4EC")
link_label.pack(pady=5)

# Main Loop
root.mainloop()
