# main.py

from flask import Flask, jsonify
# from selenium import webdriver
import chromedriver_binary  # Adds chromedriver binary to path
from OpenPlayInteractor import OpenPlayInteractor

app = Flask(__name__)

# The following options are required to make headless Chrome
# work in a Docker container
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--disable-gpu")
# chrome_options.add_argument("window-size=1024,768")
# chrome_options.add_argument("--no-sandbox")

# Initialize a new browser
# browser = webdriver.Chrome(chrome_options=chrome_options)


@app.route("/")
def hello_world():
    open_play_interactor = OpenPlayInteractor()
    court_avails = open_play_interactor.all_court_availabilities()
    court_avails_json = court_avails.to_json(orient='records')
    return jsonify(court_avails_json)
