# Async Post Fetcher

This Python script asynchronously fetches data from an API endpoint (`https://jsonplaceholder.typicode.com/posts/{id}`), using `aiohttp` and `asyncio`. It requests posts for a range of IDs, gathers them concurrently, and saves the results in a `posts.json` file.

## Features
- Fetches data from a REST API asynchronously.
- Limits concurrent requests using a semaphore (`MAX_REQUESTS`).
- Saves the fetched posts to a `posts.json` file in a formatted JSON array.
- Measures and prints the total execution time.

## How It Works

1. **Concurrency Management**: 
   - The script makes use of `asyncio` to run tasks concurrently. 
   - The `semaphore` limits the number of simultaneous requests to `MAX_REQUESTS` (set to 10 in this example).
   
2. **Fetching Data**:
   - The `fetch_post_data` function sends a GET request to retrieve data for each post.
   - If the request succeeds (`status == 200`), the post data is returned as JSON. If it fails, an error message is printed.

3. **Data Handling**:
   - The `fetch_posts` function runs multiple requests concurrently and writes the fetched data to a file `posts.json`.
   - It writes the data in JSON format with proper indentation.

4. **Execution Time**:
   - The total execution time is displayed at the end of the script.

## Dependencies

To run this script, you need to have the following dependencies installed:

- **Python 3.7+**: Make sure you have Python version 3.7 or above installed.

- **aiohttp**: A library for making asynchronous HTTP requests.

- **asyncio**: Python's built-in library for writing asynchronous code. 
No separate installation is needed, as it is included with Python 3.7 and above.
  
- **time**: A built-in Python module for handling time-related functions.
This is part of the standard Python library, so no installation is required.
## Installation

1. Clone the repository:

```bash
git clone https://github.com/GigaDarchia/TBC-Task-4.git

cd TBC-Task-4
```
2. Install Dependencies:

```bash
pip install aiohttp
```
## Usage 

1. Run the script:
```bash
python task.py
```
The script will fetch data for posts with IDs ranging from 1 to 77 from the API and store the results in posts.json.
Once the fetching is complete, the total execution time will be printed.
