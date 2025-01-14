# Letterboxd Follower Bot

This Python script uses Selenium to automatically follow users on Letterboxd who have liked horror or thriller films that you have also liked. 

**The bot logs into your Letterboxd account** using credentials that you provide. **It then navigates to your profile and finds a list of all the films you have liked**.  The script **filters this list to only include horror and thriller films** by examining the genres listed for each film [1]. 

For each horror or thriller film you have liked, **the bot navigates to that film's page and finds all the users who have liked that film** [2]. It then iterates through multiple pages of users who have liked the film [3]. **For each user, the bot clicks the "Follow" button**, thereby automatically following that user [2]. The script includes a short delay after clicking each "Follow" button to avoid overwhelming the Letterboxd server [2].


## Libraries Used

This script uses several libraries to interact with web pages and automate tasks:

*   **Selenium:** This library is used to automate web browsers [4]. It allows the script to open web pages, interact with elements on those pages (such as clicking buttons and filling in forms [5]), and extract data from those pages. Selenium is used in this script to open Letterboxd, log in, navigate to various pages, find the follow buttons for different users, and click those buttons.

*   **WebDriver:** This is a component of Selenium that controls a specific web browser [4]. The script uses the ChromeDriver to control the Chrome browser. You can replace this with other WebDriver implementations to use different browsers.

*   **ActionChains:** This class from Selenium is used to perform complex actions, like mouse movements and button clicks. However, the current script uses `driver.execute_script("arguments.click();", button)` instead of the ActionChains class to click the follow buttons [2].

*   **WebDriverWait and expected\_conditions:** These components are used to wait for specific conditions on a web page before continuing the script [4]. In this case, they are used to wait for elements, such as the follow buttons, to be loaded and visible on the page [1]. This ensures that the script doesn't try to interact with elements that aren't yet available.

*   **time:** The `time.sleep()` function from this library is used to pause the script for a set amount of time [2]. This is helpful for avoiding overwhelming the Letterboxd server with requests and for letting the page load properly before the script tries to interact with it.

In addition to these libraries, the script uses standard Python libraries like `By` to locate elements on web pages using various methods [4, 5] and common modules for handling user input and exceptions. 
