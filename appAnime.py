import time
import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import undetected_chromedriver.v2 as uc


def run_script(url, provider):
    # Check that URL is valid
    try:
        driver.get(url)
    except TimeoutException:
        st.warning("No URL or Invalid URL. Please enter a valid URL.")
        return

    # Show loading spinner
    with st.spinner(text="Loading..."):
        # Find all the episode links on the page
        try:
            episode_links = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located(
                    (By.CSS_SELECTOR, ".episodes-card-title a")
                )
            )
        except TimeoutException:
            st.warning("Failed to retrieve episode data. Please check your internet connection and try again.")
            return

        # Extract anime name from URL
        anime_name = url.split('/')[-2].replace('-', ' ')

        # Initialize the table with headers
        st.write(f"## Episodes for {anime_name}")
        st.write("")
        st.write("| Episode Number | Download Link |")
        st.write("| --- | --- |")

        # Loop through each episode URL
        for episode_link in episode_links:
            episode_url = episode_link.get_attribute("href")

            # Make a GET request to the episode page
            try:
                driver.get(episode_url)
            except TimeoutException:
                st.warning("Failed to retrieve episode data. Please check your internet connection and try again.")
                return

            # Find all HTML elements containing the provider link
            try:
                provider_links = WebDriverWait(driver, 10).until(
                    EC.presence_of_all_elements_located(
                        (By.XPATH, f"//a[contains(@href,'{provider}')]")
                    )
                )
            except TimeoutException:
                st.warning("Failed to retrieve episode data. Please check your internet connection and try again.")
                return

            # Extract the second link from the list of provider links
            if len(provider_links) >= 2:
                download_link = provider_links[1].get_attribute("href")
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
    # Set up undetected ChromeDriver
    options = uc.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = uc.Chrome(options=options)
    driver.delete_all_cookies()

    # Run the script
    run_script(url, provider)

    # Quit the driver
    driver.quit()
