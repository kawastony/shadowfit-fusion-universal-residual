# Domain Configurations — Magnificent Eight

All use the same kernel: $R_u = (obs - spine)/\sigma$, 5-pt median sieve, amp + $\sigma$ gate.

## 1. Black Hole
- Spine: $3M$ photon sphere, floor $b_c/M \ge 5.196$
- Rupture: $b=3.265 \to a\approx 0.79195$ (Bardeen verified)
- Gate: 0.3
- Notes: Template-free spin via equatorial asymmetry $\Delta b$. Static SS Schwarzschild-exterior ruled out below floor.

## 2. Fusion (Tokamak)
- Spine: Solov'ev + tanh pedestal ($\psi_{ped}=0.875$, width=0.01)
- Rupture: ELM crash
- Gate: 0.4 (tuned 7$\sigma$ + median + amp)
- Notes: Global poly fails (R2~0.065); tanh solves (R2=0.9942). $S_{ELM} = d/dt[A_{ped}/width \cdot (1-\psi_{ped})]$.

## 3. Market
- Spine: 50-pt efficient median
- Rupture: Flash crash -10%
- Gate: 2.0

## 4. Protein
- Spine: Folding funnel
- Rupture: Misfold to toxic basin
- Gate: 1.5

## 5. Horse Racing
- Spine: 10-race true form
- Rupture: Hidden injury sustained
- Gate: 3.0

## 6. NRL
- Spine: 15-min PER baseline
- Rupture: Fatigue / non-contact injury precursor
- Gate: 4.0

## 7. Network
- Spine: 100 Mbps heartbeat
- Rupture: DDoS sustained collapse
- Gate: 4.0

## 8. Climate
- Spine: Holocene AMOC 15 Sv + 0°C
- Rupture: AMOC collapse -8 Sv sustained
- Gate: 4.5 (fat tails / weather noise)
- Notes: Coupled to temperature anomaly; median kills ENSO/volcano transients.

Stress tests (gas puff, glitch, 20% junk, edge artifacts) passed with final gate: 7$\sigma$ + 5-pt median + amplitude threshold. Transients suppressed, sustained ruptures kept.
