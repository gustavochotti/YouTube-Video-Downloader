# YouTube Video Downloader

## Overview
This project allows users to download YouTube videos and audio in the best possible quality and merge them into a single `.mp4` file using FFmpeg. The script utilizes the `pytubefix` library to fetch video and audio streams and `plyer` to display notifications.

## Features
- Downloads the highest resolution video and best quality audio separately.
- Combines video and audio into a single `.mp4` file using FFmpeg.
- Notifies the user when the download is complete.

## Requirements

### Python Libraries
Install the required libraries using `pip`:
```bash
pip install pytubefix plyer
```

### FFmpeg Installation
FFmpeg is required to merge video and audio streams. Follow the instructions below based on your operating system.

#### Windows:
1. Install FFmpeg manually by following the official documentation: [FFmpeg Documentation](https://ffmpeg.org)

   **Simpler Alternative**: Use `Scoop` to install FFmpeg:
   - Open PowerShell and execute:
     ```powershell
     Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
     irm get.scoop.sh | iex
     ```
   - Install FFmpeg with Scoop:
     ```powershell
     scoop install ffmpeg
     ```

#### Linux:
Open the terminal and execute the appropriate commands for your distribution:

1. **Debian/Ubuntu**:
   ```bash
   sudo apt update
   sudo apt install ffmpeg
   ```
2. **Fedora/CentOS**:
   ```bash
   sudo dnf install ffmpeg
   ```
3. **Arch Linux**:
   ```bash
   sudo pacman -S ffmpeg
   ```
4. **openSUSE**:
   ```bash
   sudo zypper install ffmpeg
   ```
5. **Other distributions**:
   Check your distribution's documentation or download and compile FFmpeg manually following the [official instructions](https://ffmpeg.org).

#### MacOS:
1. Install Homebrew (if not already installed):
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
2. Install FFmpeg using Homebrew:
   ```bash
   brew install ffmpeg
   ```
3. Verify the installation:
   ```bash
   ffmpeg -version
   ```

## Usage
1. Run the script by executing:
   ```bash
   python downloader.py
   ```
2. Enter the URL of the YouTube video when prompted.
3. The script will:
   - Download the video and audio streams.
   - Merge them into a single `.mp4` file.
   - Notify you when the process is complete.

## Notifications
The script uses the `plyer` library to display desktop notifications indicating the completion of the download.

## Code Structure
- **`notify`**: Displays a notification when the download is complete.
- **`clean_file_name`**: Sanitizes file names by replacing spaces and special characters.
- **`download_video_and_audio`**: Downloads the video and audio streams and combines them using FFmpeg.

## Notes
- Ensure you have a stable internet connection to download video and audio streams.
- Make sure FFmpeg is correctly installed and added to your system's PATH environment variable.

## License
This project is licensed under the MIT License.


