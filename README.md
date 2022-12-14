# Crypto Project
Project for Web Scraping, MLOps and Cloud Computing with Crypto data.

## Step 1 - General Architecture of Web Scraping 

![Screenshot](diagrams/WebScraping.png)

Core points:
<ul>
    <li><strong>Web Scraping:</strong> the web scraping objetive is get util data for this analisys. This step is contained in the Application layer in the figure above. The origin data are from: https://www.investing.com/crypto/currencies, all rights reserved;</li>
    <li><strong>Storage:</strong> after the previous step, we need to save the scrapped data. For this, we can use the PostgreSQL. This step is contained in the Storage layer;</li>
    <li><strong>Storage:</strong>we knows that data changes over time (mainly cryptocurrencies). In this way, we need to get the data in a recurring and consistent way throughout the day, that is, every two minutes, 
    as shown in Trigger layer.</li>
    
</ul>

After this process, we have a database that is being populated with about +- 100rows/5minutes.

## Step 2 - General Architecture of Web Scraping + ML Process
![Screenshot](diagrams/WS%2BML_Arch.png)

### Step 2.1 - Database Structure
![Screenshot](diagrams/Database.png)

### Step 2.2 - GCP Schedules
![Screenshot](diagrams/Schedules.png)