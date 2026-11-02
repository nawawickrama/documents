# Documents: map of everything

Start here. Each folder below has its own `README.md` that says what is in it and how it is made.

```
Documents/
  Coredile/                 Main brand. Everything we build and market for ourselves.
    Coredile website/         coredile.com (Astro)
    Coredile POS/             The POS product: source code, website, videos, sales material
    Let's Ride/               The Sri Lankan trip-bidding app: source code, brand, videos, banners
    Content automation/       Writes and posts coredile.com articles (runs on GitHub Actions)
    Social Media Marketing/   Coredile brand campaigns (finished creatives)
  ToBeShore FSM/            EMPLOYER project. Not a Coredile brand. Keep it separate.
  YouTube/                  Terrachart data-video channel (studio, content plan, brand)
  CV/                       Personal
```

## Rules for every Cowork account

1. **Finished files and sources live together per project.** Finished MP4s, PNGs, PDFs and decks go in the project's
   finished folders (`Videos`, `Banners`, `Product guides`...). Editable sources (Remotion, Astro, code) go in
   `Source code`, `Website` or `Video studio`.
2. **Only finished files** go in `Videos`, `Banners` and similar folders. No scratch files.
3. **ToBeShore FSM is my employer's work.** Never mix its files, logos or code into Coredile or Let's Ride.
4. **Nothing customer-facing is sent or posted without my approval.** Drafting is fine. Exception: `Coredile/Content automation`
   is meant to run fully unattended (see `Coredile/CLAUDE.md`).
5. **Read the playbooks first**: `CLAUDE.md` here, then the `CLAUDE.md` of the folder you work in. They hold the patterns
   (brand, voice, video and social style, do's and don'ts) so any Cowork account or computer can carry on.
6. Do not put API keys or `.env` files in documents or chat. They stay in each project's own secrets.

## How the repeatable work is done

| Job | Where | How |
|---|---|---|
| Animated promo videos (wide 1920x1080 + tall 1080x1920) | each product's `Video studio/` | Remotion. See its README. `npm run voice`, then `npm run render:<name>` |
| Square / social banners | `Coredile/Let's Ride/Video studio/src/banners/` | Remotion still: `npx remotion still BannerSquare out/banners/<name>.png`, then copy to `Let's Ride/Social Media Marketing/Banners/` |
| Website articles | `Coredile/Content automation/` | Four mornings a week on GitHub Actions. See its README |
| Sales decks and brochures | `Coredile POS/Sales presentations`, `ToBeShore FSM/Sales material source` | Built from code, exported to `.pptx` / `.pdf` |

## Where the code lives on GitHub

| Folder | Remote |
|---|---|
| Coredile/Coredile website | `Coredile-com/website` |
| Coredile/Coredile POS/Source code | `Coredile-com/pos` |
| Coredile/Let's Ride/Source code/{backend,frontend,admin,landing,mobile} | `Let-s-Ride/<same name>` |
| Coredile/Content automation | `Coredile-com/content-automation` |
| Coredile/Coredile POS/Website | `Coredile-com/pos-website` |
| Coredile/Coredile POS/Video studio | `Coredile-com/pos-videos-` (name has a trailing hyphen) |
| Coredile/Let's Ride/Video studio | `Let-s-Ride/video-studio` |
| YouTube/Studio | `nawawickrama/terrachart-studio` (music beds not in git; rebuild with `scripts/music.py`) |
| ToBeShore FSM/Websites/tobeshore | Azure DevOps (ToBeShore's own) |

**Not in git yet:** the ToBeShore FSM `Video studio` and `Sales material source` (employer work, kept out
of personal GitHub). Keep `node_modules`, `out/` and finished videos out of git.

## Setting up a new computer

1. Clone the Documents repo into `~/Documents` (playbooks, READMEs, brand files, decks, PDFs, banners), then clone each code
   repo from the table above into its folder (for example `Coredile-com/pos` into `Coredile/Coredile POS/Source code`).
   Videos are not in git: re-render them in the matching `Video studio` (YouTube ones are on the channel).
   ToBeShore FSM is not in git: copy it over by hand.
2. `node_modules` is not backed up: run `npm install` (or `pnpm install` for the POS) in each project before using it.
3. YouTube music beds are not in git: rebuild with `YouTube/Studio/scripts/music.py`.
4. Recreate the YouTube rules shortcut (see `YouTube/CLAUDE.md`).
5. Install the fonts Jost and Noto Sans Sinhala for the sales decks.

## Moved on 3 Nov 2026

Everything used to be spread across `~/Desktop/Developments`, `~/Desktop` and `~/Documents`. Old paths to know:
`Desktop/Developments/<project>` is now under `Documents/Coredile/...` or `Documents/ToBeShore FSM/...`.
Other projects on the Desktop (`Developments/` cancertalk, edge, hq, ias, IAS Hub, optema, restro, weftlyn, premiumfitness,
dsrentacar, do_frontend_web, and `Desktop/Optema`) were not moved.
