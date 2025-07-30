# ----------------------------------
# ==== A simple Text To Speech (TTS) convertor usable for generating audiobooks ====
# REQUIREMENTS: pip install kokoro torch torchaudio
# INPUT ENVIRONMENTAL VARIABLES:
#   a) PATH_TO_BOOK_TXT <=> PATH TO THE TXT FILE TO BE READ
#   b) PATH_TO_OUTPUT_WAV <=> PATH TO THE WAV THAT IS GENERATED
# ----------------------------------
import os

from kokoro import KPipeline
import soundfile as sf
import torch

PATH_TO_BOOK_TXT: str = os.getenv("PATH_TO_BOOK_TXT")
PATH_TO_OUTPUT_WAV: str = os.getenv("PATH_TO_OUTPUT_WAV", "output.wav")

# Read the input text
with open(PATH_TO_BOOK_TXT, "r", encoding="utf‑8") as fp:
    content = fp.read()
    content = content.replace('’', r"'")
    content = content.replace('‘', r"'")
    content = content.replace('–', r" - ")
    content = content.replace('/', r"; ")
    text = content.strip()

# Initialize pipeline for American English ('a'), or e.g. 'b' for British English
pipeline = KPipeline(lang_code='a', device="cuda" if torch.cuda.is_available() else "cpu")

# Split and synthesize text
generator = pipeline(text, voice='af_heart', speed=1.0, split_pattern=r'\n+')

# Collect audio chunks and sample rate (constant 24 kHz)
audio_chunks = []
for gs, ps, audio in generator:
    audio_chunks.append(audio)

# Concatenate chunks along time dimension
import numpy as np
combined = np.concatenate(audio_chunks, axis=0)

# Save as WAV
sf.write(PATH_TO_OUTPUT_WAV, combined, 24000)
print(f"Saved synthesized speech to {PATH_TO_OUTPUT_WAV}")
