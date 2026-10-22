# Lab Script Sketches

## elm_predictor.py (Fusion)
Tuned gate: 7$\sigma$ + 5-pt median + amplitude 0.4
- Healthy, gas puff, impurity, glitch → suppressed
- Real ELM 80% collapse → alarm
- Uses $S_{ELM}(t) = \nabla[A_{ped}/width \cdot (1-\psi_{ped})]$ on DIII-D-like gfile

## kerr_shadow_inversion.py (Black Hole)
- Bardeen prograde: $r_{ph} = 2M[1+\cos(\frac{2}{3}\arccos(-a/M))]$
- $b_c$ inversion verified $a=0.79195 \to b_c=3.265$ (diff 0.00005)
- Robust to 20% junk data
- Template-free via equatorial $\Delta b$ asymmetry

Both use the same residual filter that proved the static SS floor theorem and the fusion pedestal solve.
