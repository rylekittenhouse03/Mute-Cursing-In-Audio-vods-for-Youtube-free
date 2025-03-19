import stable_whisper
import os
from pathlib import Path

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
MODEL_SIZE = "medium.en"
SPLIT_IN_MS = 15
print("loading model")
MODEL = stable_whisper.load_model(MODEL_SIZE, device="cuda")

segment_duration = 3000
buff_ratio = 1.25
CURSE_WORD_FILE = "curse_words.csv"

sample_audio_path = "looperman.wav"
transcripts = ""
exports = ""
new_trans_path = Path.cwd()
new_trans_path = Path(str(new_trans_path) + "\\transcripts")
