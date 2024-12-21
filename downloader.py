import os
import logging
from pytubefix import YouTube
import subprocess
from plyer import notification

# Configure logging
logging.basicConfig(
    level=logging.INFO,  # Set the default logging level
    format="%(asctime)s - %(levelname)s - %(message)s",  # Message format
    handlers=[
        logging.StreamHandler(),  # Output to console
        # logging.FileHandler("youtube_downloader.log")  # Log to a file
    ]
)

def notify(title):
    """
    Creates a notification informing that the download is complete.
    """
    notification.notify(
        title="Download Complete! ✅",
        message=f"{title}.mp4 downloaded successfully.",
        app_name="YouTube Downloader",
    )

def clean_file_name(name):
    """
    Replaces spaces and special characters, present in a list, with "_" in the file name.
    """
    special_characters = ['<', '>', ':', '"', '/', '\\', '|', '?', '*', ' ']
    for character in special_characters:
        name = name.replace(character, '_')
    return name

def download_video_and_audio(url):
    """
    Downloads video and audio separately in the best possible quality and combines both using ffmpeg.
    """
    try:
        yt = YouTube(url)
        
        logging.info(f"Processing video: {yt.title}")
        
        video_stream = yt.streams.filter(adaptive=True, file_extension="mp4", only_video=True).order_by("resolution").desc().first()
        if not video_stream:
            logging.error("No video stream is available for this video.")
            return
        
        audio_stream = yt.streams.filter(adaptive=True, only_audio=True, file_extension="mp4").order_by("abr").desc().first()
        if not audio_stream:
            logging.error("No audio stream is available for this video.")
            return
        
        logging.info(f"Downloading video in resolution: {video_stream.resolution}")
        video_path = video_stream.download(filename="video_temp.mp4")
        logging.info("Video downloaded successfully.")
        
        logging.info(f"Downloading audio in quality: {audio_stream.abr}")
        audio_path = audio_stream.download(filename="audio_temp.mp4")
        logging.info("Audio downloaded successfully.")
        
        video_name = f"{yt.title}.mp4"
        output_path = clean_file_name(video_name)
        
        logging.info("Combining video and audio...")
        subprocess.run([
            "ffmpeg",
            "-i", video_path,
            "-i", audio_path,
            "-c:v", "libx264",  # Encode video using H.264
            "-c:a", "aac",      # Encode audio using AAC
            "-strict", "experimental",
            output_path
        ], check=True)
        logging.info(f"Video saved as: {output_path}")
        
        notify(yt.title)
        
        os.remove(video_path)
        os.remove(audio_path)
        logging.info("Temporary files removed.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    url = str(input("Video link: "))
    download_video_and_audio(url)
