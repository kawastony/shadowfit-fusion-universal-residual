# Shadowfit-Fusion-Universal-Residual

Universal Geometric Residual $\mathcal{R}_u$ diagnostic kernel: one engine for detecting structural rupture across domains.

## Core Idea
$R_u = (\mathrm{obs} - \mathrm{spine}) / \sigma_\mathrm{healthy}$

5-pt median filter = Information Sieve (kills transient noise/glitches/gas puffs).  
Amp + $\sigma$ gate = rupture detector (keeps sustained structural failure).

## Magnificent Eight Domains
| # | Domain | Spine | Rupture example | Gate |
|---|--------|-------|-----------------|------|
| 1 | Black Hole | 3M photon sphere, floor 5.196 | $b=3.265 \to a\approx0.792$ | 0.3 |
| 2 | Fusion | Solov'ev + tanh pedestal | ELM crash | 0.4 |
| 3 | Market | 50-pt efficient median | Flash crash -10% | 2.0 |
| 4 | Protein | Folding funnel | Misfold to toxic basin | 1.5 |
| 5 | Horse racing | 10-race true form | Hidden injury | 3.0 |
| 6 | NRL | 15-min PER baseline | Fatigue / non-contact injury | 4.0 |
| 7 | Network | 100 Mbps heartbeat | DDoS sustained | 4.0 |
| 8 | Climate | Holocene AMOC 15 Sv | AMOC collapse | 4.5 |

See `src/universal_rupture_detector.py` for the immutable 5-line core and `notes/domain_configs.md`.

## Lab Track
- Fusion: pedestal inversion / $S_\mathrm{ELM}$ predictor (tanh R2=0.9942 vs global poly fail).
- BH: template-free spin from equatorial asymmetry (Bardeen verified $a=0.79195 \to b_c=3.265$).

## App / SDK Path
See `notes/sdk_and_platform_evolution.md` for structuring into a professional library (SpineFactory, AdaptiveGate, DomainRegistry, data sanitizers, closed-loop ideas) and deployment instructions.

Status: research kernel + stress-tested gates. Ready for packaging and domain-selector app.
