# Let's Ride playbook

## The business (facts to use in every post, video and article)

- A transport bidding marketplace for tourists in Sri Lanka (letsride.lk). Travellers (and hotels / travel agents) post a
  trip, NIC-verified Sri Lankan vehicle owners each place one bid, the traveller picks one, and a private chat opens.
- **Free for travellers and for vehicle owners.** No payments go through the platform, no commission, no booking fee.
  Never hint at future owner fees or pricing changes.
- Company: Let's Ride (Private) Limited. Support: WhatsApp +94 70 118 3325, support@letsride.lk.
- Social: @letsride.lk on Facebook, Instagram, TikTok; also YouTube. Support channels: WhatsApp and in-app chat.
- Words: Let's Ride (never LetsRide), traveller, vehicle owner, "Log in" (not "Sign in"), sentence case, "…".
  In videos for tourists, "Drivers bid" reads clearer than "Owners bid".

## Marketing pitfalls (do not repeat these)

- Sri Lanka has **25** districts (the Play Store listing wrongly says 26).
- There is **no GPS tracking**. Never say "full trip tracking" (the app has ready / trip code / start / end only).
- "Sri Lanka's first" is not verified. Don't use it.
- Bids shown on the homepage and in videos are examples. Mark them "Example".
- Prices in articles: give roughly 10% above what research found, rounded, framed as a budget ("plan on around…").
  Never change a figure that is attributed to a source.

## Brand

Mint road `#05F0B3` on deep green (like the app icon), site green `#17A280`, typeface Manrope.
Logos: `Brand/` (`newlogo/` has black and white logos and icons; `logo.png` and `app_icon.png`).
Colour tokens for code: `Video studio/src/brand.ts`.

## Videos and banners (`Video studio/`, repo `Let-s-Ride/video-studio`)

Same method as the Coredile POS videos (see `../Coredile POS/CLAUDE.md`, "Videos"): Remotion, wide + tall, Kokoro `af_heart`,
timed per voice line, words in `words.json`. `scripts/gaps.mjs` finds pauses so scenes land on the right word.
- Made: "How it works" (53 s): price guesses over a winding road → "Post your trip. Drivers bid. You pick." → example trip →
  three bids → compare → accept and chat → checks on every owner → no booking fee → letsride.lk.
- Square banner 1080×1080: `src/banners/SquareBanner.tsx`, render with `npx remotion still BannerSquare out/banners/<name>.png`.
- Finished files only: `Social Media Marketing/Videos/Let's Ride - <title> (wide|tall).mp4` and `Social Media Marketing/Banners/`.
- The music is the Coredile Pixabay track; a warmer travel track could replace it.

## App code (`Source code/`, repos `Let-s-Ride/<name>`)

- Branch from `dev` for backend, frontend, admin; from **`dev-2`** for mobile. Pull the base first, one feature branch per
  feature, same branch name in each repo for a cross-repo feature. Don't change `landing` as part of app features.
- Pushing: while iterating on tweaks, don't push until I say the round is done. A finished, verified new feature on its own
  branch: commit and push without asking. Never open PRs unasked.
- Redesigns are visual only: keep every existing field and behaviour even if the mockup leaves it out. Replace in place, no `-v2` files.
- Every button is the shared `LrButton` (lg completes a form, md 44 px for the rest, sm for compact rows). Check 1440 and 390 px wide.
- Frontend locally: `docker compose --env-file .env.local up -d --build` in `frontend/` (http://localhost:3000). Never edit
  `.env.local`; read which API it points at (often production) before starting, and intercept `/api` in browser tests.
- Flutter: `flutter test` fails inside this folder because of the apostrophe in "Let's Ride". Run tests from a scratch harness
  package that path-depends on `mobile/`. If Xcode reports "#endif without #if", run `flutter pub get` in `mobile/`.
  After the folder move on 3 Nov 2026, run `flutter pub get` once.
- For small UI changes run only that screen's tests.
- Headless screenshots: use chrome-headless-shell from `~/.cache/puppeteer`, with a timeout.
- Admin "HQ" has a Statistics page (top countries, top routes, bids per trip, time to first bid): good input for marketing.
- The landing site has `docs/seo-roadmap.html` and `docs/keywords-for-volume.txt`; articles go in `src/content/news` and `guides`.
