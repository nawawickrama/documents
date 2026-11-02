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

**1. Install the tools** (versions used on the old Mac):
Xcode and its command line tools · Homebrew · Node 22 · pnpm 12.8.1 · PHP 8.4 + Composer (Laravel Herd gives both) ·
Docker Desktop · Flutter 3.47 · Python 3 · Claude desktop app (Cowork / Claude Code) · fonts Jost and Noto Sans Sinhala (for the decks).

**2. Give the Mac access to GitHub:** make an SSH key (`ssh-keygen -t ed25519`) and add it to your GitHub account
(Settings → SSH and GPG keys). It must reach the `Coredile-com` and `Let-s-Ride` organisations.

**3. Get everything:**
```
git clone git@github.com:nawawickrama/documents.git ~/Documents
bash ~/Documents/setup-new-mac.sh
```
The script clones every code repo into its folder, installs packages, runs `flutter pub get`, and recreates the YouTube rules shortcut.

**4. By hand afterwards:**
- `.env` files are never in git. Copy them from the old Mac (POS `backend/.env`, Let's Ride `frontend/.env.local`, and so on) or rebuild them from each `.env.example`.
- POS databases: start Docker, then follow `Coredile POS/Source code` README (`coredile`, `coredile_test`, the `coredile_platform` role).
- POS browser tests: `pnpm exec playwright install` in `Coredile POS/Source code`.
- YouTube music beds: `python3 scripts/music.py <id> <seconds> …` in `YouTube/Studio` (needs numpy).
- The Kokoro voice model downloads on the first `npm run voice`.
- Videos are not in git: re-render in the matching `Video studio` when needed. YouTube ones are on the channel.
- ToBeShore FSM is not in git: copy that folder over by hand (USB drive or AirDrop).
- Sign in to the Claude desktop app, open `~/Documents` as the folder, and it will read `CLAUDE.md`.

## Moved on 3 Nov 2026

Everything used to be spread across `~/Desktop/Developments`, `~/Desktop` and `~/Documents`. Old paths to know:
`Desktop/Developments/<project>` is now under `Documents/Coredile/...` or `Documents/ToBeShore FSM/...`.
Other projects on the Desktop (`Developments/` cancertalk, edge, hq, ias, IAS Hub, optema, restro, weftlyn, premiumfitness,
dsrentacar, do_frontend_web, and `Desktop/Optema`) were not moved.
