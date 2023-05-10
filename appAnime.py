import requests
from bs4 import BeautifulSoup
import streamlit as st
import time

# Define the CSP
csp = """
<meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'self' 'unsafe-inline'">
"""


def run_script(url, provider):
    # Check that URL is valid
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
        }
        response = requests.get(url, headers=headers)
        print(f"Status Code: {response.status_code}") # Print the status code
        st.warning(f"Status Code: {response.status_code}") # Print the status code
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

        # Loop through each episode URL and create a card for each
        cards = []
        for episode_link in episode_links:
            episode_url = episode_link["href"]

            # Make a GET request to the episode page
            try:
                time.sleep(10)
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

                # Create card for episode
                card = f"""
                    <div class="card">
                        <div class="card-header">
                            Episode {episode_num}
                        </div>
                        <div class="card-body">
                            <h5 class="card-title">{anime_name}</h5>
                            <p class="card-text">Download Link: <a href="{download_link}" target="_blank">{download_link}</a></p>
                        </div>
                    </div>
                """
                cards.append(card)

        # Show the cards in Streamlit
        st.markdown(csp + ' '.join(cards), unsafe_allow_html=True)

#Define the Streamlit app
def app():
    st.set_page_config(page_title="Anime Downloader", page_icon="🎬")
    st.title("Anime Downloader")
    # Show input field for URL
    url = st.text_input("Enter the URL of the anime you want to download:")

    # Show radio buttons for provider selection
    provider = st.radio("Select the provider:", ["mega", "google", "mediafire"])

    # Show button to start downloading
    if st.button("Download Episodes"):
        run_script(url, provider)



if __name__ == "__main__":
    app()

