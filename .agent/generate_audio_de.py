#!/usr/bin/env python3
"""
generate_audio_de.py
--------------------
MP3 pronunciation generator for FlashcardsLearnGermanKids.
Language: DE (German) — for back-side word/sentence audio.

Usage:
    python3 generate_audio_de.py "Ameise"
    python3 generate_audio_de.py "die Ameise"
    python3 generate_audio_de.py "Ameise" "Hund" "Katze"

Output: audio/de/word_YYYYMMDDHHMMSS.mp3

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
LANGUAGE = "de"           # German
_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(_SCRIPT_DIR, "..", "audio", "de")  # always resolves to audio/de/
# ─────────────────────────────────────────────────────────────


def sanitize_filename(text: str) -> str:
    """Convert text to a safe filename (lowercase, no spaces)."""
    return (
        text.lower()
        .replace(" ", "_")
        .replace("/", "_")
        .replace("ä", "ae")
        .replace("ö", "oe")
        .replace("ü", "ue")
        .replace("ß", "ss")
    )


def generate_mp3(text: str, output_dir: str = OUTPUT_DIR) -> str:
    """
    Generate an MP3 file for the given text in German.

    Args:
        text: Text / word to read aloud (e.g. "die Ameise")
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


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 generate_audio_de.py <word1> [word2] ...")
        print('Example:  python3 generate_audio_de.py "Ameise" "der Hund"')
        sys.exit(1)

    words = list(sys.argv[1:])
    print(f"🎙️  Generating audio for {len(words)} word(s) (language: {LANGUAGE})")
    print(f"📁  Output: {OUTPUT_DIR}/\n")

    for word in words:
        generate_mp3(word)

    print("\nDone! 🚀")
