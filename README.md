# De-AI Writing

> An open-source, battle-tested editorial pipeline and diagnostic linter that transforms formulaic, generic AI text into grounded, scene-driven human writing.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Zero Em Dashes](https://img.shields.io/badge/Em%20Dashes-Exactly%200-success.svg)](#2-absolute-em-dash-prohibition)
[![No Banned Tropes](https://img.shields.io/badge/Banned%20Tropes-Purged-success.svg)](#4-banned-ai-tropes-purge)

---

## How This Differs From Other De-AI Writing Skills

Many other de-ai writing skills and prompts take a surface-level approach:
* They swap synonyms to shift token probability.
* They inject conversational filler (*"Honestly,"*, *"To be fair,"*, *"Let's be real"*).
* They soften tone without addressing underlying rhythm or structure.

**Human writing does not sound authentic because of casual filler.** It sounds authentic because of:
1. **Sensory Grounding**: Real tools, specific geography, physical friction, and concrete nouns.
2. **Asymmetric Rhythm**: A musical mix of staccato punch verdicts (2 to 6 words) and longer explanatory sentences.
3. **Narrative Tension**: Starting in the middle of the action (*in media res*), avoiding throat-clearing intros, and ending on a decisive floor verdict instead of a robotic summary.

`de-ai-writing` focuses on architectural editorial discipline, cadence modulation, and automated diagnostic verification.

---

## The 5-Stage Editorial Pipeline

```
Stage 1: Pre-Flight Fact Dossier (Sensory Anchors & Concrete Nouns)
   │
   ▼
Stage 2: Voice Calibration (Role, Tone, Authority, Domain Lexicon)
   │
   ▼
Stage 3: Narrative Architecture (In Media Res, Zoom Modulation, Organic Quotes)
   │
   ▼
Stage 4: Cadence & Vocabulary Surgery (Staccato Rhythm, 0 Em Dashes, Trope Purge)
   │
   ▼
Stage 5: Automated Diagnostic Verification (analyze_readability.py)
```

---

### Stage 1: Pre-Flight Fact Dossier

**The Law of Concrete Nouns**: Abstract fluff is the AI's fallback defense when it lacks facts. When an LLM does not know the exact street corner, the key of an accordion, or the temperature in the room, it compensates with empty adjectives (*"a vibrant atmosphere filled with passionate artisans"*).

Before writing a single sentence of prose, assemble a **Sensory Dossier**:
* **Verified Proper Nouns**: Documented people, founders, organizers, or subject experts. Never invent personas.
* **Specific Regional Geography**: Real intersections, highways, exits, and administrative divisions (e.g. *I-10 Exit 64*, *Rue de l'Acadie*).
* **Physical Hardware & Tools**: Exact production equipment (e.g., *benchtop pH meter with 2-point calibration*, *induction burner*, *5-gallon food-grade HDPE bucket*).
* **Sensory Anchors**: At least one sound (hum of a swamp cooler), smell (capsaicin steam), and texture (sticky tare buttons).

---

### Stage 2: Publication Voice Calibration

Calibrate the tone profile to the domain:
* **The Role**: Who is speaking? A commercial production manager, a software architect, or a regional cultural chronicler.
* **The Tone**: Pragmatic peer, porch-side guide, unhedged operator.
* **Craft Vocabulary**: Real domain terminology (titratable acidity, water activity, 21 CFR 114, latency budgets).
* **Authorship Integrity**: Attribute content to the verified practitioner or `<Brand> Editorial Team`.

---

### Stage 3: Narrative Architecture

Break the predictable AI outline (*Hook -> 3-paragraph point -> Heading -> 3-paragraph point -> Summary*):

* **In Media Res Openings**: Never start by explaining what the article is about. Cut the throat-clearing warm-up. Drop the reader directly into physical motion, friction, or sound.
* **Zoom Modulation**: Alternate between **Micro Close-Up** (hands on tools, room atmosphere) and **Macro Pull-Back** (regulations, history, economic context). Never stay in abstract theory for more than two sentences.
* **Organic Quotes**: Weave quotes into narrative sentences with physical action tags (*Lyon rests the scroll of his fiddle against his collarbone. "If we don't teach the children how to chord," he says...*).
* **Anti-Summary Ending**: Never write a section titled *"Conclusion"*, *"Final Thoughts"*, or *"Wrapping Up"*. End on a lingering visual detail or a sharp, unhedged verdict.

---

### Stage 4: Cadence & Vocabulary Surgery

#### 1. Staccato-Legato Cadence (Break the Metronome)
* **The Staccato Punch (2 to 6 words)**: *"Don't do it."*, *"Wear the glasses."*, *"Water dilutes heat."*, *"Start low."*
* **The Legato Flow (15 to 22 words)**: Technical explanations describing mechanics and real-world consequences.
* **Target Benchmarks**:
  * Sentence Length Standard Deviation: $\ge 4.0$
  * Staccato Sentences ($\le 6$ words): $\ge 10\%$ to $25\%$ of total sentences.
  * Metronome Runs (3+ consecutive sentences of similar length): $\le 2$.

#### 2. Absolute Em Dash Prohibition
* **ZERO em dashes (`—` or `--`)**.
* Large Language Models heavily overuse em dashes to stitch disjointed thoughts together. 
* Use clean periods, colons, or commas. Removing em dashes forces clean, deliberate sentence structure.

#### 3. Banned AI Tropes Purge

| Banned AI Pattern | Why It Fails | Replacement |
| :--- | :--- | :--- |
| `delve`, `tapestry`, `beacon`, `testament` | AI vocabulary fingerprints | Plain action verbs (*examine*, *mix*, *track*, *build*) |
| `crucial`, `game-changer`, `robust`, `pivotal` | Vague marketing buzzwords | Name the specific technical or financial benefit |
| *"Behind its [X] lies an unexpected [Y]"* | Formulaic brochure trope | *"Underneath that skin is legitimate [Y]"* |
| *"In today's fast-paced world..."* | Pointless throat-clearing | Cut entirely; open with the action or problem |
| *"Whether you're a novice or seasoned pro"* | Symmetrical filler | Cut entirely; speak directly to the practitioner |
| *"Mastering the art and science"* | Corporate cliché | Name the exact skill (*"dialing in your batch math"*) |
| *"Nestled in the heart of..."* | Travel brochure cliché | Name the exact road, parish, or highway intersection |
| *"Rich history"* / *"Treasure trove"* | Lazy tourist tropes | Cite the specific decade or archival record |
| *"It is important to remember that"* | Passive patronizing filler | Cut; state the rule directly as an imperative |

---

### Stage 5: Automated Diagnostic Linter

Included in this repository is a zero-dependency Python script that validates text against the editorial gates:

```bash
python scripts/analyze_readability.py <path-to-file>
```

#### Verification Checklist:
- [x] **Em Dashes (`—` or `--`)**: Exactly 0
- [x] **Banned AI Tropes**: 0 detected
- [x] **Cadence StDev**: $\ge 4.0$
- [x] **Staccato Sentences ($\le 6$ words)**: $\ge 10\%$
- [x] **Metronome Runs**: $\le 2$
- [x] **Flesch Reading Ease**: 50.0 to 85.0
- [x] **Flesch-Kincaid Grade Level**: 4.0 to 11.0

---

## How to Use

### 1. With Grok (xAI)
You can instruct Grok on X or x.ai by linking to this repository directly:

> *"Read the writing framework at https://github.com/GoldenLilyIO/de-ai-writing and rewrite the following text according to its rules: [paste draft]"*

Alternatively, copy the prompt below into Grok's Custom Instructions or chat prompt:

```markdown
Adopt the De-AI Writing editorial framework:
1. The Law of Concrete Nouns: Ground all prose in physical tools, exact measurements, sensory friction (sound, smell, texture), and verified facts. Zero hallucinated personas.
2. In Media Res: Cut throat-clearing warm-ups. Start directly in the motion or conflict.
3. Cadence Rhythm: Modulate between short staccato verdicts (2-6 words) and longer legato sentences. Aim for a sentence length standard deviation >= 4.0.
4. Zero Em Dashes: Never use em dashes (— or --). Use periods, colons, or clean commas.
5. Zero Banned Tropes: Purge delve, tapestry, beacon, testament, game-changer, robust, crucial, and symmetrical fillers ("whether you're a...", "in today's fast-paced world").
6. Anti-Summary: Never write a conclusion or summary section. End on a decisive floor verdict.
```

### 2. With Claude, ChatGPT, or Cursor
* **Claude / ChatGPT**: Paste the prompt above into your project instructions or system prompt.
* **Antigravity / Cursor / Claude Code**: Add this repository as a submodule or copy [`SKILL.md`](SKILL.md) into your skills directory (`~/.gemini/config/skills/de-ai-writing/` or `.cursor/skills/`).

---

## Example Case Study

### Before (AI Draft)
> *Mike Hultquist at Chili Pepper Madness lays out both bottling paths clearly. 🌶️*
> *Raw: no heat, the live culture stays, and the bottles live in the fridge and may need an occasional burp. Cooked: bring the blended sauce to a boil and simmer 15 minutes, which stops fermentation but costs you the live culture. Either way, check pH. Below 4.6 is the line, he suggests about 3.5 for home cooks, and his finished sauce measured 3.7. I log each batch's reading in Mash Metrics before I decide.*
> *Raw and refrigerated, or cooked: which way do you bottle, and why?*

### After (De-AI Editorial Rewrite)
> *Mike Hultquist over at Chili Pepper Madness outlines two bottling paths every hot sauce maker faces.*
>
> *Path one: keep it raw. The live culture survives, the flavor stays bright, and the bottles go straight into the fridge. You still have to watch them. Cold slows fermentation, but pressure still builds up over time.*
>
> *Path two: cook it down. Bringing the blended sauce to a simmer for 15 minutes halts fermentation completely. You lose the probiotic culture, but you gain shelf stability and peace of mind.*
>
> *Either way, check your pH. 4.6 is the regulatory ceiling, but 3.5 gives home bottlers a safe buffer against drift. Mike logged his finished batch at 3.7. I log every reading in Mash Metrics before making the call.*
>
> *Do you keep the live culture cold, or pasteurize for shelf life?*

### Diagnostic Results for Rewrite
```
============================================================
DE-AI WRITING DIAGNOSTIC REPORT: hot_sauce_bottling.md
============================================================
[PASS] Em Dashes (— or --)          : 0            (Target: Exactly 0)
[PASS] Banned AI Tropes             : 0            (Target: 0 tropes)
[PASS] Cadence StDev                : 4.16         (Target: >= 4.0)
[PASS] Staccato Sentences (<=6w)    : 30.8% (4)    (Target: >= 10.0%)
[PASS] Metronome Runs (3+ similar)  : 0            (Target: <= 2)
[PASS] Flesch Reading Ease          : 81.0         (Target: 50.0 - 85.0)
[PASS] Flesch-Kincaid Grade         : 4.5          (Target: 4.0 - 11.0)
------------------------------------------------------------
Total Words: 135 | Total Sentences: 13 | Avg Words/Sentence: 10.4
============================================================
OVERALL RESULT: PASSED (Human, concrete, modulated prose)
============================================================
```

---

## License

This project is licensed under the [MIT License](LICENSE) by Golden Lily Enterprises.
