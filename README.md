Balanced Harvester Engine for /MCL Futures (AI‑Assisted)
![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Build](https://img.shields.io/badge/Build-Passing-brightgreen.svg)
The Balanced Harvester is a modular, AI‑assisted trading engine designed to evaluate
Micro Crude Oil (/MCL) vertical spreads using a structured pipeline:
Spread Generation
Risk Modeling
AI Explanation Layer
Orchestration & Output
Dashboards & Screenshots
This repository provides a clean, extensible architecture suitable for:
Futures spread evaluation
Risk envelope validation
AI‑assisted trade summaries
Notebook‑based dashboards
Modular component upgrades
---
🧩 Architecture Overview
```mermaid
flowchart TD
    A[Spread Generator] --> B[Risk Model]
    B --> C[AI Layer]
    C --> D[Orchestrator]
    D --> E[Dashboards]
    D --> F[Screenshots]

    subgraph Engine
        A
        B
    end

    subgraph AI
        C
    end

    subgraph Output
        E
        F
    end
```
📁 Repository Structure
```
balanced-harvester/
│
├── engine/
│   ├── spread_generator.py
│   ├── risk_model.py
│   └── examples/
│       ├── sample_chain.csv
│       └── sample_spreads.json
│
├── ai_layer/
│   ├── evaluator.py
│   ├── trade_explainer_prompt.txt
│   └── risk_summary_prompt.txt
│
├── schemas/
│   ├── spread_schema.json
│   └── risk_schema.json
│
├── orchestrator/
│   ├── harvester.py
│   └── __init__.py
│
├── dashboards/
│   ├── harvester_notebook.ipynb
│   └── harvester_dashboard.png
│
└── screenshots/
    ├── engine_flow.png
    └── dashboard_view.png
```
