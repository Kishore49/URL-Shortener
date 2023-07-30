# URL-Shortener


This is a simple command-line URL shortener application written in Python. It allows users to shorten URLs using two methods: 
TinyURL API and a custom SQLite-based URL shortener.

Features:


Shorten URL using TinyURL API: The application uses the TinyURL API to shorten the given long URL. If the shortening process is successful, it provides the shortened URL as output.

Shorten URL using SQLite-based Custom Shortener: The application also provides a custom URL shortening method using SQLite-based storage. It generates a random alphanumeric short URL for the given long URL and stores the mapping in an SQLite database. 
If the long URL is already in the database, it returns the existing short URL. Otherwise, it creates a new mapping and returns the newly generated short URL.

Retrieve Long URL from Short URL: The application allows users to retrieve the original long URL associated with a previously shortened URL from the custom SQLite-based shortener.

Dependencies:


The application requires the following dependencies:

pyshorteners: A Python library for URL shortening using various services. 
Install it using: pip install pyshorteners

Usage:


Clone the repository or download the "url_shortener_.py" file.

Make sure you have the required dependencies installed.

Run the script: "python url_shortener_.py"

The application will display a menu with options for URL shortening and retrieval.

Usage Examples:


URL Shortener Menu:
1. Shorten URL using TinyURL
2. Shorten URL using SQLite-based Custom Shortener
3. Retrieve Long URL from Short URL
4. Exit

Enter your choice (1/2/3/4): ("Enter your choice")
Enter the URL to shorten: Enter the URL to be shortened

The Shortened URL: The Shortend URL will be displayed

Note:

The application uses SQLite to store the custom short URL mappings in a file named url_shortener.db. 
Make sure you have write permissions for the directory where the script is located.

The TinyURL API might have rate limits, so excessive use of the TinyURL shortening method may result in temporary blocks. 
Use it responsibly.

Author:


Kishore Kumar - kingkishore4907@gmail.com
