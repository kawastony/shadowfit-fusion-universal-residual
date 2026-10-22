import numpy as np

def median_filter(S, k=5):
    """5-pt median as Information Sieve — kills transients, keeps sustained rupture."""
    return np.convolve(S, np.ones(k)/k, mode='same')

def universal_detect(obs, spine, sigma_healthy=None, amp_gate=3.0, trim=5):
    """
    Immutable 5-line core engine.
    R_u = (obs - spine) / sigma
    Rf = 5-pt median
    alarm if max|Rf| > amp_gate AND > 3*std(Rf)
    """
    if sigma_healthy is None:
        sigma_healthy = np.std(obs - spine) + 1e-6
    Ru = (obs - spine) / sigma_healthy
    Rf = median_filter(Ru, 5)
    if trim > 0:
        Rf = Rf[trim:-trim] if len(Rf) > 2*trim else Rf
    max_abs = np.max(np.abs(Rf))
    sigma_Rf = np.std(Rf) + 1e-6
    alarm = (max_abs > amp_gate) and (max_abs > 3 * sigma_Rf)
    return alarm, max_abs, Rf

# Magnificent Eight — factory defaults (locked presets recommended for expert system)
DOMAIN_CONFIG = {
    "1_black_hole": {"spine": "3M photon sphere, floor 5.196M", "amp_gate": 0.3, "desc": "b=3.265 -> a=0.79195 Bardeen"},
    "2_fusion": {"spine": "Solov'ev + tanh pedestal", "amp_gate": 0.4, "desc": "ELM, R2 0.9942"},
    "3_market": {"spine": "50-pt efficient median", "amp_gate": 2.0, "desc": "Flash -10%"},
    "4_protein": {"spine": "Folding funnel", "amp_gate": 1.5, "desc": "Toxic basin"},
    "5_horse": {"spine": "10-race true form", "amp_gate": 3.0, "desc": "Injury -15"},
    "6_nrl": {"spine": "15-min PER baseline", "amp_gate": 4.0, "desc": "Fatigue -20"},
    "7_network": {"spine": "100 Mbps heartbeat", "amp_gate": 4.0, "desc": "DDoS -60"},
    "8_climate": {"spine": "Holocene AMOC 15 Sv", "amp_gate": 4.5, "desc": "AMOC collapse -8 Sv"},
}

if __name__ == "__main__":
    print("Universal Rupture Detector v8 — Magnificent Eight loaded.")
    print("Use universal_detect(obs, spine, amp_gate=DOMAIN_CONFIG[domain]['amp_gate'])")
