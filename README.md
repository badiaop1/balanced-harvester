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

## 📁 Repository Structure

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
