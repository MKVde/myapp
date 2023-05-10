import requests
from bs4 import BeautifulSoup
import streamlit as st


def run_script(url, provider):
    # Check that URL is valid
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException:
        st.warning("No URL or Invalid URL. Please enter a valid URL.")
        return

    # Show loading spinner
    with st.spinner(text="Loading..."):
        # Use BeautifulSoup to parse the response HTML
        soup = BeautifulSoup(response.text, "html.parser")

        # Find all the episode links on the page
        episode_links = soup.select(".episodes-card-title a")

        # Extract anime name from URL
        anime_name = url.split('/')[-2].replace('-', ' ')

        # Initialize the table with headers
        st.write(f"## Episodes for {anime_name}")
        st.write("")
        st.write("| Episode Number | Download Link |")
        st.write("| --- | --- |")

        # Loop through each episode URL
        for episode_link in episode_links:
            episode_url = episode_link["href"]

            # Make a GET request to the episode page
            try:
                response = requests.get(episode_url)
                response.raise_for_status()
            except requests.exceptions.RequestException:
                st.warning("Failed to retrieve episode data. Please check your internet connection and try again.")
                return

            # Parse the HTML using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find all HTML elements containing the provider link
            provider_links = soup.find_all('a', href=lambda href: href and provider in href)

            # Extract the second link from the list of provider links
            if len(provider_links) >= 2:
                download_link = provider_links[1]['href']
                episode_num = episode_link.text.split(' ')[-1]
                
                # Add the row to the table
                st.write(f"| {episode_num} | [{provider.capitalize()}]({download_link}) |")

# Create Streamlit UI
st.title("Anime Downloader")

# Get user input values
url = st.text_input("Enter URL:")
provider = st.selectbox("Provider:", ["mega", "google", "mediafire"])

# Run the script when the "Download" button is clicked
if st.button("Run"):
    run_script(url, provider)
