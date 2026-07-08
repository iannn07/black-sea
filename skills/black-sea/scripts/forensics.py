#!/usr/bin/env python3
"""
BLACK SEA — forensics.py
Financial-forensics indicator calculator for the Org & Financial Forensics lane.

Computes, from user-provided figures ONLY (never invented):
  - Beneish M-Score (earnings-manipulation indicator, 8 variables, needs year t and t-1)
  - Altman Z-Score (original, public manufacturer) and Z'' (private / non-manufacturer / EM)
  - Benford's Law first-digit test (chi-square + Nigrini MAD)
  - Core ratios + YoY trend

These are INDICATORS THAT DIRECT COLLECTION, not verdicts. A high M-Score or low Z is a reason to
pull the ledgers, not a finding of fraud. Every output must land in Annex C with its inputs and the
caveat that any estimated input is flagged.

Usage:
    python3 forensics.py input.json
    cat input.json | python3 forensics.py
    python3 forensics.py --demo        # runnable example
    python3 forensics.py --schema      # print the input schema

Pure standard library. No network. No external deps.
"""
import json
import math
import sys

# Emit UTF-8 regardless of the console's default code page (e.g. Windows cp1252),
# so the report's arrows/dashes don't raise UnicodeEncodeError. (Python 3.7+.)
for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8")
    except AttributeError:
        pass

# ----------------------------- Beneish M-Score ------------------------------ #

def beneish(t, p):
    """t = current year dict, p = prior year dict. Returns (M, components, notes)."""
    req = ["receivables", "sales", "cogs", "current_assets", "ppe", "total_assets",
           "depreciation", "sga", "net_income", "cash_from_ops", "current_liab", "ltd"]
    missing = [k for y, d in (("t", t), ("t-1", p)) for k in req if k not in d]
    if missing:
        return None, {}, [f"Beneish skipped — missing inputs: {sorted(set(missing))}"]

    def gm(d):   return (d["sales"] - d["cogs"]) / d["sales"]
    def lev(d):  return (d["ltd"] + d["current_liab"]) / d["total_assets"]
    def aqi_n(d):return 1 - (d["current_assets"] + d["ppe"]) / d["total_assets"]
    def depr(d): return d["depreciation"] / (d["depreciation"] + d["ppe"])

    DSRI = (t["receivables"]/t["sales"]) / (p["receivables"]/p["sales"])
    GMI  = gm(p) / gm(t)
    AQI  = aqi_n(t) / aqi_n(p)
    SGI  = t["sales"] / p["sales"]
    DEPI = depr(p) / depr(t)
    SGAI = (t["sga"]/t["sales"]) / (p["sga"]/p["sales"])
    LVGI = lev(t) / lev(p)
    TATA = (t["net_income"] - t["cash_from_ops"]) / t["total_assets"]

    M = (-4.84 + 0.920*DSRI + 0.528*GMI + 0.404*AQI + 0.892*SGI
         + 0.115*DEPI - 0.172*SGAI + 4.679*TATA - 0.327*LVGI)
    comps = dict(DSRI=DSRI, GMI=GMI, AQI=AQI, SGI=SGI, DEPI=DEPI, SGAI=SGAI, LVGI=LVGI, TATA=TATA)
    verdict = ("ABOVE −1.78 threshold — flags possible manipulation; pull ledgers"
               if M > -1.78 else "below −1.78 — no manipulation signal from this model")
    return M, comps, [f"M = {M:.3f} → {verdict}"]

# ------------------------------- Altman Z ----------------------------------- #

def altman(d):
    out = {}
    if all(k in d for k in ["working_capital","retained_earnings","ebit","total_assets",
                            "mkt_value_equity","total_liabilities","sales"]):
        ta = d["total_assets"]
        Z = (1.2*d["working_capital"]/ta + 1.4*d["retained_earnings"]/ta + 3.3*d["ebit"]/ta
             + 0.6*d["mkt_value_equity"]/d["total_liabilities"] + 1.0*d["sales"]/ta)
        zone = "SAFE" if Z > 2.99 else ("GREY" if Z >= 1.81 else "DISTRESS")
        out["Z (original)"] = (round(Z, 3), f"{zone} (>2.99 safe / 1.81–2.99 grey / <1.81 distress)")
    if all(k in d for k in ["working_capital","retained_earnings","ebit","total_assets",
                            "book_value_equity","total_liabilities"]):
        ta = d["total_assets"]
        Z2 = (3.25 + 6.56*d["working_capital"]/ta + 3.26*d["retained_earnings"]/ta
              + 6.72*d["ebit"]/ta + 1.05*d["book_value_equity"]/d["total_liabilities"])
        zone = "SAFE" if Z2 > 2.6 else ("GREY" if Z2 >= 1.1 else "DISTRESS")
        out["Z'' (private/non-mfg/EM)"] = (round(Z2, 3), f"{zone} (>2.6 safe / 1.1–2.6 grey / <1.1 distress)")
    return out or {"note": ("Altman skipped — need working_capital, retained_earnings, ebit, "
                            "total_assets, total_liabilities and (mkt_value_equity or book_value_equity)")}

# ------------------------------- Benford ------------------------------------ #

def benford(values):
    digits = [int(str(abs(float(v))).lstrip("0.").replace(".", "")[:1])
              for v in values if float(v) != 0 and str(abs(float(v)))[0:1].isdigit()]
    digits = [d for d in digits if 1 <= d <= 9]
    n = len(digits)
    if n < 30:
        return {"note": f"Benford unreliable — only {n} usable values (need a large natural dataset, ~100+)"}
    obs = {d: digits.count(d) for d in range(1, 10)}
    exp = {d: n*math.log10(1 + 1/d) for d in range(1, 10)}
    chi2 = sum((obs[d]-exp[d])**2/exp[d] for d in range(1, 10))
    mad = sum(abs(obs[d]/n - math.log10(1+1/d)) for d in range(1, 10))/9
    if mad < 0.006:   conf = "close conformity"
    elif mad < 0.012: conf = "acceptable conformity"
    elif mad < 0.015: conf = "marginal — worth a second look"
    else:             conf = "NONCONFORMITY — investigate for fabrication/rounding"
    return {"n": n, "chi_square (df=8; crit≈15.51 @0.05)": round(chi2, 2),
            "MAD": round(mad, 5), "assessment": conf,
            "observed_vs_expected_%": {d: (round(100*obs[d]/n, 1), round(100*exp[d]/n, 1)) for d in range(1, 10)}}

# ------------------------------- Ratios ------------------------------------- #

def ratios(d):
    r = {}
    g = d.get
    if g("current_assets") and g("current_liab"): r["current_ratio"] = round(d["current_assets"]/d["current_liab"], 2)
    if g("receivables") and g("sales"):           r["DSO_days"] = round(d["receivables"]/d["sales"]*365, 1)
    if g("sales") and g("cogs"):                  r["gross_margin_%"] = round((d["sales"]-d["cogs"])/d["sales"]*100, 1)
    if g("net_income") and g("sales"):            r["net_margin_%"] = round(d["net_income"]/d["sales"]*100, 1)
    if g("total_liabilities") and g("book_value_equity"): r["debt_to_equity"] = round(d["total_liabilities"]/d["book_value_equity"], 2)
    return r or {"note": "no ratio inputs provided"}

# ------------------------------- Runner ------------------------------------- #

def run(payload):
    print("="*66)
    print("BLACK SEA // FORENSICS — indicators only, not verdicts")
    print("="*66)
    if "beneish" in payload:
        M, comps, notes = beneish(payload["beneish"].get("t", {}), payload["beneish"].get("t_1", {}))
        print("\n[ BENEISH M-SCORE ]")
        for ln in notes: print("  " + ln)
        for k, v in comps.items(): print(f"    {k:5} = {v: .3f}")
    if "altman" in payload:
        print("\n[ ALTMAN Z ]")
        for k, v in altman(payload["altman"]).items():
            print(f"  {k}: {v[0]} — {v[1]}" if isinstance(v, tuple) else f"  {v}")
    if "benford" in payload:
        print("\n[ BENFORD FIRST-DIGIT ]")
        for k, v in benford(payload["benford"]).items(): print(f"  {k}: {v}")
    if "ratios" in payload:
        print("\n[ RATIOS ]")
        for k, v in ratios(payload["ratios"]).items(): print(f"  {k}: {v}")
    print("\n" + "-"*66)
    print("Flag any ESTIMATED input in Annex C. Indicators direct collection; they do not convict.")

DEMO = {
  "beneish": {
    "t":   {"receivables": 118, "sales": 196, "cogs": 150, "current_assets": 160, "ppe": 90,
            "total_assets": 300, "depreciation": 9, "sga": 22, "net_income": 14, "cash_from_ops": 3,
            "current_liab": 70, "ltd": 40},
    "t_1": {"receivables": 45, "sales": 140, "cogs": 104, "current_assets": 120, "ppe": 85,
            "total_assets": 250, "depreciation": 8, "sga": 18, "net_income": 11, "cash_from_ops": 10,
            "current_liab": 55, "ltd": 35}
  },
  "altman": {"working_capital": 90, "retained_earnings": 40, "ebit": 20, "total_assets": 300,
             "book_value_equity": 120, "total_liabilities": 180},
  "ratios": {"current_assets": 160, "current_liab": 70, "receivables": 118, "sales": 196,
             "cogs": 150, "net_income": 14, "total_liabilities": 180, "book_value_equity": 120}
}

if __name__ == "__main__":
    if "--schema" in sys.argv:
        print(json.dumps(DEMO, indent=2)); sys.exit(0)
    if "--demo" in sys.argv:
        run(DEMO); sys.exit(0)
    raw = open(sys.argv[1]).read() if len(sys.argv) > 1 else sys.stdin.read()
    run(json.loads(raw))
