import os
from pytubefix import YouTube
import subprocess
from plyer import notification


def notify(title):
    """
    Creates a notification informing that the download is complete.
    """
    notification.notify(
        title="Download Complete! ✅",
        message=f"{title}.mp4 downloaded successfully.",
        app_name="VideoDownloader",
    )


def clean_file_name(name):
    """
    Replaces spaces and special characters, present in a list, with "_" in the file name.
    """
    # List of special characters to be replaced
    special_characters = ['<', '>', ':', '"', '/', '\\', '|', '?', '*', ' ']
    
    # Iterate over each character in the list and replace with "_"
    for character in special_characters:
        name = name.replace(character, '_')
    
    return name


def download_video_and_audio(url):
    """
    Downloads video and audio separately in the best possible quality and combines both using ffmpeg.
    """
    try:
        # Create the YouTube object
        yt = YouTube(url)
        
        # Get the best video stream (based on highest resolution)
        video_stream = yt.streams.filter(adaptive=True, file_extension="mp4", only_video=True).order_by("resolution").desc().first()
        if not video_stream:
            print("No video stream is available for this video.")
            return
        
        # Get the best audio stream available
        audio_stream = yt.streams.filter(adaptive=True, only_audio=True, file_extension="mp4").order_by("abr").desc().first()
        if not audio_stream:
            print("No audio stream is available for this video.")
            return
        
        # Download the video
        print(f"Video: {yt.title}\n")
        print(f"Downloading video in the best resolution: {video_stream.resolution}...")
        video_path = video_stream.download(filename="video_temp.mp4")
        print("Video downloaded successfully.\n")
        
        # Download the audio
        print(f"Downloading audio in the best quality: {audio_stream.abr}...")
        audio_path = audio_stream.download(filename="audio_temp.mp4")
        print("Audio downloaded successfully.\n")
        
        # Combine video and audio using ffmpeg
        video_name = f"{yt.title}.mp4"
        output_path = clean_file_name(video_name)
        print("Combining video and audio...\n")
        subprocess.run([
            "ffmpeg",
            "-i", video_path,
            "-i", audio_path,
            "-c:v", "libx264",  # Encodes video in H.264
            "-c:a", "aac",      # Encodes audio in AAC
            "-strict", "experimental",
            output_path
        ], check=True)
        print(f"Video saved as: {output_path}\n")
        notify(yt.title)
        
        # Remove temporary files
        os.remove(video_path)
        os.remove(audio_path)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    url = str(input("Video link: "))
    download_video_and_audio(url)
