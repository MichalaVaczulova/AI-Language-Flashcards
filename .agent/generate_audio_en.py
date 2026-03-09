#!/usr/bin/env python3
"""
generate_audio_en.py
--------------------
MP3 pronunciation generator for FlashcardsLearnGermanKids.
Language: EN (English) — for front-side prompt sentences.

Usage:
    python3 generate_audio_en.py "T-Rex has a very sharp tooth."
    python3 generate_audio_en.py "Sentence one." "Sentence two."

Output: audio/sentence_text_YYYYMMDDHHMMSS.mp3

Install dependencies:
    pip3 install gtts
"""

import sys
import os
from datetime import datetime

try:
    from gtts import gTTS  # type: ignore[import-untyped]
except ImportError:
    print("❌ Missing library gTTS. Run: pip3 install gtts")
    sys.exit(1)

# ── Configuration ────────────────────────────────────────────
LANGUAGE = "en"           # English
_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(_SCRIPT_DIR, "..", "audio", "en")  # always resolves to audio/en/
# ─────────────────────────────────────────────────────────────


def sanitize_filename(text: str) -> str:
    """Convert text to a safe filename (lowercase, no spaces)."""
    return (
        text.lower()
        .replace(" ", "_")
        .replace("/", "_")
        .replace(".", "")
        .replace(",", "")
        .replace("'", "")
        .replace("!", "")
        .replace("?", "")
    )


def generate_mp3(text: str, output_dir: str = OUTPUT_DIR) -> str:
    """
    Generate an MP3 file for the given text in English.

    Args:
        text: Text / sentence to read aloud
        output_dir: Target folder

    Returns:
        Generated filename (basename only, no path)
    """
    os.makedirs(output_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    safe_name = sanitize_filename(text)
    filename = f"{safe_name}_{timestamp}.mp3"
    filepath = os.path.join(output_dir, filename)

    tts = gTTS(text=text, lang=LANGUAGE, slow=False)
    tts.save(filepath)

    print(f"✅ Generated: {filename}")
    return filename


import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MP3 pronunciation generator for EN")
    parser.add_argument("--deck", type=str, default="", help="Subfolder name for the deck (e.g. germanVocabulary_01_dino)")
    parser.add_argument("sentences", nargs="+", help="Sentences to read aloud")
    
    args = parser.parse_args()
    
    sentences = args.sentences
    deck_folder = args.deck

    out_dir = os.path.join(OUTPUT_DIR, deck_folder) if deck_folder else OUTPUT_DIR

    print(f"🎙️  Generating audio for {len(sentences)} sentence(s) (language: {LANGUAGE})")
    print(f"📁  Output: {out_dir}\n")

    for sentence in sentences:
        generate_mp3(sentence, out_dir)

    print("\nDone! 🚀")
