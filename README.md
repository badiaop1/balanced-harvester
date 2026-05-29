# Balanced Harvester Engine for /MCL Futures (AI‑Assisted)

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Build](https://img.shields.io/badge/Build-Passing-brightgreen.svg)

The **Balanced Harvester** is a modular, AI‑assisted trading engine designed to evaluate 
Micro Crude Oil (/MCL) vertical spreads using a structured pipeline:

1. **Spread Generation**  
2. **Risk Modeling**  
3. **AI Explanation Layer**  
4. **Orchestration & Output**  
5. **Dashboards & Screenshots**

This repository provides a clean, extensible architecture suitable for:
- Futures spread evaluation  
- Risk envelope validation  
- AI‑assisted trade summaries  
- Notebook‑based dashboards  
- Modular component upgrades  

---

## 🧩 Architecture Overview

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

