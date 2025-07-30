import tkinter as tk
from tkinter import ttk, Scrollbar
import random
import webbrowser
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Spotify API Setup
# Ye credentials Spotify Developer account se milta h
client_id = "b36b68282a4849eab3a2e7101f56b50f"
client_secret = "3e09e6f7122644469e6a6b1724cf8147"

# Authentication setup
auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

# Quotes jo app ke upar dikhega
fun_quotes = [
    "Feelings come in frequencies.🎧",
    "Your playlist reveals your soul.",
    "Melody heals what words can't. ✨",
    "Let the music fuel the fire 🔥",
    "Every beat is a comeback.🎶"
]

# Playlist dikhane wala function
def show_songs(mood):
    # Pehle purani info hata do
    songs_text.config(state=tk.NORMAL)
    songs_text.delete("1.0", tk.END)

    # Spotify par mood k basis pe playlist search kro
    query = f"{mood} songs"
    result = sp.search(q=query, type="playlist", limit=1)

    # Agr playlist mil jaaye
    if result['playlists']['items']:
        playlist = result['playlists']['items'][0]
        playlist_name = playlist['name']
        playlist_url = playlist['external_urls']['spotify']

        # Playlist ka naam display kro
        songs_text.insert(tk.END, f"🎶 {mood.capitalize()} Playlist 🎶\n\n")
        songs_text.insert(tk.END, f"Name: {playlist_name}\n\n")

        # Spotify link create kro (clickable)
        link_label.config(text="Open Playlist on Spotify", fg="blue", cursor="hand2")
        link_label.bind("<Button-1>", lambda e: webbrowser.open_new(playlist_url))
    else:
        songs_text.insert(tk.END, "No playlist found for this mood!")
        link_label.config(text="")  # agar kuch nahi mila to link mat dikhao

    songs_text.config(state=tk.DISABLED)

# GUI Setup
root = tk.Tk()
root.title("Mood-Based Song Recommender")  # App ka title
root.geometry("420x420")  # Window size
root.config(bg="#FCE4EC")  # Background color

# Random quote display kro
random_quote = random.choice(fun_quotes)
quote_label = tk.Label(root, text=random_quote, font=("Helvetica", 10, "italic"), bg="#FCE4EC", fg="#666")
quote_label.pack(pady=(10, 0))

# Welcome text
welcome_label = tk.Label(root, text="🎵 Select Your Mood 🎵", font=("Helvetica", 16, "bold"), bg="#FCE4EC", fg="#333")
welcome_label.pack(pady=15)

# Button style define kro
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12, "bold"), padding=5)

# Mood Buttons
btn_romantic = ttk.Button(root, text="Romantic ❤", command=lambda: show_songs("Romantic"))
btn_romantic.pack(pady=5)

btn_emotional = ttk.Button(root, text="Emotional 💔", command=lambda: show_songs("Emotional"))
btn_emotional.pack(pady=5)

btn_energetic = ttk.Button(root, text="Energetic ⚡", command=lambda: show_songs("Energetic"))
btn_energetic.pack(pady=5)

btn_relaxing = ttk.Button(root, text="Relaxing 😌", command=lambda: show_songs("Relaxing"))
btn_relaxing.pack(pady=5)

btn_dance = ttk.Button(root, text="Dance 🪩", command=lambda: show_songs("Dance"))
btn_dance.pack(pady=5)

btn_devotional = ttk.Button(root, text="Devotional 🔱", command=lambda: show_songs("Devotional"))
btn_devotional.pack(pady=5)

btn_retro = ttk.Button(root, text="Retro 📀", command=lambda: show_songs("Retro"))
btn_retro.pack(pady=5)

btn_flirty = ttk.Button(root, text="Flirty 🌝", command=lambda: show_songs("Flirty"))
btn_flirty.pack(pady=5)

btn_travel = ttk.Button(root, text="Travel ✈", command=lambda: show_songs("Travel"))
btn_travel.pack(pady=5)

btn_lofi = ttk.Button(root, text="Lofi 🎶", command=lambda: show_songs("Lofi"))
btn_lofi.pack(pady=5)

# Songs show krne k liye Textbox & Scrollbar
text_frame = tk.Frame(root, bg="#FCE4EC")
text_frame.pack(pady=10)

scrollbar = Scrollbar(text_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

songs_text = tk.Text(text_frame, height=8, width=40, font=("Helvetica", 10),
                     yscrollcommand=scrollbar.set, wrap="word")
songs_text.pack(side=tk.LEFT)

scrollbar.config(command=songs_text.yview)

# Spotify Playlist k liye link label
link_label = tk.Label(root, text="", font=("Helvetica", 11, "underline"), bg="#FCE4EC")
link_label.pack(pady=5)

# App Run
root.mainloop()
