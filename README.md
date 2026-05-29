# Balanced Harvester Engine for /MCL Futures (AI‑Assisted)

The Balanced Harvester is an AI‑assisted trading engine designed to evaluate, construct, and monitor multi‑layered vertical spreads for /MCL futures. It solves a real constraint I face as an advanced retail derivatives trader: maintaining a stable risk envelope while operating under limited buying power.

---

## 🔧 Engine Capabilities

### 1. Spread Generation
Automatically constructs candidate vertical spreads such as:
- 122/125
- 123/126
- 124/127

Based on:
- current chain
- volatility
- distance to expiry
- envelope rules

### 2. Risk Modeling
A deterministic risk engine evaluates:
- max profit
- max loss
- breakevens
- theta decay
- envelope compliance

### 3. AI Layer
An LLM assists with:
- generating structured trade notes
- summarizing risk scenarios
- validating envelope fit
- explaining trade rationale in plain language

All AI outputs follow strict JSON schemas to prevent hallucinations.

---

## 📁 Repository Structure
balanced-harvester/
│
├── engine/
│   ├── spread_generator.py
│   ├── risk_model.py
│   ├── envelope_rules.json
│   └── examples/
│       ├── sample_chain.csv
│       └── sample_spreads.json
│
├── ai_layer/
│   ├── trade_explainer_prompt.txt
│   ├── risk_summary_prompt.txt
│   └── evaluator.py
│
├── schemas/
│   ├── spread_schema.json
│   ├── risk_output_schema.json
│   └── ai_summary_schema.json
│
├── dashboards/
│   ├── harvester_notebook.ipynb
│   └── harvester_dashboard.png
│
└── screenshots/
    ├── overview.png
    ├── spread_evaluation.png
    └── ai_summary.png

---

## 📊 Example Outputs

- Spread evaluation JSON  
- AI‑generated trade summary  
- Dashboard screenshot  

---

## 🎯 What I Learned

- How to combine deterministic trading logic with AI‑generated insights  
- How to design guardrails for LLMs in high‑stakes workflows  
- How to build cockpit‑style tools for rapid decision‑making  
- How to structure a multi‑layered trading engine cleanly  

---

## 📜 License
MIT (optional)

