import tkinter as tk
from tkinter import messagebox
import requests

def get_lyrics(artist, title):
    # Format the URL for the Lyrics.ovh API
    api_url = f'https://api.lyrics.ovh/v1/{artist}/{title}'

    # Make a GET request to the API
    response = requests.get(api_url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Check if lyrics are available
        if 'lyrics' in data:
            return data['lyrics']
        else:
            return "Lyrics not found for the given song."
    else:
        return "Error fetching lyrics. Please check the artist and title."

def display_lyrics():
    # Get the artist and title from the entry widgets
    artist = artist_entry.get()
    title = title_entry.get()

    # Get the lyrics using the get_lyrics function
    lyrics = get_lyrics(artist, title)

    # Display the lyrics in a message box
    messagebox.showinfo("Lyrics", lyrics)

# Create the main window
root = tk.Tk()
root.title("Lyrics Finder")

# Create and place the labels and entry widgets
tk.Label(root, text="Artist:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
artist_entry = tk.Entry(root)
artist_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Title:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
title_entry = tk.Entry(root)
title_entry.grid(row=1, column=1, padx=5, pady=5)

# Create and place the search button
search_button = tk.Button(root, text="Search", command=display_lyrics)
search_button.grid(row=2, columnspan=2, padx=5, pady=5)

# Start the Tkinter event loop
root.mainloop()

