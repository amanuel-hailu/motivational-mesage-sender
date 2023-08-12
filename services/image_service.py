import urllib.request
import random
import os


def fetch_image():
    # For logging say that we're fetching a image
    print("Fetching image...")
    sentiments = [
        "happy",
        "vibe",
        "sky",
        "city",
        "pet",
        "nature",
        "enjoy",
        "love",
        "life",
        "travel",
        "fun",
    ]
    keyword = random.choice(sentiments)
    url = f"https://source.unsplash.com/random/?{keyword}"
    print(f"Fetching image from URL: {url}")

    # path = os.path.join("../images", "downloaded_image.jpg")
    # Save it in the by first navigating to the parent directory and then the images folder
    path = os.path.join("images", "downloaded_image.jpg")

    try:
        urllib.request.urlretrieve(url, path)
        print(f"Image saved as 'downloaded_image.jpg' for keywords: {keyword}")
        return {'success': True, 'url': url, 'path': path}
    except urllib.error.URLError as e:
        print(f"An error occurred while fetching the image: {e.reason}")
        return {'success': False, 'url': url, 'error': str(e.reason)}
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
        return {'success': False, 'url': url, 'error': str(e)}


if __name__ == "__main__":
    result = fetch_image()
    print(result)  # Outputs the result dictionary
