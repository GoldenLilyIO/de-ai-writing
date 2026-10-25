#!/usr/bin/env python3
"""
De-AI Writing Diagnostic Linter (analyze_readability.py)
Automated verification of readability, cadence modulation, em-dash prohibition,
and banned AI tropes in markdown or plain text files.
Zero external dependencies (pure Python standard library).
"""

import math
import re
import sys
from pathlib import Path

# Ensure UTF-8 output on Windows consoles
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

# Banned AI tropes and formulaic patterns
BANNED_WORDS = [
    "delve", "delving", "delves",
    "tapestry", "tapestries",
    "beacon", "beacons",
    "testament",
    "game-changer", "gamechanger",
    "crucial", "crucially",
    "robust", "robustly",
    "pivotal",
    "foster", "fostering",
    "showcase", "showcasing",
    "vibrant",
    "landscape",
    "realm",
    "unwavering",
    "ever-evolving",
]

BANNED_PHRASES = [
    r"in today['’]?s (?:fast-paced|digital|interconnected) world",
    r"whether you['’]?re a (?:novice|beginner) or (?:seasoned|experienced) pro",
    r"mastering the art and science",
    r"it is important to (?:remember|note) that",
    r"nestled in the (?:heart|middle)",
    r"rich history",
    r"treasure trove",
    r"behind its [^,\.\n]+ lies an unexpected",
]


def count_syllables_in_word(word: str) -> int:
    word = word.lower().strip()
    if not word:
        return 0
    # Remove punctuation
    word = re.sub(r"[^a-z]", "", word)
    if not word:
        return 0
    if len(word) <= 3:
        return 1

    # Heuristic syllable counter for English
    word = re.sub(r"es$", "", word)
    word = re.sub(r"ed$", "", word)
    word = re.sub(r"e$", "", word)

    vowel_groups = re.findall(r"[aeiouy]+", word)
    count = len(vowel_groups)
    return max(1, count)


def clean_markdown(text: str) -> str:
    # Strip YAML frontmatter
    text = re.sub(r"^---\n[\s\S]*?\n---\n", "", text)
    # Strip fenced code blocks
    text = re.sub(r"```[\s\S]*?```", "", text)
    # Strip inline code
    text = re.sub(r"`[^`]*`", "", text)
    # Strip markdown links, keep anchor text
    text = re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"\1", text)
    # Strip images
    text = re.sub(r"!\[[^\]]*\]\([^\)]+\)", "", text)
    # Strip markdown headers (# Header)
    text = re.sub(r"^#+\s+.*$", "", text, flags=re.MULTILINE)
    # Strip blockquotes marker
    text = re.sub(r"^\s*>\s*", "", text, flags=re.MULTILINE)
    # Strip horizontal rules
    text = re.sub(r"^[\*\-_]{3,}\s*$", "", text, flags=re.MULTILINE)
    return text


def split_sentences(text: str) -> list[str]:
    # Match sentences ending in ., !, or ? followed by whitespace or end of line
    raw = re.split(r"(?<=[.!?])\s+", text.strip())
    sentences = []
    for s in raw:
        cleaned = s.strip()
        # Ensure it has word characters
        if re.search(r"\w", cleaned):
            sentences.append(cleaned)
    return sentences


def count_words(sentence: str) -> list[str]:
    return [w for w in re.split(r"\s+", sentence) if re.search(r"\w", w)]


def analyze(text: str, filename: str = "text") -> dict:
    cleaned = clean_markdown(text)
    sentences = split_sentences(cleaned)

    sentence_word_counts = []
    total_words = 0
    total_syllables = 0

    for s in sentences:
        words = count_words(s)
        w_count = len(words)
        if w_count == 0:
            continue
        sentence_word_counts.append(w_count)
        total_words += w_count
        for w in words:
            total_syllables += count_syllables_in_word(w)

    num_sentences = max(1, len(sentence_word_counts))
    avg_sentence_len = total_words / num_sentences if num_sentences else 0

    # Cadence standard deviation
    if len(sentence_word_counts) > 1:
        variance = sum((x - avg_sentence_len) ** 2 for x in sentence_word_counts) / len(sentence_word_counts)
        stdev = math.sqrt(variance)
    else:
        stdev = 0.0

    # Staccato sentences (<= 6 words)
    staccato_count = sum(1 for x in sentence_word_counts if x <= 6)
    staccato_pct = (staccato_count / num_sentences * 100) if num_sentences else 0.0

    # Metronome runs (3+ consecutive sentences with word counts differing by <= 2)
    metronome_runs = 0
    current_run = 1
    for i in range(1, len(sentence_word_counts)):
        if abs(sentence_word_counts[i] - sentence_word_counts[i - 1]) <= 2:
            current_run += 1
            if current_run == 3:
                metronome_runs += 1
        else:
            current_run = 1

    # Flesch calculations
    if total_words > 0 and num_sentences > 0:
        words_per_sentence = total_words / num_sentences
        syllables_per_word = total_syllables / total_words
        flesch_reading_ease = 206.835 - (1.015 * words_per_sentence) - (84.6 * syllables_per_word)
        flesch_grade = (0.39 * words_per_sentence) + (11.8 * syllables_per_word) - 15.59
    else:
        flesch_reading_ease = 0.0
        flesch_grade = 0.0

    # Em dashes check (—, –, or --)
    em_dashes = re.findall(r"[—–]|--", text)

    # Banned tropes check
    flagged_tropes = []
    text_lower = text.lower()
    for word in BANNED_WORDS:
        matches = re.findall(r"\b" + re.escape(word) + r"\b", text_lower)
        if matches:
            flagged_tropes.append(f"{word} ({len(matches)}x)")

    for pattern in BANNED_PHRASES:
        matches = re.findall(pattern, text_lower)
        if matches:
            flagged_tropes.append(f"phrase: '{pattern}'")

    return {
        "filename": filename,
        "total_words": total_words,
        "num_sentences": num_sentences,
        "avg_sentence_len": avg_sentence_len,
        "stdev": stdev,
        "staccato_count": staccato_count,
        "staccato_pct": staccato_pct,
        "metronome_runs": metronome_runs,
        "flesch_reading_ease": flesch_reading_ease,
        "flesch_grade": flesch_grade,
        "em_dashes_count": len(em_dashes),
        "flagged_tropes": flagged_tropes,
    }


def print_report(res: dict) -> bool:
    print("\n" + "=" * 60)
    print(f"DE-AI WRITING DIAGNOSTIC REPORT: {res['filename']}")
    print("=" * 60)

    passed_all = True

    def check(name, value_str, condition, target_str):
        nonlocal passed_all
        status = "[PASS]" if condition else "[FAIL]"
        if not condition:
            passed_all = False
        print(f"{status} {name:<28} : {value_str:<12} (Target: {target_str})")

    # 1. Em dashes
    check("Em Dashes (— or --)", str(res["em_dashes_count"]), res["em_dashes_count"] == 0, "Exactly 0")

    # 2. Banned tropes
    tropes_count = len(res["flagged_tropes"])
    tropes_val = f"{tropes_count} detected" if tropes_count > 0 else "0"
    check("Banned AI Tropes", tropes_val, tropes_count == 0, "0 tropes")

    # 3. Sentence Length StDev
    check("Cadence StDev", f"{res['stdev']:.2f}", res["stdev"] >= 4.0, ">= 4.0")

    # 4. Staccato Sentences (<= 6 words)
    check("Staccato Sentences (<=6w)", f"{res['staccato_pct']:.1f}% ({res['staccato_count']})", res["staccato_pct"] >= 10.0, ">= 10.0%")

    # 5. Metronome Runs
    check("Metronome Runs (3+ similar)", str(res["metronome_runs"]), res["metronome_runs"] <= 2, "<= 2")

    # 6. Flesch Reading Ease (50.0 to 85.0 covers accessible social copy through standard articles)
    fre = res["flesch_reading_ease"]
    check("Flesch Reading Ease", f"{fre:.1f}", 50.0 <= fre <= 85.0, "50.0 - 85.0")

    # 7. Grade Level (4.0 to 11.0 covers punchy conversational writing through technical trade prose)
    grade = res["flesch_grade"]
    check("Flesch-Kincaid Grade", f"{grade:.1f}", 4.0 <= grade <= 11.0, "4.0 - 11.0")

    print("-" * 60)
    print(f"Total Words: {res['total_words']} | Total Sentences: {res['num_sentences']} | Avg Words/Sentence: {res['avg_sentence_len']:.1f}")

    if res["flagged_tropes"]:
        print("\nFlagged Tropes Detail:")
        for t in res["flagged_tropes"]:
            print(f"  - {t}")

    print("=" * 60)
    if passed_all:
        print("OVERALL RESULT: PASSED (Human, concrete, modulated prose)")
    else:
        print("OVERALL RESULT: FAILED GATES (Review flagged items above)")
    print("=" * 60 + "\n")
    return passed_all


def main():
    if len(sys.argv) < 2:
        print("Usage: python analyze_readability.py <path-to-markdown-or-text-file>")
        sys.exit(1)

    file_path = Path(sys.argv[1])
    if not file_path.exists():
        print(f"Error: File '{file_path}' does not exist.")
        sys.exit(1)

    text = file_path.read_text(encoding="utf-8", errors="replace")
    results = analyze(text, filename=file_path.name)
    success = print_report(results)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
