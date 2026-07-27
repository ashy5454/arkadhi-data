import os
import sys

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

"""
================================================================================
CAN ENGINEERS SELL? SOURCING & TRAINING TECHNICAL SALES ENGINEERS IN INDIA
================================================================================
"""

def update_hiring_guide():
    doc_path = "TIER2_3_COLLEGE_HIRING_GUIDE.md"
    
    sales_section = """
---

## 💼 5. Can Engineers Sell? Sourcing & Training Technical Sales Engineers

### 💡 The Reality of B2B AI Infrastructure Sales
* **The Myth:** Selling B2B AI middleware requires traditional corporate sales MBAs in suits.
* **The Truth:** Corporate sales reps **cannot** sell AI infrastructure to CTOs because they don't understand PyTorch, token prefill latency, or KV-cache VRAM limits.
* **The Best Sellers for Dev Tools ARE Engineers.** (Examples: Patrick Collison at Stripe, Mitchell Hashimoto at HashiCorp, Guillermo Rauch at Vercel). In developer infrastructure, **technical credibility IS the sales pitch**.

```text
┌────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ THE 3 TYPES OF TECHNICAL SELLERS YOU NEED                                                         │
├───────────────────────────┬────────────────────────────────────────────────────────────────────────┤
│ 1. Inbound Content Seller │ Writes deep technical teardowns on HackerNews, X, and r/developersIndia│
│                           │ ("How we cut LLM API bills by 65% with 1 line of code").               │
├───────────────────────────┼────────────────────────────────────────────────────────────────────────┤
│ 2. Audit Solution Engineer│ Takes 1 day of a customer's prompt logs, runs a free Prexi token audit, │
│                           │ and demonstrates: "You are wasting ₹3.5 Lakhs/month on uncompressed logs."│
├───────────────────────────┼────────────────────────────────────────────────────────────────────────┤
│ 3. Ecosystem Hacker       │ Runs hands-on developer workshops at T-Hub, IIIT-H CIE, and Bengaluru  │
│                           │ dev meetups, converting attendees into live API subscribers.           │
└───────────────────────────┴────────────────────────────────────────────────────────────────────────┘
```

---

### 🔍 How to Identify "Sales-Engineers" in Vasavi & Malla Reddy Students

When interviewing Tier 2/3 engineering candidates, search for candidates who possess **Technical Fluency + Customer Empathy**:

1. **Hackathon Pitchers:** Students who didn't just write code at hackathons, but led the final demo presentation to judges.
2. **Community Managers / Tech Fest Organizers:** Students who organized college tech fests, managed sponsorships, or ran college developer clubs.
3. **Technical Writers & Content Creators:** Candidates who run YouTube tech channels, write Medium/Substack blogs, or actively post side-projects on X/LinkedIn asking for user feedback.
4. **Consultative Mindset:** When given a technical problem, they immediately ask: *"How will real users interact with this API?"* rather than just talking about code syntax.
"""

    if os.path.exists(doc_path):
        with open(doc_path, "a", encoding="utf-8") as f:
            f.write(sales_section)
        print(f"✅ Appended Technical Sales section to '{doc_path}'.", flush=True)

if __name__ == "__main__":
    update_hiring_guide()
