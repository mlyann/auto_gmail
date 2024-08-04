# Project Name

This is an automated email sending system developed in Python. It fetches data from a specified JSON data source and sends emails to recipients listed.

## Features

- Fetches information from a JSON data source.
- Sends personalized emails with dynamic content based on fetched data.
- Supports basic authentication for data fetching.
- Emails include customized HTML content featuring a card-style layout for recipients.
- Allows for both direct recipients and BCC options to maintain privacy.

## Installation

To set up this project, you need to install Python and the required packages.

```bash
pip install requests python-dotenv sendgrid
```

## Configuration

1. Create a `.env` file in the root directory and add your SendGrid API key:
   ```
   API_KEY='YOUR_SENDGRID_API_KEY_HERE
   ```
2. Modify the script to include your email addresses and the specific JSON URL you will be fetching data from.


## Usage
To run the script, simply execute the main Python file:
```
python your_script_name.py
```
Ensure you have proper internet connectivity and your API keys are correctly set up.


## Contribution
Contributions to this project are welcome. Please fork the repository and submit a pull request with your enhancements.

## Contact
For support or to report issues, please send an email to mlyang721@arizona.edu
