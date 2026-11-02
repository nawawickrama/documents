# Coredile POS playbook

Multi-industry, offline-first POS for Sri Lanka (Laravel API, React apps, Electron till for Windows). Launching for
restaurants first, then bakeries, cafés and shops without scales. Fashion, pharmacy and supermarket come later.
Domain: coredilepos.cloud. Headline: **"You sell. Coredile does the rest."**
Coredile WhatsApp Business: **+94 72 282 2060**, on every deck, guide, video ending and PDF.

## The POS code (`Source code/`, repo `Coredile-com/pos`)

- Read `Source code/CLAUDE.md` and `docs/` first; `docs/stages/` holds each stage's plan and progress. That is the record
  of where the build stands, not this file.
- Branches: finished work goes on a branch, then merge into `dev` and push without asking. `dev` → `uat` → `main` is a
  release and happens only when I say so. Ask before force-pushing or rewriting history.
- Commit messages on this repo carry **no Co-Authored-By line**. I am the only author of record.
- Never run `migrate:fresh` or anything destructive without `DB_DATABASE=coredile_test`. Development data lives in `coredile`.
  Pest and e2e both use `coredile_test`, so never run them at the same time.
- Tests: run the tests a change touches while building; full Pest per build step; full e2e (under `caffeinate -dis`) before a stage merges.
- Never verified, so never claim they work: GitHub CI, anything on Windows, a real printer or cash drawer, a real staging server.
- Waiting on me: accountant answers (`docs/tax/sri-lanka.md`), cashier trial, Windows hardware test, Coolify server, code-signing.
- Never claim Coredile files tax with the IRD. Say "ready for your accountant to check and file".

## Website (`Website/`, repo `Coredile-com/pos-website`)

Astro, same look as coredile.com, hosted on my Coolify server. Kept out of the POS repo so a website change never redeploys the POS.
- 14 pages: home, 6 area pages (each feature is a section `#slug` with an animated drawing), 4 industries, pricing, guides, 404.
- Menu: What it does ▾, Who it's for ▾, What it costs, Guides, Book a demo. No "Log in" link.
- Pricing page: short hero, the calculator as the centrepiece. Never show a setup price ("agreed when you join").
- Advertise only what is built. Not yet: fashion, pharmacy, scales, Uber Eats / PickMe, Sinhala / Tamil, "tax-ready", printer brands.
- Let every AI crawler in (turn off Cloudflare's managed robots.txt blocking).
- Claims to confirm before launch: daily backups, the 3-day offline login limit, the 7 a.m. email.

## Videos (`Video studio/`, repo `Coredile-com/pos-videos-`)

I made Claude my social media marketing manager on 31 Oct 2026. The pattern every video follows:
- Motion graphics: cards popping in, wires drawing, text typing, real POS screens in device frames, finger taps.
- Wide 1920×1080 and tall 1080×1920 from one source. All words in the video's `words.json`.
- Voice: Kokoro `af_heart` (smooth, clear female voice), recorded per line with `npm run voice -- <video>`; the animation is
  timed from the voice. Kokoro says "Coredile" right when spelled "Cordile".
- Music: Creative Technology Showreel (Pixabay), started so its beat drops on the logo, ducked under the voice.
  I can't hear audio, so check the mix with `npm run sound`.
- Launch videos need a clear early brand reveal ("Introducing Coredile POS").
- Ending: logo, "You sell. Coredile does the rest.", WhatsApp +94 72 282 2060 (no web address until coredilepos.cloud is live).
- Made so far: one-bill, saturday, meet (introduction), table (one table start to finish). Restaurant owners are the audience.
- Render with `npm run render:<video>`, check frames, then copy only the MP4s to `Videos/`.

## Sales material

Decks (Slides artifacts, copies as .pptx in `Sales presentations/`):
General EN https://claude.ai/artifact/3QRYA4RGwJLcKGu3nQwJZ6 · General SI https://claude.ai/artifact/JJfTibRRNZYstKys9egJcM ·
Restaurant https://claude.ai/artifact/3zanvKTTg6oGKe1bRCUo31 · Bakery https://claude.ai/artifact/8KTV5Zt2fN5sHpvoS39dLa ·
Shop https://claude.ai/artifact/SDFUErPG4a8swaqAV4XA51
Product guides (PDF copies in `Product guides/`): Restaurant https://claude.ai/artifact/SDoUzGrHEG8giPFJEUuPkr ·
Bakery https://claude.ai/artifact/Ez6A4VHGoE7uEmERvp4WbS · Shop https://claude.ai/artifact/Y2P2MrijkiCuBhwbobH2pS
How they are built: `../CLAUDE.md` "Sales decks and printed documents".
