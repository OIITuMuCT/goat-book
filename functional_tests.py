from selenium import webdriver

browser = webdriver.Firefox()
browser.get("http://localhost:8000")

# She notices the page title and header mention to-to lists
assert "To-Do" in browser.title, f" Browser title was {browser.title}"

browser.quit()