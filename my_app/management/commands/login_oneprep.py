import time
from django.core.management.base import BaseCommand
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Command(BaseCommand):
    help = "Automates login to OnePrep"

    def handle(self, *args, **kwargs):
        # Initialize WebDriver
        driver = webdriver.Chrome()  # Ensure chromedriver is in PATH

        try:
            # Open the login page
            driver.get("https://oneprep.xyz/accounts/login/")
            time.sleep(2)  # Allow page to load

            # Find username and password fields
            username_field = driver.find_element(By.NAME, "login")  # Finds the login input field

            password_field = driver.find_element(By.NAME, "password")

            # Enter credentials
            username_field.send_keys("sydulamin")
            password_field.send_keys("aminamin")
            password_field.send_keys(Keys.RETURN)

            time.sleep(5)  # Wait for login response

            # Check login status
            if "dashboard" in driver.current_url or "logout" in driver.page_source:
                self.stdout.write(self.style.SUCCESS("Login successful!"))
            else:
                self.stdout.write(self.style.ERROR("Login failed!"))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error: {e}"))

        finally:
            driver.quit()  # Close the browser
