# import openai

# # Replace YOUR_API_KEY with your actual API key
# openai.api_key = "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"

# # Make a test API request
# response = openai.Completion.create(engine="davinci", prompt="Hello, World!", max_tokens=5)

# # Check if the API request was successful
# if response["object"] == "error":
#     print("Error:", response["error"]["message"])
# else:
#     print("API key is working!")


# import requests
# from bs4 import BeautifulSoup
# import streamlit as st
# import pandas as pd

# def remove_dash(anime_name):
#     """
#     Removes any dashes in an anime name
#     """
#     return anime_name.replace('-', ' ')


# def run_script(url, provider):
#     # Check that URL is valid
#     try:
#         response = requests.get(url)
#         response.raise_for_status()
#     except requests.exceptions.RequestException:
#         st.warning("No URL or Invalid URL. Please enter a valid URL.")
#         return

#     # Show loading spinner
#     with st.spinner(text="Loading..."):
#         # Use BeautifulSoup to parse the response HTML
#         soup = BeautifulSoup(response.text, "html.parser")

#         # Find all the episode links on the page
#         episode_links = soup.select(".episodes-card-title a")

#         # Extract anime name from URL
#         anime_name = url.split('/')[-2]
#         anime_name = remove_dash(anime_name)

#         # Loop through each episode URL
#         rows = []
#         for episode_link in episode_links:
#             episode_url = episode_link["href"]

#             # Make a GET request to the episode page
#             try:
#                 response = requests.get(episode_url)
#                 response.raise_for_status()
#             except requests.exceptions.RequestException:
#                 st.warning("Failed to retrieve episode data. Please check your internet connection and try again.")
#                 return

#             # Parse the HTML using BeautifulSoup
#             soup = BeautifulSoup(response.text, 'html.parser')

#             # Find all HTML elements containing the provider link
#             provider_links = soup.find_all('a', href=lambda href: href and provider in href)

#             # Extract the second link from the list of provider links
#             if len(provider_links) >= 2:
#                 download_link = provider_links[1]['href']
#                 episode_num = episode_link.text.split(' ')[-1]
            
#                 download_button = f"<a href='{download_link}' target='_blank'><button>Download Episode {episode_num}</button></a>"
                

#                 # Add the anime name, episode number, and download link to the rows list
#                 row = {"Anime Name": anime_name, "E": episode_num, "Extracted Links": download_link, "Button": download_button}
#                 rows.append(row)

#         # Create a DataFrame from the rows list
#         df = pd.DataFrame(rows)

#         # Set the width of the "Anime Name" column to fit the full content of the cell
#         df.style.set_properties(**{'text-align': 'center'})
#         df.style.set_properties(subset=["Anime Name"], **{'width': '100%'})

        
#         # Show the DataFrame in Streamlit
#         st.dataframe(df)


# # Create Streamlit UI
# st.title("Anime Downloader")

# # Get user input values
# url = st.text_input("Enter URL:")
# provider = st.selectbox("Provider:", ["mega", "google", "mediafire"])

# # Run the script when the "Download" button is clicked
# if st.button("Run"):
#     run_script(url, provider)






# import streamlit as st
# import pandas as pd
# import requests
# from bs4 import BeautifulSoup

# def remove_dash(anime_name):
#     """
#     Removes any dashes in an anime name
#     """
#     return anime_name.replace('-', ' ')

# def run_script(url, provider):
#     # Check that URL is valid
#     try:
#         response = requests.get(url)
#         response.raise_for_status()
#     except requests.exceptions.RequestException:
#         st.warning("No URL or Invalid URL. Please enter a valid URL.")
#         return

#     # Show loading spinner
#     with st.spinner(text="Loading..."):
#         # Use BeautifulSoup to parse the response HTML
#         soup = BeautifulSoup(response.text, "html.parser")

#         # Find all the episode links on the page
#         episode_links = soup.select(".episodes-card-title a")

#         # Extract anime name from URL
#         anime_name = url.split('/')[-2]
#         anime_name = remove_dash(anime_name)

#         # Loop through each episode URL
#         rows = []
#         for episode_link in episode_links:
#             episode_url = episode_link["href"]

#             # Make a GET request to the episode page
#             try:
#                 response = requests.get(episode_url)
#                 response.raise_for_status()
#             except requests.exceptions.RequestException:
#                 st.warning("Failed to retrieve episode data. Please check your internet connection and try again.")
#                 return

#             # Parse the HTML using BeautifulSoup
#             soup = BeautifulSoup(response.text, 'html.parser')

#             # Find all HTML elements containing the provider link
#             provider_links = soup.find_all('a', href=lambda href: href and provider in href)

#             # Extract the second link from the list of provider links
#             if len(provider_links) >= 2:
#                 download_link = provider_links[1]['href']
#                 episode_num = episode_link.text.split(' ')[-1]
            
#                 download_button = f"<a href='{download_link}' target='_blank'><button class='download-button'>Download Episode {episode_num}</button></a>"
                

#                 # Add the anime name, episode number, and download link to the rows list
#                 row = {"Anime Name": anime_name, "E": episode_num, "Extracted Links": download_link, "Button": download_button}
#                 rows.append(row)

#         # Create a DataFrame from the rows list
#         df = pd.DataFrame(rows)

#         # Set the width of the "Anime Name" column to fit the full content of the cell
#         df.style.set_properties(**{'text-align': 'center'})
#         df.style.set_properties(subset=["Anime Name"], **{'width': '100%'})

#         # Apply custom CSS styling to the results table
#         st.markdown("""
#             <style>
#                 .dataframe {
#                     font-size: 14px;
#                     text-align: center;
#                     border-collapse: collapse;
#                     margin: 20px 0;
#                     background-color: #fff;
#                     box-shadow: 0 0 20px rgba(0, 0, 0, 0.15);
#                 }

#                 .dataframe th, .dataframe td {
#                     padding: 12px 15px;
#                     border: 1px solid #e5e5e5;
#                 }

#                 .dataframe th {
#                     font-size: 16px;
#                     font-weight: bold;
#                     background-color: #f2f2f2;
#                     color: #333;
#                     text-transform: uppercase;
#                 }

#                 .dataframe td {
#                     font-size: 14px;
#                     color: #666;
#                 }

#                 .dataframe tr:nth-child(even) {
#                     backgroundcolor: #f9f9f9;
                
#                 .download-button {
#                     background-color: #4CAF50; /* Green */
#                     border: none;
#                     color: white;
#                     padding: 10px 24px;
#                     text-align: center;
#                     text-decoration: none;
#                     display: inline-block;
#                     font-size: 14px;
#                     margin: 4px 2px;
#                     cursor: pointer;
#                     border-radius: 5px;
#                 }
#             </style>
#         """, unsafe_allow_html=True)

#         # Display the results DataFrame
#         st.write(df)

    
# def main():
#     # Set the app title
#     st.set_page_config(page_title="Anime Episode Downloader", page_icon=":tv:", layout="wide")
#     # Add a title and description
#     st.title("Anime Episode Downloader")
#     st.write("This app allows you to download episodes of your favorite anime from selected providers.")

#     # Create a form to get the user input
#     form = st.form(key='my_form')
#     url = form.text_input('Enter URL:')
#     provider = form.selectbox('Select Provider:', ['Gogoanime', '4anime'])

#     if form.form_submit_button():
#         # Run the script with the user input
#         run_script(url, provider)

# if __name__ == "__name__":
#     main()







# BEST RESULT i CAN GET!!!!!!!!!!!!

# import requests
# from bs4 import BeautifulSoup
# import streamlit as st

# def run_script(url, provider):
#     # Check that URL is valid
#     try:
#         response = requests.get(url)
#         response.raise_for_status()
#     except requests.exceptions.RequestException:
#         st.warning("No URL or Invalid URL. Please enter a valid URL.")
#         return

#     # Show loading spinner
#     with st.spinner(text="Loading..."):
#         # Use BeautifulSoup to parse the response HTML
#         soup = BeautifulSoup(response.text, "html.parser")

#         # Find all the episode links on the page
#         episode_links = soup.select(".episodes-card-title a")

#         # Extract anime name from URL
#         anime_name = url.split('/')[-2].replace('-', ' ')

#         # Loop through each episode URL and create a card for each
#         cards = []
#         for episode_link in episode_links:
#             episode_url = episode_link["href"]

#             # Make a GET request to the episode page
#             try:
#                 response = requests.get(episode_url)
#                 response.raise_for_status()
#             except requests.exceptions.RequestException:
#                 st.warning("Failed to retrieve episode data. Please check your internet connection and try again.")
#                 return

#             # Parse the HTML using BeautifulSoup
#             soup = BeautifulSoup(response.text, 'html.parser')

#             # Find all HTML elements containing the provider link
#             provider_links = soup.find_all('a', href=lambda href: href and provider in href)

#             # Extract the second link from the list of provider links
#             if len(provider_links) >= 2:
#                 download_link = provider_links[1]['href']
#                 episode_num = episode_link.text.split(' ')[-1]

#                 # Create card for episode
#                 card = f"""
#                     <div class="card">
#                         <div class="card-header">
#                             Episode {episode_num}
#                         </div>
#                         <div class="card-body">
#                             <h5 class="card-title">{anime_name}</h5>
#                             <p class="card-text">Download Link: <a href="{download_link}" target="_blank">{download_link}</a></p>
#                         </div>
#                     </div>
#                 """
#                 cards.append(card)

#         # Show the cards in Streamlit
#         st.markdown(' '.join(cards), unsafe_allow_html=True)

# # Create Streamlit UI
# st.set_page_config(page_title="Anime Downloader", page_icon="📺")
# st.title("Anime Downloader")

# # Get user input values
# url = st.text_input("Enter URL:")
# provider = st.selectbox("Provider:", ["mega", "google", "mediafire"])

# # Run the script when the "Download" button is clicked
# if st.button("Download Episodes"):
#     run_script(url, provider)




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
