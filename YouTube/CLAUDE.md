# Terrachart (YouTube) playbook

Faceless data channel: rankings, timelines, bar and line chart races, with voiceover and music. Claude is producer and advisor.
Goal: get into the YouTube Partner Program (AdSense) fast. Everything for the channel lives in this folder; working files are allowed here.

## The channel

- **Terrachart**, @terrachart, "The world, charted through time." Google account nawawickrama@gmail.com
  (the browser's default account may be a different one: pick the right one). Name and handle can change only twice per 14 days.
- Colours: navy `#0D1B2A`, teal `#1FB5A3`, amber `#FFB23F`. Font Inter. Logo: teal globe with navy bars and an amber leader bar.
  Brand files and `Channel setup.md` in `Brand/`.
- Audience: **Europe first**, then US / Canada / Australia, never Sri Lanka (ad rates). British spelling on screen.
- Creator lives in Sri Lanka, so the 500-subscriber YPP tier isn't available. **The YPP bar doubles on 1 Feb 2027**
  (8,000 watch hours or 20M Shorts views), so aim to qualify and be reviewed before then.
- Biggest risk: a "reused / inauthentic content" refusal. Long videos with real narrated analysis earn the watch hours;
  Shorts bring subscribers.

## Rules

Load the policy skill in `Guidelines/` (`SKILL.md` and `references/`) for any video work: music, voice / AI disclosure,
data sources, titles, thumbnails, metadata, claims. It was checked against YouTube's pages on 2 Nov 2026; re-check when it's
older than three months. `Guidelines/` is the real folder; on this Mac `~/.claude/skills/youtube-channel-compliance` is a shortcut
to it. On a new computer, recreate that shortcut:
`ln -s ~/Documents/YouTube/Guidelines ~/.claude/skills/youtube-channel-compliance`

## Making the next video

1. **What and when**: `Content plan/Terrachart content plan 2 Nov - 1 Dec 2026.xlsx` (built from `Content plan/source/*.py`,
   needs openpyxl in a venv). In zsh, pass a list of times to `stills.mjs` written out, not as `$T` (zsh doesn't split it). Long videos Mon / Wed 17:00 CET and Sat 15:00 CET; Shorts daily 19:00 CET.
2. **Script**: plan scripts are drafts. Expand to about 1,100 words (8 to 9 minutes) with checked facts, not pauses.
   A line that names a year must show that year on the counter.
3. **Data**: download into `Data/downloaded-<date>/` and cite the source.
4. **Build**: in `Studio/` (Remotion, repo `nawawickrama/terrachart-studio`, see its README). `words.json` per video; voice is
   Kokoro `af_heart` (American woman; I preferred it over the British voices). Music is our own:
   `python3 scripts/music.py <id> <seconds> <tempo> <seed> <semitones>`, a new track per video (the .wav files are not in git).
   From L06 and S12 on, voice .wav files aren't in git either (re-record with `scripts/voice.mjs`).
   `finish.mjs` sets loudness to −14 LUFS. Shared parts in `src/shared` (Race, LineRace, TileMap, Panels, Overlays, Shorts).
5. **Shorts**: keep all text above y=1480 and left of x=930 (YouTube's phone overlay).
6. **Check every video frame by frame** before handover: render stills across the whole timeline (every beat, mid-race, every
   crossing, every card, the end) and check order and numbers match the narration, nothing overlaps or is cut off, captions
   match the voice, loudness is −14 LUFS, names are pronounced right. S01 shipped with broken bars because only the last frame was checked.
7. **Hand over** in `Videos/<id>/`: MP4, thumbnail, captions, `Upload details.md`.

## Uploading (YouTube Studio)

- Scheduling that matches the content plan (date, slot time, title) is pre-approved: upload and click Schedule without asking.
  Ask only when something differs from the plan.
- I pick the file myself when it's over 10 MB (Claude in Chrome only attaches files under 10 MB, so Shorts can be attached directly;
  the browser pane can't use the file picker).
- Schedule: Time zone "(GMT+01:00) Berlin", then date and time. Add six title translations (Languages → Add language).
- End screen: "Import from latest video", then stretch the video slot. Needs a Chrome window about 1280 px wide.
- Focus a Studio field with JavaScript before typing, or keystrokes hit the preview player.
- After a long video goes public: set it as the related video on its Shorts and pin its comment.
  Session-only reminders die when the session ends, so list open follow-ups in `Videos/<id>/Upload details.md`.

## Made so far (as of 4 Nov 2026)

L01 Europe's biggest economies (S01, S02, S05) · L02 minimum wages (S03, S04) · L03 How Poland caught up (S06, S07) ·
L04 life expectancy (S08, S09, public Mon 9 Nov 17:00 CET). L05 working hours (S10, S11, scheduled: L05 public Wed 11 Nov 17:00 CET). L06 electricity prices (S13, S14, scheduled: L06 public Sat 14 Nov 15:00 CET). S12 (Italian house prices) scheduled Fri 13 Nov 19:00 CET.
L08 (Champions League winners) still needs UEFA data and the 2026 winner.
Open follow-ups: L02 related video on S03/S04 and pin comment (after 4 Nov 17:00 CET); L03 on S06/S07 (after 7 Nov 15:00);
L04 on S08/S09 (after 9 Nov 17:00);
L05 on S10/S11 (after 11 Nov 17:00); L06 on S13/S14 (after 14 Nov 15:00); L12 on S12 (after 28 Nov).
