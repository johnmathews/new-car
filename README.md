# Family Car Project 2026

Replacing our 2017 Citroën Grand C4 Picasso (174,000 km) with a used electric vehicle. Budget: ~€27,000. Location: Spaarndam, Noord-Holland, Netherlands.

## Shortlist

1. **Hyundai Ioniq 5** (Lounge/Ultimate) — #1 pick. Best all-round package. Predictive ACC (NSCC), blind spot, and electric tailgate standard on all trims. 800V fast charging. Best panoramic roof of the three.
2. **Kia EV6** (GT-Line) — #2 pick. Most features standard (12/16 wishlist items on GT-Line). Predictive ACC (NSCC-C), best audio (Meridian). Stretches budget.
3. **Skoda Enyaq iV** (Edition/L&K) — #3 pick. Biggest boot (585 L), best value. Predictive ACC (pACC) and blind spot require separate option packages. Test driven 1 April 2026.

## Key files

| File | Description |
|------|-------------|
| `Family_Car_Report_2026.pdf` | Full PDF report — overview, specs, feature matrix, safety, costs, recommendations |
| `Family_Car_Project_2026.xlsx` | 7-tab spreadsheet — features, trims, costs, shortlist, charging, timeline |
| `generate_report.py` | Python script (reportlab) that generates the PDF report |

## Working docs

Research notes and deep dives live in `working-docs/`. The main ones:

| File | What it covers |
|------|---------------|
| `recommendations.md` | Overall ranking and reasoning |
| `feature-comparison.md` | 16-item wishlist matrix, scorecard, predictive ACC details |
| `pre-purchase-checklist.md` | What to check when viewing a car — battery, features, Enyaq packages |
| `trim-guide.md` | Which trim to look for per car, quick comparison table |
| `ioniq-5.md` | Ioniq 5 deep dive — specs, trims, NSCC, panoramic roof |
| `ev6.md` | EV6 deep dive — specs, trims, NSCC-C, audio |
| `enyaq.md` | Enyaq deep dive — specs, trims, pACC, three option packages |
| `financial-comparison.md` | TCO analysis — EV saves ~€5,100 over 5 years vs Picasso |
| `charging-infrastructure.md` | Home charging, public network, road trip planning |
| `model-year-guide.md` | Pre-facelift vs facelift differences for all three cars |
| `selling-the-picasso.md` | Notes on selling the current car |

Additional research on cars not in the final shortlist: `extended-shortlist.md`, `vw-id4.md`, `tesla-model-y.md`, `nissan-ariya.md`, `renault-scenic-e-tech.md`, `skoda-elroq.md`, `kia-ev9.md`, `volvo-ex60.md`.

## Feature priorities (top 6)

1. Predictive ACC (nav-based) — NSCC / NSCC-C / pACC
2. Blind spot detection
3. Traffic sign recognition
4. Panoramic sunroof
5. Reversing / 360° camera
6. Park assist (auto steering) — SPA / Parking Plus

## Key insight — Enyaq option packages

On a pre-2025 Enyaq, three separate packages are needed for full ADAS coverage:

- **Assisted Drive** — pACC + blind spot detection + Traffic Jam Assist
- **Side Assist** — blind spot mirror indicators + rear cross-traffic alert + exit warning
- **Parking Plus** — Park Assist + 360° camera + Trained Parking

Business Edition models often have all three. The 2025 facelift made Side Assist and pACC standard, but Park Assist is still optional.

## Status

- [x] Initial research and shortlisting
- [x] Feature comparison and scoring
- [x] Financial analysis (TCO)
- [x] Enyaq test drive (1 April 2026)
- [ ] Ioniq 5 test drive
- [ ] EV6 test drive
- [ ] Find specific listings on Marktplaats / AutoScout24
- [ ] View and purchase
