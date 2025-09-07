import os
import requests
from urllib.parse import urlparse
from pathlib import Path
import hashlib

# Function to generate a SHA256 hash for a file.
# This helps detect duplicate images by comparing content, not just filenames.
def get_file_hash(file_path):
    hash_sha256 = hashlib.sha256()  # Create a SHA256 hashing object
    with open(file_path, "rb") as f:  # Open file in binary read mode
        for chunk in iter(lambda: f.read(4096), b""):  # Read in chunks of 4KB
            hash_sha256.update(chunk)  # Update the hash with each chunk
    return hash_sha256.hexdigest()  # Return the final hash string


# Main function to fetch multiple images
def fetch_images(urls):
    # Create directory to store images if it doesn't exist
    save_dir = Path("Fetched_Images")
    save_dir.mkdir(parents=True, exist_ok=True)

    # Keep track of already downloaded image hashes (avoid duplicates)
    downloaded_hashes = set()
    for file in save_dir.iterdir():  # Loop through existing files in folder
        if file.is_file():
            downloaded_hashes.add(get_file_hash(file))  # Add their hashes to set

    # Process each URL provided by the user
    for url in urls:
        print(f"\n🌍 Processing: {url}")  # Show which URL is being processed
        try:
            # Fetch the image with timeout and stream enabled
            response = requests.get(url, stream=True, timeout=10)
            response.raise_for_status()  # Raise error if HTTP response is bad

            # Extract important HTTP headers
            content_type = response.headers.get("Content-Type", "")
            content_length = response.headers.get("Content-Length", "Unknown")

            # Check if the content is an image (skip if not)
            if not content_type.startswith("image/"):
                print(f"⚠️ Skipped (Not an image): {url}")
                continue

            # Skip if file is larger than 5MB (safety precaution)
            if content_length != "Unknown" and int(content_length) > 5e6:
                print(f"⚠️ Skipped (File too large > 5MB): {url}")
                continue

            # Extract filename from URL path
            parsed_url = urlparse(url)
            filename = os.path.basename(parsed_url.path) or "downloaded_image.jpg"
            save_path = save_dir / filename

            # Prevent overwriting files by renaming duplicates (filename_1, filename_2, etc.)
            base, ext = os.path.splitext(filename)
            counter = 1
            while save_path.exists():
                save_path = save_dir / f"{base}_{counter}{ext}"
                counter += 1

            # Save the downloaded content in binary mode
            with open(save_path, "wb") as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)

            # Check for duplicate content by comparing file hash
            file_hash = get_file_hash(save_path)
            if file_hash in downloaded_hashes:
                print(f"⚠️ Duplicate detected, removing {save_path}")
                save_path.unlink()  # Delete duplicate file
            else:
                downloaded_hashes.add(file_hash)  # Store hash in memory
                print(f"✅ Saved: {save_path} | Size: {content_length} bytes")

        except requests.exceptions.RequestException as e:
            # Handle all network-related errors gracefully
            print(f"❌ Error fetching {url}: {e}")


if __name__ == "__main__":
    # Prompt user to enter multiple image URLs (comma separated)
    raw_input = input("Enter image URLs (comma separated): ").strip()
    # Split input into list of URLs, trimming whitespace
    urls = [u.strip() for u in raw_input.split(",") if u.strip()]
    # Call main function to fetch all images
    fetch_images(urls)
