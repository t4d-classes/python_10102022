# Exercise 9

How to run the client and server.

From the `rates_app` folder, run the server:

```bash
python ./rates_api.py
```

1. Implement the code in the steps below in a new file named `rates_demo.py` in the `rates_app` folder. 

2. Install the "requests" package from PyPi.org.

https://docs.python-requests.org/en/master/user/quickstart/#make-a-request

3. Using the "requests" package API, call the following URL for each date returned from the "business_days" function. Import the `business_days` function from the `business_days` module.

http://127.0.0.1:5000/api/2021-04-08?base=INR&symbols=USD,EUR

Specify a start date and an end date, and for each business day in within the start and end date range, get the currency rate information from the rates API.

4. Create a list of text values from each response. The text value is formatted as JSON. Do not parse the JSON. Just put each JSON response in the list.

5. Display each list items in the console.