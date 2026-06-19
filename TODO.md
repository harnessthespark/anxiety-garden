# Anxiety Garden — To-Do

_Reconciled against actual code/repo state (the old date stamps were unreliable — anchor to git + what the files actually do). **Note:** the second build agent crashed mid-run, so a few of its in-flight items are now orphaned back to "open" (see 🔁)._

## 🔴 Needs Lisa (decisions / clinical / design)
- [ ] **Sensation→garden-place map** (§6) — the cast's place-glows are **placeholder** in `garden.html`'s `CAST.place` config until this lands (the scene has no greenhouse/gate/canopy layers, so it's a positional overlay, not real geography).
- [ ] **Redline the `SIGNATURE` map** in `sundial.html` — which body qualities point to which feeling (fear = cold/racing/tight, anger = hot/tight, etc.). The body-first narrow's accuracy rides on this. Also `REGIONS` / `QUALITIES` wording.
- [ ] **Confirm the 6 weather colours** — anger red · joy amber · disgust green · sadness blue · fear purple · surprise pink.
- [ ] **Flat 6-disc art** — faceted top-down 6-segment disc matching the tilted one (or I warm the code wheel as interim).
- [ ] **Body figure** in the drill-down — keep & soften / calmer outline / drop and use words.
- [ ] **Redeploy in Coolify** to see the latest — push doesn't auto-deploy.

## 🟠 Open — my lane (garden), no Lisa needed
- [ ] **Perspective modes** (the big new direction, MODEL §7): *outside* = iOS-Weather-style layered falling rain + drifting clouds over the scene; *inside the shed* (`inside-shed.png`) = **rain-on-glass** (rivulets, blurred garden) — the "step into the shed = take perspective" regulation move. Prototype: `rain-shed.html`. Rules: positive weather stays outside; hard weather is a *choice* to tend-through or shelter; never all-in-the-shed.
- [ ] **Drifting clouds** layer in the cast (slow, soft, "alive") — wanted in both perspective modes.
- [ ] **Action screens** (blooms / weeds / bucket) with **first-person hands + skin-tone picker** — `hands-picker.html` prototype exists (CSS-filter recolour + `localStorage`); `hands-web.png` is prepped. Skin = a recolour layer, everything else fixed.
- [ ] Optional: cast weather *behind the dial on screen 6* too (currently casts on the screen-1 scene).

## 🔁 Orphaned by the crash — now nobody's unless I take them
- [ ] **Alarm: bigger + visibly ringing** — was handed to the (now-crashed) second agent. The small octagon is baked into the scene rasters; the cleanest fix is lifting it to a scriptable overlay (`alarm-calm.png` / `alarm-alert.png`) so it's big, tappable, and rings on storm. `alarm.png` is candidate art (160 MP, unwired).
- [ ] **Downsize the 3 orphaned 160 MP exports** (`alarm.png`, `buckets-together.png`, `seedshed.png`) to ≤1800px (mobile rule); keep originals aside. (`inside-shed-web.png` already done.)
- [ ] **`garden-api/`** — usable FastAPI scaffold sitting **uncommitted** (the gate's future `/auth` + check-in backend + Lisa's learning project). Clean 13-file add (no venv/idea/pyc). Decide: commit or leave.

## 🔗 Intensity handshake (was the dial's half — also orphaned)
- [ ] **Dial sends `detail.intensity` (0–1)** on `sundial:select`. The garden's `cast()` **already reads it** (defaults 0.5), so until the dial sends it, every weather renders mid-intensity (worry-mist vs panic-fog look the same). Source it from the dial's radius (mild→intense, MODEL §2) and/or the coarse read.

## 🟢 Seeking & Care homes (off the wheel — conceptual/art)
- [ ] **Seeking = the sun** — the always-there light/drive that casts the shadow (present in the whole instrument, not a slice).
- [ ] **Care = the nurturing pour + a between-gardens beat** — the watering can as nurture; relational warmth across the fence.

## ✅ Done (verified in code)
- **Cast lane:** 6 weathers; **rain "fireworks" fixed** (pixel-distance fall, not `translateY(%)`); contrast sweep over the bright scene; **haze** (disgust, yellow/humid, distinct from fear's grey fog); **intensity scaling** via `--i`; **climate (Seeking/Care) retired** — six weathers only. Surprise fork = renderers only (`flash`/`sunbreak`/`hail`); the **dial owns the appraisal**.
- **Sundial walk complete** — notice → narrow → pick → read → tell-apart → express (+ surprise fork). _(Per the crashed agent's report — worth a quick re-verify.)_
- **Scenes reworked** to `calmstate.png` / `negativestate.png` (1801×900, aligned, mobile-safe; old `calm-garden`/`anxiety-garden` removed). Alarm trip cross-fades cleanly.
- **Bear** fixed — `#bearArt` is now just `bear-trim.png` in the markup (no brown stand-in flash); `ensureBear()` is a no-op.
- **Entry gate** — soft client-side access gate (committed). To be pointed at `garden-api`'s real `/auth` later.
- Sundial embedded in garden screen 6 as "today's weather" + verified postMessage cast bridge.
- 6-segment weather wheel (Seeking & Care taken off); body-first walk keystone (notice → narrow).
- Cosmetic: removed stray "0" rim markers + blue focus box. Docker deploy on Coolify; lean repo (394 MB → 21 MB).

## 🗒️ Notes
- **Two-session history:** sundial/MODEL/scenes/gate were built by a second agent (transcript exported to `~/Desktop/other-agent-chat-garden.md`); that session crashed. Cast lane + bear fix + this reconcile by the current session.
- **Mobile rule:** keep image exports ≤ ~1800px — bigger ones (8514–17067px) blanked mobile Safari (decode-RAM blowout). Pixel dimensions matter as much as file size.
