import pyshorteners
import sqlite3
import string
import random
import webbrowser

def shorten_tinyurl_url(url):
    try:
        s = pyshorteners.Shortener()
        return s.tinyurl.short(url)
    except pyshorteners.exceptions.ShorteningErrorException as e:
        print(f"Error occurred while shortening URL: {e}")
        return None

def create_shortened_url(long_url):
    # Generate a random alphanumeric string as the short URL
    short_url = ''.join(random.choices(string.ascii_letters + string.digits, k=6))

    # Store the mapping between the long and short URLs in a database
    conn = sqlite3.connect("url_shortener.db")
    cursor = conn.cursor()

    # Create the table if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS url_mapping (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        long_url TEXT NOT NULL,
                        short_url TEXT NOT NULL)''')

    # Check if the long URL is already in the database
    cursor.execute("SELECT short_url FROM url_mapping WHERE long_url = ?", (long_url,))
    existing_short_url = cursor.fetchone()

    if existing_short_url:
        # If the long URL is already in the database, return the existing short URL
        conn.close()
        return existing_short_url[0]
    else:
        # If the long URL is not in the database, insert the mapping and return the new short URL
        cursor.execute("INSERT INTO url_mapping (long_url, short_url) VALUES (?, ?)", (long_url, short_url))
        conn.commit()
        conn.close()

        # Open the long URL in the default web browser when the shortened URL is accessed
        webbrowser.open(long_url)

        return short_url

def retrieve_shortened_url(short_url):
    # Retrieve the long URL associated with the provided short URL from the database
    conn = sqlite3.connect("url_shortener.db")
    cursor = conn.cursor()

    cursor.execute("SELECT long_url FROM url_mapping WHERE short_url = ?", (short_url,))
    long_url = cursor.fetchone()

    conn.close()

    if long_url:
        return long_url[0]
    else:
        return None

def main():
    print("URL Shortener Menu:")
    print("1. Shorten URL using TinyURL")
    print("2. Shorten URL using SQLite-based Custom Shortener")
    print("3. Retrieve Long URL from Short URL")
    print("4. Exit")

    while True:
        choice = input("Enter your choice (1/2/3/4): ")
        
        if choice == "1":
            url = input("Enter the URL to shorten: ")
            shortened_url = shorten_tinyurl_url(url)
            if shortened_url:
                print(f"The Shortened URL: {shortened_url}")
        elif choice == "2":
            url = input("Enter the URL to shorten: ")
            shortened_url = create_shortened_url(url)
            if shortened_url:
                print(f"The Shortened URL: {shortened_url}")
        elif choice == "3":
            url = input("Enter the Short URL to retrieve the Long URL: ")
            long_url = retrieve_shortened_url(url)
            if long_url:
                print(f"The Long URL: {long_url}")
            else:
                print("Short URL not found.")
        elif choice == "4":
            print("Exiting the URL Shortener.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
