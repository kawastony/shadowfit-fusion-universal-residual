# Stress Tests & Final Tuned Gate

**Final gate**: 7$\sigma$ + 5-pt median + amplitude threshold (0.4 for fusion ELM).

## Fusion ELM
- Healthy: no alarm
- Gas puff 30%, impurity width 2x, glitch 100% spike: suppressed after median
- Real ELM 80% collapse: alarm (max_filt ~0.45 > 0.4 and >7$\sigma$)
- 20% junk: robust

## Black Hole
- Valid Kerr dirty data: median |R_u| ~0.045 < threshold → heartbeat
- Invalid static: median ~-0.34 > threshold → tumor
- 20% outliers + blur survived

## Zero-shot
Same engine on sine-wave / new systems: heartbeat vs step tumor correctly flagged.

Persistence alone insufficient for single-step ELM gradient; amplitude separates sustained rupture from filtered transients.

All eight domains PASS with domain-specific gates. Weather/fat tails require slightly higher gate (climate 4.5).
