from flask import Flask, request, jsonify
from bs4 import BeautifulSoup
from flask_cors import CORS
import requests
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from discount import extract_flipkart_info
from timer_scarcity import check_timer_changes_within_duration
from fake_review import analyze_reviews
from urgency import urgency_check


app = Flask(__name__)
CORS(app)

@app.route('/run_python_code', methods=['GET', 'POST'])
def run_python_code():
    try:
        data = request.get_json()
        product_url = data.get('product_url', '')
         
        timer_result = check_timer_changes_within_duration(product_url)

        price_info = extract_flipkart_info(product_url)

        analysis_result = analyze_reviews(product_url)

        urgency_info = urgency_check(product_url)
       
        return jsonify({"price_info": price_info, "timer_result": timer_result,"analysis_result":analysis_result,"urgency_info":urgency_info})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=7000)