from instaloader import Instaloader, Profile
import os
from db.database import DatabaseManager
from pathlib import Path

class ProfileDownloader:
    def __init__(self, profile_names, image_count, download_directory, ig_username=None, ig_password=None):
        self.profile_names = profile_names
        self.image_count = image_count
        self.download_directory = download_directory
        self.ig = Instaloader(compress_json=False, download_video_thumbnails=False, save_metadata=False, download_comments=False, post_metadata_txt_pattern='')
        self.db = DatabaseManager("mellstory.db")
        self.ensure_directory_exists()
        if ig_username and ig_password:
            self.login(ig_username, ig_password)

    def login(self, username, password):
        try:
            self.ig.login(username, password)
        except Exception as e:
            print(f"Failed to log in: {e}")

    def ensure_directory_exists(self):
        if not os.path.exists(self.download_directory):
            os.makedirs(self.download_directory)

    def download_images(self):
        print(self.image_count)
        if self.db.fetchone("SELECT COUNT(*) FROM images WHERE is_used = 0")[0] >= self.image_count:
            return
        
        for profile_name in self.profile_names:
            try:
                download_count = 0
                profile = Profile.from_username(self.ig.context, profile_name)
                for post in profile.get_posts():
                    if post.is_video or self.db.fetchone("SELECT * FROM images WHERE profile = ? AND date = ?", (profile_name, post.date_utc)):
                        continue
                    self.ig.download_post(post, target=self.download_directory)
                    
                    self.rename_and_record(post, profile_name)
                    
                    download_count += 1
                    if download_count >= self.image_count:
                        break
            except Exception as e:
                print(e)
        
        self.delete_all_mp4_files()

    def rename_and_record(self, post, profile_name):
        for downloaded_file in Path(self.download_directory).glob("*.jpg"):
            new_name = ImageRenamer.rename(downloaded_file, profile_name, post.date_utc)
            self.db.query("INSERT INTO images (profile, name, date) VALUES (?, ?, ?)", (profile_name, new_name, post.date_utc))

    def delete_all_mp4_files(self):
        for file in Path(self.download_directory).glob("*.mp4"):
            os.remove(file)

class ImageRenamer:
    @staticmethod
    def rename(original_path, profile_name, post_date):
        new_name = f"{profile_name}_{post_date.strftime('%Y%m%d_%H%M%S')}.png"
        new_path = original_path.parent / new_name
        os.rename(original_path, new_path)
        return new_name