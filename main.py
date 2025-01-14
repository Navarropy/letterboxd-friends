from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the Selenium WebDriver
driver = webdriver.Chrome()  # Use ChromeDriver, or replace with your preferred driver
wait = WebDriverWait(driver, 10)

# Open the Letterboxd website
driver.get("https://letterboxd.com/")

driver.find_element(By.XPATH, '//*[@id="header"]/section/div[1]/div/nav/ul/li[1]/a/span[2]').click()
driver.find_element(By.XPATH, '//*[@id="username"]').send_keys(input("Enter your username: "))
driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(input("Enter your password: "))
driver.find_element(By.XPATH, '//*[@id="signin"]/fieldset/div/div[4]/div[1]/input').click()

try:
    while True:
        # Wait for the element to appear on the main page
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div[3]/h1')))

        driver.get("https://letterboxd.com/orbitred/likes/films/")
        
        # # Collect the movie links
        movie_links = driver.find_elements(By.XPATH, '//a[@class="frame has-menu"]')
        movie_links = [element.get_attribute("href") for element in movie_links]

        for movie_url in movie_links:

            # Iterate through each movie
            driver.get(movie_url + "genres/")
            
            # Check if genres include "Thriller" or "Horror"
            genres = driver.find_elements(By.XPATH, '//*[@class="text-sluglist capitalize"]//*[@class="text-slug"]')
            genre_texts = [genre.text for genre in genres]
            
            if "Thriller" in genre_texts or "Horror" in genre_texts:
                # Go to the original movie URL + "/likes/page/1/"
                current_page = 1
                
                while True:
                    likes_url = movie_url + f"likes/page/{current_page}/"
                    driver.get(likes_url)

                    # Find all follow buttons that are visible
                    follow_buttons = driver.find_elements(By.XPATH, '//*[@data-recaptcha-action="follow" and not(@style="display: none;")]')
                    
                    # Click all follow buttons using JavaScript
                    for button in follow_buttons:
                        driver.execute_script("arguments[0].click();", button)
                        time.sleep(0.5)
                
                    # Check if there's a next page
                    try:
                        next_page = driver.find_element(By.XPATH, '//*[@id="content"]/div/div/section/div[2]/div[2]/a')
                        current_page += 1
                    except:
                        # No next page, break the loop
                        break

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    driver.quit()
