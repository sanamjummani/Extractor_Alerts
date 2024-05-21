### Project Description: Extractor Alerts

#### Overview
The "Extractor Alerts" project is a Python-based application designed to monitor Bitcoin prices from the CoinDesk website and send email alerts when the price meets a specified target. This project integrates web scraping, data processing, and automated email notifications to keep users informed about significant changes in Bitcoin prices.

#### Project Goals
1. **Real-time Bitcoin Price Monitoring:** Scrape Bitcoin price data from the CoinDesk website at regular intervals.
2. **Price Target Alerts:** Compare the scraped price data against user-defined target prices.
3. **Email Notifications:** Send automated email alerts to users when the Bitcoin price reaches or surpasses the specified target.

#### Key Components

1. **Data Scraping:**
   - Utilize Python libraries such as `requests` and `BeautifulSoup` to extract Bitcoin price data from the CoinDesk website.
   - Implement a scheduled task to perform web scraping at regular intervals, ensuring up-to-date price monitoring.

2. **Price Target Comparison:**
   - Store user-defined target prices in a configuration file or database.
   - Compare the scraped Bitcoin price with the target prices to determine if an alert needs to be triggered.

3. **Email Notifications:**
   - Use the `smtplib` library to send email notifications to users.
   - Ensure secure email sending by integrating with email service providers using SMTP authentication.

#### Technical Implementation

1. **Web Scraping:**
   - **Libraries:** `requests`, `BeautifulSoup`,`jmespath`
   - **Functionality:** Fetch the latest Bitcoin price from the CoinDesk website. Parse the HTML content to extract the current price.

2. **Price Target Alert:**
   - **Functionality:** Check if the current Bitcoin price meets or exceeds any user-defined target prices.

3. **Email Notifications:**
   - **Functionality:** Send an email alert to the user if the target price is met.


#### Workflow
1. **Scraping Schedule:**
   - The scraper runs at pre-defined intervals (in our case every hour) to fetch the latest Bitcoin price from CoinDesk.

2. **Price Check:**
   - After fetching the price, the system checks it against the target prices.

3. **Alert Trigger:**
   - If the current price meets or exceeds a target, the system triggers an email alert to the user.

#### Conclusion
The "Extractor Alerts" project provides an automated solution to monitor Bitcoin prices and notify users of significant changes. By leveraging Python's powerful libraries, the project ensures timely and accurate alerts, helping users stay informed about market movements.
