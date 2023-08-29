# CarPriceProject

Serverless Car Market Insights is an advanced platform designed to provide users with real-time data and insights about car offers. Leveraging the power of AWS Lambda and Python web scraping, it ensures efficient data extraction, processing, and storage while offering features like Price History Tracking, Safety Ratings Integration, and Fuel Efficiency Information.

## Key Features

### Serverless Web Scraping

**Overview**: The project utilizes AWS Lambda functions to scrape car offers from multiple websites daily. This serverless architecture ensures cost-efficient and scalable data extraction.

**Functionality**:
- **AWS Lambda Scrapers**: Individual AWS Lambda functions are dedicated to scraping data from specific car listing websites.
- **Scheduled Execution**: AWS CloudWatch Events schedule the Lambda functions to run daily, ensuring up-to-date car offer data.
- **Scalability**: The serverless architecture automatically scales based on the workload, accommodating high-traffic days.

### Price History Tracking

**Overview**: Users can track the historical prices of car offers, enabling them to make informed decisions based on pricing trends.

**Functionality**:
- **Historical Price Data**: Price history data is stored efficiently in AWS DynamoDB, allowing users to access and analyze historical price trends.
- **Lambda for Price Change Alerts**: Another Lambda function checks for price changes and sends notifications to users who've set up alerts.

### Integration with External APIs

**Overview**: External APIs are integrated seamlessly to provide safety ratings and fuel efficiency information for each car offer.

**Functionality**:
- **Data Enrichment**: This data is enriched in DynamoDB alongside car listings, enabling users to access comprehensive car information such as safety ratings and fuel efficiency.


