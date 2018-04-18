# Udacity Logs Analysis Project

This is the Udacity logs analysis project.

## Files
1. analysis.py
    - Main program that performs logs analysis
2. Program Output.txt
    - Copy of expected program output

## SQL Views

Below are the various views:

**Rows for <i>top_articles</i> view**

1. title: Title of article
2. author: ID of author who wrote article
3. num: Number of times article accessed

**Rows for <i>request_errors</i> view**

1. dt: Date in the format YYYY-MM-DD for request
2. error_count: Number of requests with errors relating to dt column

**Rows for <i>request_total</i> view**

1. dt: Date in the format YYYY-MM-DD for request
2. total_count: Total requests for day relating to dt column

## Running the Program

Running in IDLE:
1. Open up the analysis.py file in Python IDLE.
2. Run the code in IDLE

Running in Command Line:
1. Open up the command line
2. Type in `python3 analysis.py` and execute
