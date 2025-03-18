class AudioTranscriber:
    def __init__(self, model_size="large-v3", device="cuda"):
        global MODEL
        try:
            self.model = MODEL
        except Exception as e:
            print(
                f"Error loading model: {e} Dont panic, I got this. You should really use nvidia for good results."
            )
        self.model = stable_whisper.load_model("medium", device="cpu")
        self.audio_paths = []
        self.index = len(self.audio_paths) - 1
        self.clean_audio_paths = []
        self.srt_paths = []
        self.srt_paths_small = []
        self.clean_json = ""
        self.clean_json_paths = []
        self.srt_small = ""
        self.text_paths = []
        self.text_parts = 0

    def add_time(self, time_str, minutes=1):
        """Add minutes to SRT timestamp, adjusting for fractional seconds."""
        base_time = datetime.strptime(time_str.split(",")[0], "%H:%M:%S")
        milliseconds = int(time_str.split(",")[1]) if "," in time_str else 0
        added_time = base_time + timedelta(minutes=minutes, milliseconds=milliseconds)
        return added_time.strftime("%H:%M:%S,") + f"{milliseconds:03d}"

    def srt_combine(self, paths):
        combined_content = ""
        subtitle_number = 1
        additional_minutes = 0

        for index, file_path in enumerate(paths):
            if index > 0:
                combined_content += ("\n\n")
            with open(file_path, "r", encoding="utf-8") as file:
                lines = file.readlines()
                i = 0
                while i < len(lines):
                    line = lines[i].strip()
                    if line.isdigit():
                        combined_content += f"{subtitle_number}\n"
                        subtitle_number += 1
                    elif "-->" in line:
                        start_time, end_time = line.split(" --> ")
                        combined_content += f"{self.add_time(start_time, additional_minutes)} --> {self.add_time(end_time, additional_minutes)}\n"
                    else:
                        combined_content += line + "\n"
                    i += 1
                additional_minutes += 1

        name = Path(paths[0]).stem
        output_file_prt = Path(paths[0]).parent.parent / f"{name}.srt"
        with open(str(output_file_prt), "w", encoding="utf-8") as file:
            file.write(combined_content)

    def transcribe_audio(self, audio_path, language="en", beam_size=5):
        """Transcribe the given audio file and return the transcription result."""
        self.audio_paths.append(audio_path)
        self.json_paths = []
        return self.model.transcribe(
            audio_path,
            verbose=True,
            word_timestamps=True,
            language=language,
        )

    def save_transcription(self, audio_path, result, small=False):
        """Save the transcription to .srt and .json files based on the audio file path."""
        if small:
            audio_path = audio_path.replace(".wav", "_small.wav")
        if "wav" in audio_path:
            srt_path = audio_path.replace(".wav", ".srt")
            txt_path = audio_path.replace(".wav", ".txt")
            json_path = audio_path.replace(".wav", ".json")
        else:
            srt_path = audio_path.replace(".mp3", ".srt")
            json_path = audio_path.replace(".mp3", ".json")
        print("outputting transcript files")

        if not small:
            result.to_txt(txt_path)
            self.text_paths.append(txt_path)
            self.srt_paths.append(srt_path)
            self.text_parts += 1
        else:
            self.srt_small = srt_path

        result.to_txt(f"{srt_path}".replace(".srt", ".txt"))
        result.save_as_json(json_path)
        self.json_path = json_path
        print("completed transcript files")

        if small:
            self.srt_paths_small.append(srt_path)
        else:
            self.srt_paths.append(srt_path)

    def censor_cursing(self, audio_path):
        return process_audio(audio_path, self.json_path)

    def transcribe_and_censor(self, audio_paths):
        """Process a list of audio files, transcribe and censor them, and save the results."""
        results = {}  # Store results in a dict to maintain order
        for audio_path in audio_paths:
            result = self.transcribe_audio(audio_path)  # Transcribe audio
            result.split_by_length(max_chars=42)  # Split result if needed
            self.save_transcription(audio_path, result)  # Save transcription
            aud, self.clean_json = self.censor_cursing(audio_path)  # Censor audio
            results[audio_path] = (aud, self.clean_json)  # Store results

        # Extract clean audio paths and json paths in order
        for audio_path in audio_paths:
            aud, clean_json = results[audio_path]
            self.clean_audio_paths.append(aud)  # Append clean audio
            self.clean_json_paths.append(clean_json)  # Append clean json

def main(audio_path, video_):
    global transcript_paths
    transcript_paths = []
    print("loading model")
    transcriber = AudioTranscriber(model_size=MODEL_SIZE, device="cuda")
    print("finished")
    log_ = JSONLog(audio_path)
    enums = split_audio(audio_path, "output")
    temp_folder = None
    if enums:
        for counter, audio_path in enumerate(enums):
            if not temp_folder and audio_path:
                temp_folder = Path(audio_path).parent.__str__()
            print("wav_file_path type:", type(audio_path))
            print("wav_file_path content:", audio_path)
            print(
                f"\n\nProcessing {audio_path}...@@@@@@@@@@@@@@@@@@@\n\nindex {counter+1} of {len(enums)}\n\n@@@@@@@@@@@@@@@@@@@\n\n"
            )
            transcriber.transcribe_and_censor(enums)  # Pass the list of audio paths
