# Coredile playbook

Coredile is a Sri Lankan custom software company ("Your dedicated software team", coredile.com). It has two products:
Coredile POS and Let's Ride. Each product folder has its own `CLAUDE.md`.

## Brand

- Coredile: crocodile logo, deep greens `#0B2A24`, `#0F3D34`, `#2E7D66`; bright green `#4ADE80` only on dark surfaces;
  page background `#F5F8F5`; typeface **Jost**. Look: like Apple, modern, simple, clean, calm.
- Only PNG logos exist; there is no vector logo yet.
- Built in Sri Lanka: 8 years, 80+ projects (used on deck endings).

## Finished files vs sources

- Finished files only (MP4, PNG, PPTX, PDF) go in the finished folders: `Videos/`, `Banners/`, `Sales presentations/`,
  `Product guides/`, `Social posts/`, `Social Media Marketing/`. "I need the MP4 file only, no other thing."
- Sources (Remotion, Astro, scripts, renders, scratch) stay in `Source code/`, `Website/`, `Video studio/`.
- Naming: `<Product> - <title> (wide|tall).mp4`, decks `<Product> - <Industry> (<Language>).pptx`. Folders stay flat.

## Writing

See `../CLAUDE.md` "Writing must sound human". For Sri Lankan owners: "you" to the owner, Rs., local detail
(power cuts, the morning bake, cash-up at closing). Keep every website word in locale files (Sinhala and Tamil come later).

## Content automation (`Content automation/`)

Writes, publishes and shares a coredile.com article four mornings a week on GitHub Actions
(repo `Coredile-com/content-automation`). **It must stay fully unattended**: no Slack interviews, no approval steps. I rejected
human-in-the-loop designs; don't propose them again. It stays honest instead: only facts from the site's own files, parks
topics that need a client's OK or legal review, and marks articles `review: automated` so the page says nobody reviewed them.
Notifications (Slack / WhatsApp) are one-way. Let's Ride (letsride.lk) is to be added later; its schema needs `reviewedBy`
when `aiAssisted`, so keep any disclosure truthful there too.
To go live it needs these GitHub secrets: `ANTHROPIC_API_KEY`, `COREDILE_REPO_TOKEN`, and optionally the Meta and notify keys (README).

## Article style for coredile.com

The skill `Coredile website/.claude/skills/coredile-articles` (in the website repo) is the rulebook, with the topic map.

## Sales decks and printed documents (method used for Coredile POS and ToBeShore FSM)

1. Design the deck as a Slides artifact on claude.ai (HTML, Jost, real screens, speaker notes).
2. Make the .pptx by rendering each slide in Playwright and rebuilding it with pptxgenjs (editable text). No LibreOffice.
   The converter lived in a session scratchpad, so rebuild it when needed.
3. Printed guides and brochures are fixed A4 pages: full-page dark-green cover (logo, pill, big headline, real screen, key
   figures, contacts), one section per page that feels full, full-page bright-green ending (book a demo, contacts, how we
   start, "Built in Sri Lanka"). No box-shadows in print (Chrome turns them into dark blocks).
4. Look at every slide and page as an image before handing over.
5. The decks use Jost and Noto Sans Sinhala; another computer needs those fonts installed.
