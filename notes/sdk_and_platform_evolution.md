# SDK & Platform Evolution — Deployment Instructions

## From Research Script to Production SDK
1. **Structure**: Move core to `src/` as protected class. Immutable 5-line kernel locked.
2. **DomainRegistry**: Magnificent Eight as factory defaults. New domains (bridge vibration, power grid, etc.) added via registry without touching kernel.
3. **API Contract**:
   - `data_stream`
   - `domain_type`
   - `callback` (log, Slack, shutdown, etc.)
4. **Data Sanitizers**: `pre_process()` for missing values, resampling, [0,1] normalization before $R_u$.
5. **Docs**: Docstrings for median=5 and gate choices. Quickstart `main.py` example.

**Recommendation**: Lock the Magnificent Eight gates as expert-system presets so users cannot break the engine by mis-tuning. Adaptive burn-in optional for new domains.

## Phase 1 — Auto-Tuner
Burn-in on historical data → compute quiet-state $\sigma$ → set gate at $6\sigma$ or $7\sigma$ above noise floor automatically.

## Phase 2 — Causality Tracer
Vector residual: track which input variable (current, temperature, pressure, etc.) deviated first. Output: "Rupture due to pressure spike in sector 4".

## Phase 3 — Closed-Loop Intervention
When alarm=True, trigger `dampen()`: inject gas, rebalance portfolio, adjust cooling, etc. Self-healing controller.

## Modular Spine
`SpineFactory` class so users can plug their own spine definitions.

## Telemetry
Standard ingestion: CSV, JSON stream, API hook → same $R_u$ engine.

## Community
Global database of spines for new domains.

## Deployment Path
1. Package as pip-installable (`universal-rupture-detector`).
2. Domain-selector CLI or web app.
3. Push current kernel + notes now; finalize SDK classes (`SpineFactory`, `AdaptiveGate`) before public release.
4. Lab validation first: EHT M87* visibilities for BH asymmetry; real DIII-D 157952 OMFIT/Thomson for ELM lead time.

This is the operational blueprint for turning the diagnostic kernel into a deployable Universal Safety Protocol.
