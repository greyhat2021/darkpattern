import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

def extract_flipkart_info(url):
    
    chromedriver_path = 'F:\\chromedriver-win64\\chromedriver-win64'

    
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument(f'--executable_path={chromedriver_path}')
    chrome_options.add_argument('--headless')  # Add this line for headless mode
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Open the Flipkart URL
        driver.get(url)

        # Wait for the price-info-icon to be clickable
        price_info_icon = driver.find_element(by=By.ID, value='price-info-icon')

        # Click the price-info-icon using ActionChains
        price_info_icon.click()
        time.sleep(0.5)
        price_info_icon.click()

        # Wait for the overlay to appear
        overlay = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, '_1C5V67'))
        )

        # Extract Maximum Retail Price
        mrp = overlay.find_element(By.XPATH, "//div[text()='Maximum Retail Price']/following-sibling::div").text.strip()

        # Extract Selling Price
        selling_price = overlay.find_element(By.XPATH, "//div[text()='Selling Price']/following-sibling::div").text.strip()

        # Extract Special Price
        special_price = overlay.find_element(By.XPATH, "//div[text()='Special Price']/following-sibling::div").text.strip()

        # Remove the ₹ symbol and convert to float
        mrp = float(mrp.replace('₹', '').strip())
        selling_price = float(selling_price.replace('₹', '').strip())
        special_price = float(special_price.replace('₹', '').strip())

        # Calculate the discount amount and percentage
        discount_amount = selling_price - special_price
        discount_percentage = (discount_amount / selling_price) * 100

        # Extract Given Discount Percentage from the webpage
        given_discount_percentage_element = driver.find_element(By.CLASS_NAME, '_3Ay6Sb._31Dcoz')
        given_discount_percentage = given_discount_percentage_element.find_element(By.TAG_NAME, 'span').text.strip()

        # Convert the extracted percentage to float
        given_discount_percentage = float(given_discount_percentage.replace('% off', '').strip())

        # Return the results as a dictionary
        result = {
            "Maximum Retail Price": mrp,
            "Selling Price": selling_price,
            "Special Price": special_price,
            "Discount Amount": discount_amount,
            "Discount Percentage": discount_percentage,
            "Given Discount Percentage": given_discount_percentage
        }

        return result

    finally:
        # Close the browser window
        driver.quit()