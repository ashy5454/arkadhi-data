import os
import sys

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

"""
================================================================================
DAVID SENRA'S FOUNDERS PODCAST: ELON MUSK OPERATING PRINCIPLES FOR YOUR AI LAB
================================================================================
Extracts core takeaways from David Senra's Founders Podcast episodes on Elon Musk
(Ashlee Vance & Walter Isaacson biographies) and applies them directly to your lab.
================================================================================
"""

def generate_elon_musk_founders_doc():
    doc_content = """# 🚀 Elon Musk's Operating Principles (David Senra's Founders Podcast)
### Applying History's Greatest Founder Mindset to Your AI Research Lab & Prexi Revenue Engine

---

## 📌 Executive Summary & Key Takeaway
On David Senra's **Founders Podcast**, David analyzes thousands of hours of founder biographies. His study of Elon Musk (Ashlee Vance & Walter Isaacson biographies) highlights that Elon's superpower is **Maniacal Urgency**, **First Principles Reasoning**, and **Deleting Waste**.

```text
┌────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ ELON MUSK'S CORE OPERATING MATRIX (FOUNDERS PODCAST SYNTHESIS)                                     │
├───────────────────────────┬────────────────────────────────────────────────────────────────────────┤
│ 1. Maniacal Urgency       │ Speed is the ultimate competitive moat. Every delay is a bug.          │
├───────────────────────────┼────────────────────────────────────────────────────────────────────────┤
│ 2. First Principles Math  │ Boil problems down to raw physics/FLOPs, not conventional consensus.  │
├───────────────────────────┼────────────────────────────────────────────────────────────────────────┤
│ 3. The 5-Step Algorithm   │ Delete requirements first. Simplify second. Automate last.            │
├───────────────────────────┼────────────────────────────────────────────────────────────────────────┤
│ 4. Attack the Bottleneck  │ Find the 1 single thing blocking progress and destroy it relentlessly. │
├───────────────────────────┼────────────────────────────────────────────────────────────────────────┤
│ 5. Hardcore Culture       │ Surround yourself with high-agency builders who love extreme velocity. │
└───────────────────────────┴────────────────────────────────────────────────────────────────────────┘
```

---

## 🛠️ 1. Applying Elon's 5-Step Algorithm to Your AI Lab & Prexi

### Step 1: Make Requirements Less Dumb
* **Conventional Consensus:** "You need 128k context windows and massive quadratic self-attention matrices for AI agents."
* **First Principles Correction:** 95% of long-context tokens are stack traces, duplicate prompts, and system noise. Delete the noise; keep 259 relevant tokens.

### Step 2: Delete the Part or Process
* Delete unnecessary LLM calls, verbose JSON schemas, and redundant status meetings.
* If you aren't adding back 10% of deleted code/process later, you aren't deleting enough.

### Step 3: Simplify & Optimize
* Optimize neural network compute density using **3.05% active $k$-WTA sparse codebook memory**, saving 96.95% of unnecessary FLOPs.

### Step 4: Accelerate Cycle Time
* Compress paper-to-code shipping cycles from 6 months down to **7 days**.

### Step 5: Automate Execution
* Automate evaluation loops via PyTest & SWE-bench Docker scripts.

---

## ⏰ 2. How a 5-6 Hour Founder Applies "Maniacal Focus"

Elon Musk moves at insane speed because he focuses 100% of his energy on the **Current Critical Bottleneck**:

```text
┌────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ FOUNDER MANIACAL FOCUS QUEUE                                                                       │
├───────────────────────────┬────────────────────────────────────────────────────────────────────────┤
│ Bottleneck 1: Hiring      │ Hour 1-2: Review 48-Hr Trial Task PRs from Vasavi / Malla Reddy grads. │
├───────────────────────────┼────────────────────────────────────────────────────────────────────────┤
│ Bottleneck 2: Revenue     │ Hour 3-4: Pitch T-Hub startups on Free LLM Token Audits for Prexi.     │
├───────────────────────────┼────────────────────────────────────────────────────────────────────────┤
│ Bottleneck 3: R&D Math    │ Hour 5-6: Write PyTorch loss formulations (cmp_1b_model.py).           │
└───────────────────────────┴────────────────────────────────────────────────────────────────────────┘
```

---

## ⚡ 3. David Senra's "Hardcore Culture" Lessons for India Hiring

From David Senra's analysis of SpaceX and Tesla:
1. **Never Compromise on Agency:** "One bad hire who requires hand-holding will slow down 5 great builders."
2. **Insane Standards:** Set aggressive deadlines that force creative solutions (e.g. *"Write a custom PyTorch activation layer in 24 hours"*).
3. **Mission Over Money:** High-agency builders stay because they want to build historic systems, publish arXiv papers, and solve hard non-transformer problems.
"""

    with open("ELON_MUSK_FOUNDERS_PODCAST_PLAYBOOK.md", "w", encoding="utf-8") as f:
        f.write(doc_content)

    print("✅ Created ELON_MUSK_FOUNDERS_PODCAST_PLAYBOOK.md!", flush=True)

if __name__ == "__main__":
    generate_elon_musk_founders_doc()
