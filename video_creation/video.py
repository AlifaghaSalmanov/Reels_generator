from moviepy.editor import VideoFileClip, ImageClip, CompositeVideoClip
from db.database import DatabaseManager
from datetime import datetime
import os
class VideoEditor:
    # Static attribute for the background clip, shared across all instances
    background_clip = VideoFileClip("video_tools/background.mp4")

    def __init__(self):
        self.db = DatabaseManager("mellstory.db")
        self.image_clip = None
        self.image_folder = "images/"
        self.final_clip = None
        
        

    def fetch_media_path(self, video_number):
        """Fetch the image path for the given video number from the database."""
        image_paths = self.db.fetchall("SELECT id, name FROM images WHERE is_used = 0 ORDER BY RANDOM() LIMIT ?",(video_number,))  # Assuming this method exists and returns video info
        return image_paths

    def prepare_image_clip(self, image_path):
        """Prepare the image clip."""
        new_width = VideoEditor.background_clip.size[0] * 0.8
        bg_height = VideoEditor.background_clip.size[1]
        self.image_clip = (ImageClip(self. image_folder+image_path)
                           .set_duration(VideoEditor.background_clip.duration)
                           .resize(width=new_width, height=bg_height*0.4)
                           .set_position(('center', bg_height*0.1)))

    def create_final_clip(self):
        """Overlay the image on the video."""
        self.final_clip = CompositeVideoClip([VideoEditor.background_clip, self.image_clip])

    def export_video(self, output_path):
        """Export the final video."""
        self.final_clip.write_videofile(output_path, codec="libx264", fps=VideoEditor.background_clip.fps)

    def mark_image_as_used(self, image_id):
        """Mark the image as used in the database."""
        self.db.set_image_as_used(image_id)  # Assuming this method exists in your DatabaseManager class

    def generate_video(self, video_number):
        """Generate the video from database entries."""
        images_data = self.fetch_media_path(video_number)
        for image_data in images_data:
            # if file doesn't exist skip
            if not os.path.exists(self.image_folder + image_data[1]):
                print(f"File {self.image_folder + image_data[1]} does not exist. Skipping...")
                self.mark_image_as_used(image_data[0])
                continue
            self.prepare_image_clip(image_data[1])
            self.create_final_clip()
            
            file_name = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
            
            # if video path doesn't exist, create it
            if not os.path.exists("videos"):
                os.makedirs("videos")
            
            self.export_video(f"videos/output_{file_name}.mp4")
            
            self.mark_image_as_used(image_data[0])  # Mark the image as used after creating the clip
            
