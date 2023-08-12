import requests
import time


def get_random_quote():
    # For logging say that we're fetching a quote
    print("Fetching quote...")
    url = "https://api.forismatic.com/api/1.0/"
    params = {
        "method": "getQuote",
        "format": "json",
        "lang": "en",
    }
    max_retries = 5
    retries = 0
    while retries < max_retries:
        try:
            response = requests.get(url, params=params)
            # Will raise an HTTPError if the HTTP request returned an unsuccessful status code
            response.raise_for_status()

            # Attempt to parse the response as JSON
            quote_data = response.json()
            return quote_data['quoteText'], quote_data.get('quoteAuthor', 'Unknown author')
        except (requests.RequestException, ValueError):
            retries += 1
            print(
                f"Error fetching quote, retrying... ({retries}/{max_retries})")
            time.sleep(1)  # Optional: add a delay between retries
        except Exception as e:
            # Handle any other unexpected exceptions
            raise Exception(f"An unexpected error occurred: {e}")
    raise Exception(f"Failed to fetch quote after {max_retries} attempts.")
