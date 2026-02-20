# 🚀 Performance Test -- Locust Setup Guide

This guide explains how to run the load test for the payment transfer
feature using Locust.



------------------------------------------------------------------------

## ⚙️ Setup & Run Instructions

### 2️⃣ Install Locust

``` bash
pip install locust
```

------------------------------------------------------------------------

### 3️⃣ Start Locust

Replace with your actual host:

``` bash
locust -f locustfile.py --host=https://yourapp.com
```

------------------------------------------------------------------------

### 4️⃣ Open the Locust Web UI

Open your browser and go to:

http://localhost:8089

------------------------------------------------------------------------

### 5️⃣ Configure the Test

Set:

-   Number of Users: 10,000\
-   Spawn Rate: 500--1000 users per second

Then click **Start Swarming**.

------------------------------------------------------------------------

## 📊 Success Criteria

During the test, monitor:

-   Response time \< 2 seconds\
-   Stable throughput under load

------------------------------------------------------------------------

## 📈 What you can Monitor on Server Side

-   CPU usage\
-   Memory usage\
-   Database performance\
-   API response times

------------------------------------------------------------------------

## 🛑 Stop the Test

Click **Stop** in the web UI when validation is complete.
