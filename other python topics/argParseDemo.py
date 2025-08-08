import argparse
import requests
parser=argparse.ArgumentParser()

parser.add_argument("url",help="URL of the file to download")
parser.add_argument("output",help="by which to save the file")


args=parser.parse_args()

print("URL:",args.url)
print("Output file:",args.output)


try:
    with requests.get(args.url, stream=True) as response:
        response.raise_for_status()  # Raise an error on bad status
        with open(args.output, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
    print("Download completed successfully.")
except Exception as e:
    print("Error during download:", e)