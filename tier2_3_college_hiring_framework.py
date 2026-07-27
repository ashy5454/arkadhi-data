import pandas as pd
import json
import os
import sys

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

"""
================================================================================
ARKADHI DATA - TIER 2/3 COLLEGE HIRING FRAMEWORK & AI BOOTCAMP CURRICULUM
================================================================================
Specially tailored for hiring & up-skilling students from Tier 2/3 engineering
colleges in Hyderabad/Telangana (Vasavi, Malla Reddy, SNIST, VNR, BVRIT, etc.).
================================================================================
"""

def generate_hiring_and_course_docs():
    print("📊 Generating Tier 2/3 College Hiring Guide & Bootcamp Curriculum...", flush=True)

    # 1. TIER2_3_COLLEGE_HIRING_GUIDE.md
    hiring_guide = """# 🎯 Arkadhi Data: Tier 2 & Tier 3 College Hiring & Talent Sourcing Guide
### Sourcing High-Agency Diamonds in the Rough from Vasavi, Malla Reddy, SNIST, VNR & Regional Engineering Colleges

---

## 📌 1. The Tier 2/3 Talent Reality in India

Students from Tier 2 and Tier 3 engineering colleges in Hyderabad/Telangana (e.g. **Vasavi College of Engineering**, **Malla Reddy Engineering College**, **SNIST**, **VNR VJIET**, **BVRIT**) are often ignored by elite US labs or Big Tech recruiters. 

However, Tier 2/3 colleges contain the **highest concentration of hungry, high-agency builders** who are eager to prove themselves, provided you know how to filter through the noise.

```text
┌────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ TIER 2/3 CANDIDATE SPECTRUM IN TELANGANA / INDIA                                                  │
├───────────────────────────┬────────────────────────────────────────────────────────────────────────┤
│ 90% Noise (Avoid)         │ Rote-learners, generic resume copy-pasters, tutorial-project coders.   │
├───────────────────────────┼────────────────────────────────────────────────────────────────────────┤
│ Top 10% Gems (Target)     │ Self-taught hackers, hackathon obsessives, nocturnal GitHub committers,│
│                           │ eager to build real AI projects and publish papers.                     │
└───────────────────────────┴────────────────────────────────────────────────────────────────────────┘
```

---

## 🔍 2. How to Identify High Agency in Vasavi & Malla Reddy Students

High agency in a Tier 2/3 candidate does NOT look like fluent English speeches or polished LinkedIn posts. It looks like **un-prompted building energy**:

### 🎯 5 Raw Signals of High Agency:
1. **GitHub Activity Beyond Coursework:** Public commits on personal side projects at 2 AM, not just college lab assignments.
2. **Hackathon Persistence:** They participated in hackathons (even regional ones) and built working prototypes under 24-hour pressure.
3. **Self-Taught Resourcefulness:** They learned PyTorch/FastAPI/Docker from YouTube/GitHub rather than waiting for college faculty to teach it.
4. **Indifferent to Corporate Bureaucracy:** They want to build real systems rather than spend 6 months grinding aptitude tests for mass recruiters (TCS/Wipro/Infosys).
5. **Obsession with Hardware/GPU Compute:** They know how to optimize VRAM, handle CUDA errors, or use free Kaggle/Colab GPUs effectively.

---

## 🧪 3. The 4-Stage Screening & Filtration Funnel

```text
Stage 1: The No-Resume Code Filter
 └── Ignore college marks/CGPA. Require a link to 1 public GitHub repo or working project.

Stage 2: The 48-Hour Un-Prompted Trial Task (Paid)
 └── Hand candidate a real issue in arkadhi-data (e.g., "Implement a custom 2D k-WTA PyTorch activation").
 └── High-agency candidates debug setup errors independently and submit a working PR in <24 hours.

Stage 3: The Debugging & Problem-Solving Audit
 └── Ask: "When your PyTorch code hit CUDA Out of Memory, what exact steps did you take to fix it?"
 └── High-agency candidates describe tensor memory clearing, batch sizing, or gradient accumulation.

Stage 4: The Fire-Fast Trial Period (2 Weeks)
 └── If a candidate requires constant hand-holding or makes excuses for 2 consecutive sprints, cut them.
```

---

## 🏆 4. The Non-Monetary Incentive Stack for Tier 2/3 Candidates

```text
┌────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ WHAT MOTIVATES TIER 2/3 BUILDERS IN INDIA                                                         │
├───────────────────────────┬────────────────────────────────────────────────────────────────────────┤
│ 1. arXiv Co-Authorship    │ Global academic credibility on published AI architecture papers.       │
├───────────────────────────┼────────────────────────────────────────────────────────────────────────┤
│ 2. Public GitHub Profile  │ Proof of real engineering impact on high-visibility repositories.      │
├───────────────────────────┼────────────────────────────────────────────────────────────────────────┤
│ 3. Dedicated Compute      │ Un-restricted access to GCP A100/T4 GPU VM compute for research.       │
├───────────────────────────┼────────────────────────────────────────────────────────────────────────┤
│ 4. Revenue-Share Pool     │ 15-20% transparent revenue pool tied to Prexi API middleware sales.    │
└───────────────────────────┴────────────────────────────────────────────────────────────────────────┘
```
"""

    with open("TIER2_3_COLLEGE_HIRING_GUIDE.md", "w", encoding="utf-8") as f:
        f.write(hiring_guide)

    # 2. ARKADHI_AI_BOOTCAMP_CURRICULUM.md
    curriculum = """# 📚 Arkadhi Data: 14-Day Fast-Track AI Architecture Bootcamp
### Up-skilling Tier 2/3 Engineering Candidates (Vasavi / Malla Reddy Grads) into High-Velocity AI Researchers

Designed to bridge the gap between basic Python knowledge and writing custom PyTorch neural network architectures within 14 days.

---

## 📅 Day-by-Day Intensive Curriculum

```text
┌────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ WEEK 1: PYTORCH CORE & TENSOR MECHANICS                                                            │
├───────────────┬────────────────────────────────────────────────────────────────────────────────────┤
│ Day 1 – 2     │ PyTorch Tensor Fundamentals, Vectorization & GPU Memory Allocation                  │
│ Day 3 – 4     │ Custom Loss Functions, Autograd Mechanics & Perplexity Calculations                 │
│ Day 5 – 7     │ Building Neural Networks from Scratch & Debugging CUDA OOM Exceptions              │
├───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ WEEK 2: ADVANCED NON-ATTENTION ARCHITECTURES & EVALUATION                                          │
├───────────────┬────────────────────────────────────────────────────────────────────────────────────┤
│ Day 8 – 10    │ CMP k-WTA Sparse Relational Memory & Non-Attention Recurrence                     │
│ Day 11 – 12   │ Supervised Fine-Tuning (SFT), LoRA Adaptations & Tokenizer Packing                │
│ Day 13 – 14   │ Automated SWE-bench Docker Benchmarking & Git Pull Request Workflows               │
└───────────────┴────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 🛠️ Required Hands-On Capstone Project

Every bootcamp candidate must complete the **Arkadhi Capstone**:
1. Implement a sparse $k$-WTA activation function in PyTorch.
2. Train a 50M parameter baseline model on 1 Million tokens of code text.
3. Benchmark token throughput (tokens/sec) and state memory norm.
4. Submit a clean pull request to `ashy5454/arkadhi-data`.
"""

    with open("ARKADHI_AI_BOOTCAMP_CURRICULUM.md", "w", encoding="utf-8") as f:
        f.write(curriculum)

    # 3. README.md for arkadhi-data
    readme = """# 🚀 Arkadhi Data: AI Research Lab OS & Tier 2/3 College Hiring Framework

[![Repository](https://img.shields.io/badge/Repo-ashy5454%2Farkadhi--data-purple?style=for-the-badge)](https://github.com/ashy5454/arkadhi-data)
[![Hiring Guide](https://img.shields.io/badge/Guide-Tier__2%2F3__Hiring--Guide-blue?style=for-the-badge)](./TIER2_3_COLLEGE_HIRING_GUIDE.md)
[![Bootcamp](https://img.shields.io/badge/Course-14--Day__AI__Bootcamp-green?style=for-the-badge)](./ARKADHI_AI_BOOTCAMP_CURRICULUM.md)

Welcome to **Arkadhi Data**—the master repository for AI Architecture Research Lab operations, Tier 2/3 engineering college hiring frameworks (Vasavi, Malla Reddy, SNIST, VNR), and 100,000 scraped Reddit AI market intelligence datasets.

---

## 📂 Repository Contents

* 📄 **[`TIER2_3_COLLEGE_HIRING_GUIDE.md`](./TIER2_3_COLLEGE_HIRING_GUIDE.md)** — Sourcing and filtering high-agency talent from Tier 2/3 engineering colleges in Telangana/India.
* 📚 **[`ARKADHI_AI_BOOTCAMP_CURRICULUM.md`](./ARKADHI_AI_BOOTCAMP_CURRICULUM.md)** — 14-Day Fast-Track PyTorch & AI Architecture Training Bootcamp.
* 📊 **[`reddit_100k_ai_dataset.csv`](./reddit_100k_ai_dataset.csv)** — Complete 100,000 scraped Reddit AI discussions dataset (27.1 MB).
"""

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme)

    print("✅ Created TIER2_3_COLLEGE_HIRING_GUIDE.md, ARKADHI_AI_BOOTCAMP_CURRICULUM.md, and README.md!", flush=True)

if __name__ == "__main__":
    generate_hiring_and_course_docs()
