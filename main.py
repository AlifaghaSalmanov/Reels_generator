# main.py
import argparse
from image import ProfileDownloader
from video_creation.video import VideoEditor
# Create the parser
parser = argparse.ArgumentParser(description="A simple Python CLI tool for basic arithmetic operations.")



parser.add_argument("-v", "--video_count", type=int, default=3, help="Number of videos to create from the downloaded images")

parser.add_argument("-u", "--username", type=str, help="Instagram username")
parser.add_argument("-p", "--password", type=str, help="Instagram password")

# Execute the parse_args() method
args = parser.parse_args()


# Initialize and run the ProfileDownloader
profile_names_list = [
    "memenade_",
    "memes",
    "reddit_top_memes",
    "peddytommy",
    "onlyteens.us",
    "memespointt",
    "memesfunnyzone",
    "relatefy",
    "geniusintrovert",
    "antisocialmeme",
]
downloader = ProfileDownloader(profile_names_list, image_count=args.video_count, download_directory="images", ig_username=args.username, ig_password=args.password)
downloader.download_images()

# Example usage
video_editor = VideoEditor()
video_editor.generate_video(args.video_count)  # Assuming 1 is the video number you want to generate
