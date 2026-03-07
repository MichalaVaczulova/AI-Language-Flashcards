# 📋 INSTRUCTIONS FOR CREATING FLASHCARDS

## 🎯 Goal

Prepare digital flashcards for **FlashcardsLearnGermanKids** in **Obsidian** using the **AOSR (Another Obsidian Spaced Repetition)** plugin.

The cards work with sentences and context — not just isolated words.
**Pictures are always the foundation** — a visual anchor for memorisation.

**Source language: English → German**

---

## 📁 Štruktúra vaultu

```
FlashcardsLearnGermanKids/
├── pictures/           ← card images (PNG/JPG)
├── audio/              ← audio files (EN + DE)
├── flashcards/         ← .md files with cards
├── generate_audio_en.py ← generate English audio (front side)
├── generate_audio_de.py   ← generate German audio (back side)
├── instructions.md     ← this file
```

---

## 🃏 TYP 1: Nemecká slovná zásoba (`#germanVocabulary`)

### Popis

Kartičky na učenie nemeckých slov v kontexte viet. Každé slovo je zasadené do jednoduchej, zaujímavej vety.

---

### Pravidlá tvorby kartičiek

#### ▶ Front of card (question)
- **Short, simple English sentence** — max 1 sentence, no subordinate clauses!
  - ✅ Good: *"Dino has a long <span style="color:#e53935">neck</span>."* or *"A little dino hatched from the <span style="color:#e53935">egg</span>."*
  - ❌ Bad (too complex): *"Brachiosaurus had a neck longer than an entire school bus!"*
- The sentence is **in English** — the key word is the English word, **NOT the German word**
- **Highlight the key English word in red** `#e53935`: `<span style="color:#e53935">neck</span>`
- **English audio** of the sentence — generated with `generate_audio_en.py`
  - `python3 generate_audio_en.py "Dino has a long neck."`
  - Saved in `audio/` folder
- **Picture** in Pixar / cartoon style — colourful, action-oriented, clear
  - Save in `pictures/`
  - Filename: `word_YYYYMMDD.png` — e.g. `kopf_20260225.png`
  - Embed using Obsidian syntax **without path**: `![[kopf_20260225.png]]`

#### ▶ Zadná strana kartičky (odpoveď)
- **Člen** (rod): `der` / `die` / `das` — tučný, zvýraznený
- **Nemecký preklad kľúčového slova** — rozdelený na slabiky s **striedaním farieb** (modrá 🔵 a červená 🔴)
- **Nemecká veta** — preklad celej vety z prednej strany (kurzívou)
  - Nové nemecké slovo zvýrazniť červenou `#e53935`: `<span style="color:#e53935">Kopf</span>`
- **Audio výslovnosť celej nemeckej vety** (MP3) — vložiť pomocou `![[slovo_timestamp.mp3]]`
  - Generovať pomocou inline Python skriptu (nie `generate_audio_de.py`, ten je len pre slová):
    ```bash
    python3 -c "from gtts import gTTS; import os; from datetime import datetime; ts=datetime.now().strftime('%Y%m%d%H%M%S'); tts=gTTS('VETA_PO_NEMECKY', lang='de'); tts.save(f'audio/slovo_{ts}.mp3'); print(f'audio/slovo_{ts}.mp3')"
    ```
  - Uložiť do priečinka `audio/`

#### ▶ Farebné schéma — prehľad

| Where | What | Colour |
|-------|------|--------|
| EN sentence (front side) | Key **English** word | 🔴 Red `#e53935` |
| DE sentence (back side) | Key **German** word | 🔴 Red `#e53935` |
| DE heading — 1st, 3rd, 5th syllable | Syllables of German word | 🔵 Blue `#1a73e8` |
| DE heading — 2nd, 4th, 6th syllable | Syllables of German word | 🔴 Red `#e53935` |

---

### Šablóna kartičky — Veta (AOSR formát)

> **Pravidlá oddeľovania kartičiek:**
> - `#Q #germanVocabulary` sa píše **len raz** — na úplnom začiatku `.md` súboru
> - Kartičky sa oddeľujú pomocou `***` — **bez prázdnych riadkov** pred ani za
> - Nová kartička začína **hneď na riadku pod `***`**

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

## 🃏 TYP 2: Otázka & Vysvetlenie (`#robkoLearn`)

### Popis

Kartičky pre širší obsah — história, príroda, zaujímavosti. Predná strana je otázka + obrázok, zadná strana je vysvetlenie, prípadne doplnkový diagram alebo mapa.

---

### Pravidlá tvorby kartičiek

#### ▶ Predná strana kartičky (otázka)
- **Otázka** — jednoduchá, konkrétna, zaujímavá pre 8-ročného chlapca
  - Príklad: *„Prečo dinosaury vyhynuli?"*
- **Obrázok** — ilustrácia témy (cartoon, realistický, diagram)

#### ▶ Zadná strana kartičky (odpoveď)
- **Krátke vysvetlenie** — 2–4 vety, jasné a zrozumiteľné
- *Voliteľne:* doplnkový obrázok, diagram, mapa alebo tabuľka

---

### Šablóna kartičky — Otázka & Vysvetlenie (AOSR formát)

```markdown
#Q #robkoLearn
Prečo dinosaury vyhynuli?
![[dinosaur_20260224.png]]
?
Pred 66 miliónmi rokov padol na Zem obrovský meteor. Zdvihol mrak prachu, ktorý zablokoval slnko. Rastliny uhynuli a dinosaury nemali čo jesť.
![[dinosaur_impact_diagram_20260224.png]]
***
Ako dlho trvá, kým sa svetlo zo Slnka dostane na Zem?
![[sun_earth_20260224.png]]
?
Svetlo cestuje rýchlosťou 300 000 km/s. Vzdialenosť Zem–Slnko je asi 150 miliónov km. Trvá to približne **8 minút**.
![[light_speed_diagram_20260224.png]]
```

---

## 🖼️ Štýl obrázkov

- **Predná strana:** Pixar / Disney / cartoon — akčné, farebné, vhodné pre chlapca
- **Zadná strana (diagram):** schematický obrázok, mapa, tabuľka — jasný a prehľadný
- **Pozadie:** jednoduché alebo biele — bez rozptyľovania
- **Veľkosť:** **512×512 px** — povinné! Väčšie obrázky sa nezmestia na display tabletu a AOSR tlačítka sú skryté za scrollom
  - Pri generovaní zadávať prompt s `512x512`
  - Existujúce väčšie obrázky zmenšiť: `sips -z 512 512 nazov.png --out nazov.png`
- **Formát:** `.png`
- **Pomenovanie súborov:** malé písmená, bez diakritiky, podčiarkovník pred dátumom
  - Príklad: `kopf_20260225.png`, `kralle_20260225.png`

---

## 📝 Pracovný postup pri tvorbe novej kartičky

### German vocabulary card (Type 1)
1. **Choose a word** (e.g. `der Hund`)
2. **Write an English sentence** with the key word — short and fun
3. **Generate English audio**: `python3 generate_audio_en.py "The dog has a big nose."`
4. **Generate image** — cartoon/Pixar style, illustrating the word or sentence
5. **Save image** in `pictures/`
6. **Split the German word into syllables** and assign colours (1st blue, 2nd red, ...)
7. **Translate sentence into German**
8. **Generate German audio**: `python3 generate_audio_de.py "der Hund"`
9. **Create the card** using the Type 1 template

### Otázka & Vysvetlenie (Typ 2)
1. **Vymysli zaujímavú otázku** pre 8-ročného chlapca
2. **Vygeneruj obrázok** k téme
3. **Napíš krátke vysvetlenie** (2–4 vety)
4. *Voliteľne:* vygeneruj diagram alebo mapu pre zadnú stranu
5. **Vytvor kartičku** podľa šablóny Typ 2

---

## 🏷️ Tagy a organizácia

| Tag | Popis |
|-----|-------|
| `#germanVocabulary` | Nemecká slovná zásoba s vetami |
| `#robkoLearn` | Otázky a vysvetlenia (príroda, história, zaujímavosti) |
| `#Q` | Povinný AOSR tag — začiatok balíka otázok |
| `?` | Povinný oddeľovač odpovede (default AOSR) |

---

## 🚀 Plánované typy kartičiek (budúcnosť)

- [ ] `#germanVocabulary` — nemecká slovná zásoba (aktívny)
- [ ] `#robkoLearn` — zaujímavosti, príroda, história
- [ ] `#mathBasics` — matematika (násobilka, zlomky, ...)
- [ ] `#geography` — krajiny, hlavné mestá, rieky
- [ ] `#science` — veda a technika

---

*Instructions created: February 2026 | Updated March 2026 — language changed to English → German 🚀*
