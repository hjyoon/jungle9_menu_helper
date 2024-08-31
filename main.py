import sys
import os
import re
import requests
from datetime import datetime, timezone, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv


def remove_numbers_and_commas(food_list):
    cleaned_list = []
    for food in food_list:
        cleaned_food = re.sub(r"[0-9,]+$", "", food)
        cleaned_list.append(cleaned_food)
    return cleaned_list


def main():
    load_dotenv()

    kst_timezone = timezone(timedelta(hours=9))
    today_kst = datetime.now(kst_timezone).date().isoformat()

    url = 'https://www.kaist.ac.kr/kr/html/campus/053001.html?dvs_cd=icc&stt_dt=' + today_kst

    options = webdriver.FirefoxOptions()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)

    driver.get(url)

    menu_type = sys.argv[1]

    if menu_type == "breakfast":
        nth = 1
        menu_type = "아침"
    elif menu_type == "lunch":
        nth = 2
        menu_type = "점심"
    elif menu_type == "dinner":
        nth = 3
        menu_type = "저녁"
    else:
        exit(-1)

    selector = f"#tab_item_1 > table > tbody > tr > td:nth-child({nth})"

    menu = driver.find_element(by=By.CSS_SELECTOR, value=selector).text
    menu = remove_numbers_and_commas(menu.split())
    menu = ', '.join(menu) if len(menu) > 0 else '오늘은 운영하지 않습니다.'

    driver.quit()

    webhook_url = os.getenv("WEBHOOK_URL")
    payload = {
        "blocks": [
            {
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": f"오늘의 {menu_type} 메뉴",
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": menu,
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"<{url}|상세정보>",
                }
            },
        ],
    }
    requests.post(webhook_url, json=payload)


if __name__ == "__main__":
    main()
