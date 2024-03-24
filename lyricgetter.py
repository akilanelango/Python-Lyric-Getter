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

def main():
    # Get user input for the song title and artist
    title = input("Enter the title of the song: ")
    artist = input("Enter the name of the artist: ")

    # Get and display the lyrics
    lyrics = get_lyrics(artist, title)
    print("\nLyrics:\n")
    print(lyrics)

if __name__ == "__main__":
    main()