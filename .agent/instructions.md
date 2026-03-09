# 📋 INSTRUCTIONS FOR CREATING FLASHCARDS

## 🎯 Goal

Prepare digital flashcards for **FlashcardsLearnGermanKids** in **Obsidian** using the **AOSR (Another Obsidian Spaced Repetition)** plugin.

The cards work with sentences and context — not just isolated words.
**Pictures are always the foundation** — a visual anchor for memorization.

**Source language: English → German**

---

## 📁 Vault Structure

```
FlashcardsLearnGermanKids/
├── pictures/           ← card images (organized in subfolders per deck)
├── audio/              ← audio files (organized in subfolders: en/deck_name, de/deck_name)
├── flashcards/         ← .md files with cards
├── .agent/             ← AI tools directory
│   ├── generate_audio_en.py ← generate English audio
│   ├── generate_audio_de.py ← generate German audio
│   └── instructions.md      ← this file
```

---

## 🃏 TYPE 1: German Vocabulary (`#germanVocabulary`)

### Description

Flashcards for learning German words in the context of sentences. Each word is embedded in a simple, engaging sentence.

---

### Flashcard Creation Rules

#### ▶ Front of card (question)
- **Short, simple English sentence** — max 1 sentence, no subordinate clauses!
  - ✅ Good: *"Dino has a long <span style="color:#e53935">neck</span>."* or *"A little dino hatched from the <span style="color:#e53935">egg</span>."*
  - ❌ Bad (too complex): *"Brachiosaurus had a neck longer than an entire school bus!"*
- The sentence is **in English** — the key word is the English word, **NOT the German word**
- **Highlight the key English word in red** `#e53935`: `<span style="color:#e53935">neck</span>`
- **English audio** of the sentence — generated with `generate_audio_en.py`
  - `python3 .agent/generate_audio_en.py --deck NAME_OF_DECK "Dino has a long neck."`
  - Saved in `audio/en/NAME_OF_DECK/` folder
- **Picture** in Pixar / cartoon style — colourful, action-oriented, clear
  - Save in `pictures/NAME_OF_DECK/`
  - Filename: `word_YYYYMMDD.png` — e.g. `kopf_20260225.png`
  - Embed using Obsidian syntax **without path**: `![[kopf_20260225.png]]`

#### ▶ Back of card (answer)
- **Article** (gender): `der` / `die` / `das` — bold, highlighted
- **German translation of the key word** — split into syllables with **alternating colours** (blue 🔵 and red 🔴)
- **German sentence** — translation of the whole sentence from the front side (in italics)
  - Highlight the new German word in red `#e53935`: `<span style="color:#e53935">Kopf</span>`
- **Audio pronunciation of the whole German sentence** (MP3) — embedded via `![[word_timestamp.mp3]]`
  - Generate using the inline Python script:
    ```bash
    python3 -c "from gtts import gTTS; import os; from datetime import datetime; ts=datetime.now().strftime('%Y%m%d%H%M%S'); out='audio/de/NAME_OF_DECK'; os.makedirs(out, exist_ok=True); tts=gTTS('GERMAN_SENTENCE', lang='de'); tts.save(f'{out}/word_{ts}.mp3'); print(f'{out}/word_{ts}.mp3')"
    ```
  - Save to the folder `audio/de/NAME_OF_DECK/`

#### ▶ Colour Scheme Overview

| Where | What | Colour |
|-------|------|--------|
| EN sentence (front side) | Key **English** word | 🔴 Red `#e53935` |
| DE sentence (back side) | Key **German** word | 🔴 Red `#e53935` |
| DE heading — 1st, 3rd, 5th syllable | Syllables of German word | 🔵 Blue `#1a73e8` |
| DE heading — 2nd, 4th, 6th syllable | Syllables of German word | 🔴 Red `#e53935` |

---

### Card Template — Sentence (AOSR format)

> **Rules for separating cards:**
> - `#Q #germanVocabulary` is written **only once** — at the very beginning of the `.md` file
> - Cards are separated by `***` — **without empty lines** before or after
> - A new card starts **immediately on the line below `***`**

```markdown
#Q #germanVocabulary
## Dino has a long <span style="color:#e53935">neck</span>.
![[dino_has_a_long_neck_20260307102402.mp3]]
![[hals_20260225.png]]
?
**der**
# <span style="color:#1a73e8">HALS</span>
## *Der Dino hat einen langen <span style="color:#e53935">Hals</span>.*
![[hals_v2_20260226065619.mp3]]
***
## A little dino hatched from the <span style="color:#e53935">egg</span>.
![[a_little_dino_hatched_from_the_egg_20260307102402.mp3]]
![[ei_20260225.png]]
?
**das**
# <span style="color:#1a73e8">EI</span>
## *Aus dem <span style="color:#e53935">Ei</span> schlüpft ein kleiner Dino.*
![[ei_v2_20260226065620.mp3]]
```

---

## 🃏 TYPE 2: Question & Explanation (`#robkoLearn`)

### Description

Cards for broader content — history, nature, interesting facts. The front side is a question + image, the back side is an explanation, and optionally an additional diagram or map.

---

### Flashcard Creation Rules

#### ▶ Front of card (question)
- **Question** — simple, specific, interesting for an 8-year-old boy
  - Example: *"Why did the dinosaurs go extinct?"*
- **Image** — illustration of the topic (cartoon, realistic, diagram)

#### ▶ Back of card (answer)
- **Short explanation** — 2–4 sentences, clear and easy to understand
- *Optional:* additional image, diagram, map, or table

---

### Card Template — Question & Explanation (AOSR format)

```markdown
#Q #robkoLearn
Why did the dinosaurs go extinct?
![[dinosaur_20260224.png]]
?
Around 66 million years ago, a huge meteor hit the Earth. It raised a dust cloud that blocked the sun. The plants died and the dinosaurs had nothing to eat.
![[dinosaur_impact_diagram_20260224.png]]
***
How long does it take for light from the Sun to reach Earth?
![[sun_earth_20260224.png]]
?
Light travels at a speed of 300,000 km/s. The distance between the Earth and the Sun is about 150 million km. It takes approximately **8 minutes**.
![[light_speed_diagram_20260224.png]]
```

---

## 🖼️ Image Style

- **Front side:** Pixar / Disney / cartoon — action-oriented, colourful, suitable for a boy
- **Back side (diagram):** schematic image, map, table — clear and uncluttered
- **Background:** simple or white — no distractions
- **Size:** **512×512 px** — mandatory! Larger images won't fit on the tablet display and AOSR buttons will be hidden behind scaling
  - When generating, provide the prompt with `512x512`
  - Shrink existing larger images: `sips -z 512 512 name.png --out name.png`
- **Format:** `.png`
- **File naming:** lowercase letters, no diacritics, underscore before the date
  - Example: `kopf_20260225.png`, `kralle_20260225.png`

---

## 📝 Workflow for creating a new card

### German vocabulary card (Type 1)
1. **Choose a word** (e.g. `der Hund`)
2. **Write an English sentence** with the key word — short and fun
3. **Generate English audio**: `python3 .agent/generate_audio_en.py --deck deck_name "The dog has a big nose."`
4. **Generate image** — cartoon/Pixar style, illustrating the word or sentence
5. **Save image** in `pictures/deck_name/`
6. **Split the German word into syllables** and assign colours (1st blue, 2nd red, ...)
7. **Translate sentence into German**
8. **Generate German audio**: `python3 .agent/generate_audio_de.py --deck deck_name "der Hund"`
9. **Create the card** using the Type 1 template

### Question & Explanation (Type 2)
1. **Think of an interesting question** for an 8-year-old boy
2. **Generate an image** related to the topic
3. **Write a short explanation** (2–4 sentences)
4. *Optional:* generate a diagram or map for the back side
5. **Create the card** following the Type 2 template

---

## 🏷️ Tags and Organization

| Tag | Description |
|-----|-------------|
| `#germanVocabulary` | German vocabulary with sentences |
| `#robkoLearn` | Questions and explanations (nature, history, fun facts) |
| `#Q` | Mandatory AOSR tag — start of a question deck |
| `?` | Mandatory answer separator (default AOSR) |

---

## 🚀 Planned Card Types (Future)

- [ ] `#germanVocabulary` — German vocabulary (active)
- [ ] `#robkoLearn` — fun facts, nature, history
- [ ] `#mathBasics` — mathematics (multiplication tables, fractions, ...)
- [ ] `#geography` — countries, capital cities, rivers
- [ ] `#science` — science and technology

---

*Instructions created: February 2026 | Updated March 2026 — translated to English 🚀*
