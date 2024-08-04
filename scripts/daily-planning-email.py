import json
import os
from datetime import datetime, timedelta

import requests
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Email, To, Bcc, HtmlContent


load_dotenv()
api_key = os.getenv('API_KEY')
# Raise an error if API_KEY is not set in the environment variables.
if not api_key:
    raise ValueError("API_KEY is not set in the environment variables.")

sg = SendGridAPIClient(api_key=api_key)
# from_email = Email("coretechs.twilio@coretechs.com")
from_email = Email("FROM_EMAIL_ADDRESS")


def fetch_data(url):
    """
     Fetch data from a URL. This is a wrapper around requests. get that handles authentication
     
     @param url - URL to fetch data from
     
     @return JSON data from the URL Raises exception if something goes
    """
    response = requests.get(url, auth=HTTPBasicAuth("why?", "whynot!"))
    # Returns the JSON response body.
    if response.status_code == 200:
        return response.json()

    raise Exception(f"Failed to fetch data: {response.status_code} - {response.content}")

def send_email(data, date_str):
    """
     Send email to RECEIVE_EMAIL_ADDRESS and BCC_EMAIL_ADDRESS
     
     @param data - list of data to send
     @param date_str - date of data to send ( YYYYMMDD
    """
    to_emails = [To("RECEIVE_EMAIL_ADDRESS")]
    bcc_emails = Bcc("BCC_EMAIL_ADDRESS")
    subject = f"???????????????????????? - {date_str} - Count: {len(data)}"
    html_content_str = f"""
    <html>
    <head>
        <style>
            .card {{
                display: inline-block;
                margin: 10px;
                width: 200px;
                border: 1px solid #ccc;
                border-radius: 5px;
                padding: 10px;
                text-align: center;
            }}
            .card img {{
                width: 100px;
                border-radius: 50%;
            }}
            .image-wrapper.circle {{
                width: 150px;
                height: 150px;
                margin: 0 auto; /* Centers the circle horizontally */
                display: flex;
                align-items: center; /* Centers content vertically */
                justify-content: center; /* Centers content horizontally */
                -webkit-border-radius: 50%;
                -moz-border-radius: 50%;
                border-radius: 50%;
                background-size: cover; /* Cover the entire area of the circle */
                background-position: center; /* Center the background image */
                overflow: hidden; /* Hide anything outside the circle */
                border: none;
            }}
            .image-wrapper.circle img {{   
                max-width: 100%;
                max-height: 100%;
                object-fit: cover; /* This will cover the area without losing the aspect ratio */
            }}


        </style>
    </head>
    <body>
        <a href="THE_LINK" style="background-color: #4CAF50; color: white; padding: 10px 20px; text-align: center; text-decoration: none; display: inline-block; font-size: 16px; margin: 4px 2px; cursor: pointer; border-radius: 12px;">LINK_DESCRIPTION</a>
        <h1>{subject}</h1>
        <div class="card-container">"""

    # Generates the HTML for the person
    for person in data:
        image_url = "EXCEPTION_IMAGE" if person['name'] == "EXCEPTION_USER_NAME" else person['image']
        html_content_str += f""" <div class="card">
        <div class="image-wrapper circle" style="background-image: url({image_url});"></div>
        <p>{person['name']}</p>
    </div> """
    html_content_str += """
        </div>
        <a href="THE_LINK" style="background-color: #4CAF50; color: white; padding: 10px 20px; text-align: center; text-decoration: none; display: inline-block; font-size: 16px; margin: 4px 2px; cursor: pointer; border-radius: 12px;">LINK_DESCRIPTION</a>
    </body>
    </html>
    """

    html_content = HtmlContent(html_content_str)
    mail = Mail(from_email, to_emails, subject, html_content)
    mail.add_bcc(bcc_emails)
    response = sg.send(mail)
    print(response.status_code, response.body, response.headers)

def main():
    """
     Send an email to the person who created the CREAT_YOUR_OWN_JSON_URL/JSON_FILE
    """
    json_url = "CREAT_YOUR_OWN_JSON_URL.json"
    data = fetch_data(json_url)
    current_date = datetime.now() + timedelta(days=1)
    formatted_date = current_date.strftime("%a %b %d")  
    send_email(data[formatted_date], formatted_date)

        
main()
