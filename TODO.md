# Anxiety Garden — To-Do

_Reconciled against actual code/repo state (the old date stamps were unreliable — anchor to git + what the files actually do). **Note:** the second build agent crashed mid-run, so a few of its in-flight items are now orphaned back to "open" (see 🔁)._

## 🔴 Needs Lisa (decisions / clinical / design)
- [ ] **Sensation→garden-place map** (§6) — the cast's place-glows are **placeholder** in `garden.html`'s `CAST.place` config until this lands (the scene has no greenhouse/gate/canopy layers, so it's a positional overlay, not real geography).
- [x] **SIGNATURE map** in `sundial.html` — **confirmed by Lisa**: anger=hot/tight · fear=cold/racing/tight · disgust=queasy/tight · sadness=heavy/numb · joy=light/buzzy · surprise=jolt/racing. No changes needed.
- [x] **6 weather colours** — confirmed by Lisa (fine as-is): anger `#e0432a` · joy `#e7b91f` · disgust `#2d9846` · sadness `#2f63b3` · fear `#5b4a9e` · surprise `#cc3f86`.
- [x] **Sundial — done for now.** Ambient = Lisa's gnomon disc (`sun-dial-face.png`) → tap → clean 6-colour reading wheel → pick → stone gnomon swings, shadow falls, others fade, weather casts over the garden. Works end-to-end.
  - _Optional future polish (NOT needed):_ a faceted, flat, head-on 6-disc to make the engaged reading face match the painted disc's craft. The code-drawn reading wheel is clean and clear as-is (clarity suits the "name what you feel" moment). Only do this if Lisa wants it.
- [ ] **Body figure** in the drill-down — keep & soften / calmer outline / drop and use words.
- [ ] **Redeploy in Coolify** to see the latest — push doesn't auto-deploy.

## 🟠 Open — my lane (garden), no Lisa needed
- [ ] **Perspective modes** (MODEL §7) — _partly done:_ ✅ drifting clouds in the outside cast (`408ec01`); ✅ **shed rain-on-glass** "step into the shed" view, rain/storm only (`f53302e`). _Remaining:_ **fog/haze "panes fog up"** shelter treatment (fog = can't-see, not rain-on-glass); **outside "layered depth"** iOS-style near/far rain polish.
- [ ] **Action screens** (blooms / weeds / bucket) with **first-person hands + skin-tone picker** — `hands-picker.html` prototype exists (CSS-filter recolour + `localStorage`); `hands-web.png` is prepped. Skin = a recolour layer, everything else fixed. ← _in progress_
- [ ] Optional: cast weather *behind the dial on screen 6* too (currently casts on the screen-1 scene).

## 🔁 Orphaned by the crash — now nobody's unless I take them
- [x] **Alarm: bigger + visibly ringing** — `alarm-alert.png` (octagon + yellow rays) added as a scene-SVG layer (`#alarmringing`), revealed on `svg.storm`, hidden in calm. Bigger + clearly ringing when tripped. ⚠️ **Caveat:** the alarm assets were *not* soloed-in-position (the alarm is drawn mid-canvas, not at the scene's bottom-left), so it's placed via a viewBox `transform` workaround — works + resolution-independent, but **the clean fix is for Lisa to re-export `alarm-calm`/`alarm-alert` soloed at the scene position** (per the PLAN.md export recipe), then it drops in 1:1 without the transform. "Bigger in *calm*" still needs her scene redraw (octagon is baked small into `calmstate.png`).
- [ ] **Downsize the 3 orphaned 160 MP exports** (`alarm.png`, `buckets-together.png`, `seedshed.png`) to ≤1800px (mobile rule); keep originals aside. (`inside-shed-web.png` already done.)
- [ ] **`garden-api/`** — usable FastAPI scaffold sitting **uncommitted** (the gate's future `/auth` + check-in backend + Lisa's learning project). Clean 13-file add (no venv/idea/pyc). Decide: commit or leave.

## 🔗 Intensity handshake (was the dial's half — also orphaned)
- [ ] **Dial sends `detail.intensity` (0–1)** on `sundial:select`. The garden's `cast()` **already reads it** (defaults 0.5), so until the dial sends it, every weather renders mid-intensity (worry-mist vs panic-fog look the same). Source it from the dial's radius (mild→intense, MODEL §2) and/or the coarse read.

## 🟢 Seeking & Care homes (off the wheel — conceptual/art)
- [ ] **Seeking = the sun** — the always-there light/drive that casts the shadow (present in the whole instrument, not a slice).
- [ ] **Care = the nurturing pour + a between-gardens beat** — the watering can as nurture; relational warmth across the fence.

## ✅ Done (verified in code)
- **Perspective:** **drifting clouds** layer in the cast (sun 2 / rain 4 / fog 2 / storm 4 dark / haze none; reduced-motion-safe); **shed rain-on-glass** view — "step into the shed" from a rain/storm cast → sheltered rain-on-glass over `inside-shed-web.png`, loops torn down on close, reduced-motion = static drops.
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
