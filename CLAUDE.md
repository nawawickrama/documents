# Documents: start here

Read `README.md` in this folder for the map of every project. Then read the `CLAUDE.md` of the folder you work in:

| Folder | Playbook |
|---|---|
| `Coredile/` | `Coredile/CLAUDE.md` (brand, writing, finished-file rules) |
| `Coredile/Coredile POS/` | `Coredile/Coredile POS/CLAUDE.md` (videos, website, sales decks, POS repo rules) |
| `Coredile/Let's Ride/` | `Coredile/Let's Ride/CLAUDE.md` (business facts, marketing, videos, app code rules) |
| `YouTube/` | `YouTube/CLAUDE.md` (Terrachart channel: how the next video is made and uploaded) |
| `ToBeShore FSM/` | `ToBeShore FSM/CLAUDE.md` (employer work, kept separate) |
| `CV/` | `CV/CLAUDE.md` (career facts) |

These playbooks are the source of truth. Claude's private memories on one Mac are not shared with other accounts or computers,
so anything worth keeping goes into these files, not only into memory.

## Who I am

Ayesh Nawawickrama, Sri Lanka. Co-founder and product engineer at Coredile (a custom software company, coredile.com).
Owner, developer and only designer of Coredile POS and Let's Ride. Software Engineer at ToBeShore (employer).
I work on a Mac and use several Claude / Cowork accounts on the same folders.

## How to work with me

- **Ask short questions.** A decision is one short multiple-choice question with your recommendation first. No long lists of options or "bla bla".
- **Explain in plain words.** Accounting, inventory or architecture ideas: give an everyday example, what each choice means, and your recommended default.
- **Sweat the small details.** Same wording, casing and button sizes across every screen; check at phone width (390 px) and desktop before handing over.
- **Check before handover.** Look at every video frame by frame (and measure the sound), every slide and printed page as an image. I can't review everything myself; whatever you miss goes public.
- **Say what you checked** and what you skipped. Never claim something works if you didn't see it work.
- **Writing must sound human.** Short plain sentences, concrete local detail, British spelling. No em dashes, and none of: seamless, robust, empower, unlock, elevate, streamline, cutting-edge, all-in-one, "take your business to the next level", "whether you're X or Y".
- **Work in place.** Edit the existing folder. No git worktrees, copy folders or `-v2` files. Other chats may be working in the same folder: check `git status` first.
- **Delete by moving to the Trash**, never `rm`.
- **Ask before** posting or sending anything as me (social media, LinkedIn, WhatsApp, email), and before installing system software.
  The one exception is `Coredile/Content automation`, which I want fully unattended (see `Coredile/CLAUDE.md`).
- **Ports 8000 and 5173** belong to other projects on this Mac. Never stop them; use other ports.
- **The Mac sleeps on battery.** For long jobs run them under `caffeinate -dis`.

## Tools on this Mac

- No `gh` CLI. Git pushes go over SSH (`git@github.com:...`).
- No ffmpeg. Remotion bundles its own.
- Videos use Remotion 4.0.535 and the Kokoro voice `af_heart` (kokoro-js, Apache 2.0). Never the macOS `say` voices for anything published (non-commercial licence).
- Music: Pixabay tracks that are NOT "Content ID registered", or our own from `YouTube/Studio/scripts/music.py`.
