## Mute Curse Words in Your Videos - A Simple Guide

This tool helps you automatically mute curse words in your video or audio files. It's designed to be easy to use, even if you're not a tech expert.

### What You'll Need

Before you start, you'll need to install a couple of things:

1.  **Python:** Think of Python as the engine that runs this tool.  You need version 3.10.  You can download it here:
    *   [Python 3.10 Download](https://www.python.org/ftp/python/3.10.11/python-3.10.11-amd64.exe)

    **Important:** When you install Python, make sure you check the box that says "Add to PATH" or something similar. This allows your computer to easily find and use Python.  Here's what it looks like:

    ![Add Python to PATH](https://miro.medium.com/v2/resize:fit:1344/0*7nOyowsPsGI19pZT.png)

2.  **FFmpeg:** This is a tool that helps the program work with video and audio files.  You can download it from one of these links:
    *   [FFmpeg (Option 1)](https://github.com/icedterminal/ffmpeg-installer/releases/download/6.1.1.20240201/FFmpeg_Full.msi)
    *   [FFmpeg (Option 2)](https://github.com/Vouk/ffmpeg/releases/download/autobuild-2025-03-10-19-20/FFmpeg.GPL.Installer.msi)

### Setting Up the Program

Here's how to get everything up and running:

1.  **Download the Program:** Download the program files as a zip file from this link:
    *   [Download Mute-Cursing-In-MP4-MP3-for-Youtube](https://github.com/samfisherirl/Mute-Cursing-In-MP4-MP3-for-Youtube/archive/refs/heads/main.zip)

2.  **Install Dependencies:**
    * You can install the dependencies using the `one-click-installer.bat` or `venv + pip install -r requirements.txt`.

3.  **Extract the Files:**  Find a place on your computer where you want to keep the program (like your Documents folder). Extract the zip file you downloaded into that location.

4.  **Run the Installer:**  Inside the extracted folder, you'll find a file called `one-click-installer.bat`.  Double-click this file to run it.  This will install some additional components the program needs.

5.  **Create Your Curse Word List:** The program needs to know which words to mute.
    *   Create a new, blank text file using Notepad (Windows) or TextEdit (Mac).
    *   Rename the file to `curse_words.csv`
    *   In this file, write each curse word you want to mute on a separate line.  For example:
        ```
        damn
        hell
        shit
        ```
    *   Save the file in the same folder where you extracted the program files.

### How to Use the Program

1.  **Run the Program:** Double-click the main program file (likely a `.py` file).

2.  **Initial Setup (Important):** The *very first* time you run the program, it will ask about a transcript.  **Answer "no"** by typing "n" and pressing Enter.
    * It will then ask you to select the file you want to work with (MP4 or WAV).

3.  **Select Your Video/Audio File:**  Choose the video or audio file you want to mute.

4.  **Output:**  The program will create a new version of your file with the curse words muted, saving it in the same folder as the original.

# Example 

![image](https://github.com/user-attachments/assets/3658e6f8-2b59-4373-97ea-bcbf44cf02d9)


https://github.com/user-attachments/assets/3eeb2839-48f0-4137-a6fa-a2a285e2585f



## Concept 

1) convert mp4/mp3 to wav
2) read wav transcript with openai wisper via stable-ts
3) read csv of curse words
4) if curse word found matching a word in a sentence, mute that word
5) convert back to mp3

## To add

1) Convert from mp4
   

### Concerns:

- clipping // not fading in/out of clips
- setting words to censor
- conversion time/optimization
