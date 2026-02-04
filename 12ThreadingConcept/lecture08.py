# Multithreaded file downloader
# Demonstrates I/O-bound concurrency using threads

import threading
import requests
import time

# Function that downloads content from a URL
def download(url):
    # Print when download starts
    print(f"Starting download from {url}")
    
    # Network I/O operation (releases GIL)
    resp = requests.get(url)
    
    # Print when download finishes with size
    print(
        f"Finished downloading from {url}, "
        f"size: {len(resp.content)} bytes"
    )

# List of URLs to download
urls = [
    "https://httpbin.org/image/png",
    "https://httpbin.org/image/jpeg",
    "https://httpbin.org/image/svg",
]

# Record start time
start = time.time()

threads = []

# Create and start a thread for each URL
for url in urls:
    # Create thread that runs download(url)
    t = threading.Thread(target=download, args=(url,))
    
    # Start thread execution
    t.start()
    
    # Store thread reference for later synchronization
    threads.append(t)

# Wait for all threads to finish
for t in threads:
    t.join()

# Record end time
end = time.time()

# Total time taken
print(f"All downloads done in {end - start:.2f} seconds")
