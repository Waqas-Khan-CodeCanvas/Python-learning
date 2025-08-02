from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

# Path to your ChromeDriver (make sure it's correctly placed and matches your Chrome version)
driver_path = "chromedriver.exe"

# Set up the WebDriver service
service = Service("C:/Users/DECENT LAPTOPS/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Python 3.9/chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Open WhatsApp Web
driver.get("https://web.whatsapp.com/")
input("Scan the QR code and press Enter...")  # Wait for manual login

# Your friend's name (must be saved in contacts)
friend_name = "Friend Name"  # Replace with actual name or phone number

# List of messages to send
messages = [
    "Hello! How are you?",
    "Just checking in!",
    "Hope you have a great day!",
    "Take care!"
]

# Search for the contact
search_box = driver.find_element(By.XPATH, "//div[@contenteditable='true']")
search_box.click()
search_box.send_keys(friend_name)
time.sleep(2)
search_box.send_keys(Keys.ENTER)
time.sleep(2)

# Sending messages one by one
for message in messages:
    msg_box = driver.find_element(By.XPATH, "//div[@title='Type a message']")
    msg_box.send_keys(message)
    msg_box.send_keys(Keys.ENTER)
    time.sleep(2)  # Small delay to avoid detection

print("Messages sent successfully!")

# Close the browser after sending messages
time.sleep(5)
driver.quit()
