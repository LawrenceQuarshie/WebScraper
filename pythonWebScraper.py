# import Playwright
import os.path
import re
from datetime import datetime
from playwright.sync_api import sync_playwright

prodURL = 'https://www.amazon.com/Apple-iPhone-Pro-Max-trade/dp/B0CHBNYL5L/ref=sr_1_3?crid=1K2KR026GSV51&keywords=15+pro+max&qid=1700560714&sprefix=15+pro+%2Caps%2C112&sr=8-3'

with sync_playwright() as playw:
    browser = playw.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(prodURL)