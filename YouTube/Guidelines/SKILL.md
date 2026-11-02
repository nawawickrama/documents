---
name: youtube-channel-compliance
description: Keeps every YouTube video and Short we make inside YouTube's and Google's rules, so the channel gets into the YouTube Partner Program (AdSense) and stays there. Covers monetisation eligibility, the inauthentic and reused content policies, background music and sound licensing, AI voiceovers and AI disclosure, data sources and citations, images, logos, flags and fonts, titles, thumbnails, descriptions and tags, made-for-kids, advertiser-friendly topics, Content ID claims and strikes, and AdSense payments and tax. Use this skill whenever we plan, script, produce, edit, render, title, thumbnail or upload a YouTube video or Short (rankings, timelines, bar chart races, data videos, voiceovers), pick music, a voice or a data source, or talk about YPP, AdSense, monetisation, copyright or a claim, even if the user does not mention policy.
---

# YouTube channel compliance

We are building a faceless data channel (rankings, timelines, bar chart races, Shorts) with voiceover and background music, and the goal is to get into the YouTube Partner Program and earn from AdSense. A channel like this rarely fails because of one bad video. It fails at review time, when a person at YouTube looks at the whole channel and decides it is "mass-produced" or "reused". It can also fail because a music track or a data source turns out not to be licensed for money-making use. This skill exists to stop both.

The user is the owner. Claude is the producer and the advisor. When something we want to do breaks a rule here, say so plainly before doing it, explain the risk in one or two sentences, and offer the nearest safe alternative.

## The channel's situation (affects which rules apply)

- **The channel is Terrachart** (@terrachart). Everything for the channel lives in `~/Documents/YouTube/`: `Brand/` (logo, banner, colours, About text, upload defaults), `Videos/` (finished videos), and `Guidelines/` (a link to this skill, so the owner can read it). Save new work there.
- **We make videos for viewers in Europe first, then the US, Canada and Australia, not Sri Lanka**, because ad rates follow the viewer's country. English for second-language speakers, British spelling, metric units, euros, publishing at 16:00–18:00 CET. The channel's "country of residence" still stays Sri Lanka. Read `references/audience-europe.md` before planning topics, titles or promotion.
- **The creator lives in Sri Lanka.** YPP is available there, but the lower "expanded" tier (500 subscribers, fan funding) is **not**. The only way in is the full tier: 1,000 subscribers plus watch hours or Shorts views.
- **The bar to join doubles on 1 February 2027.** Until then: 1,000 subscribers and either 4,000 public watch hours in 12 months (long-form only) or 10 million Shorts views in 90 days. From 1 Feb 2027 for new applicants: 8,000 hours or 20 million Shorts views. Channels already in YPP keep their place. YouTube has not said how applications still under review on that date are treated, and review takes about a month.
- **From 1 Feb 2027 Shorts only pay a channel that keeps 10 million Shorts views every 90 days**, even after joining. Below that, Shorts earn nothing and long-form still earns.
- **Shorts pay very little.** Shorts earn roughly 3 to 14 percent of what long-form earns per 1,000 views (about US$0.03 to $0.20 per 1,000). Use Shorts to win subscribers and point them at long-form; plan the money around long-form.

Details, sources and the money arithmetic are in `references/monetization-and-ypp.md`.

## Six rules that are easiest to break

1. **Every video needs our own insight, not just a moving chart.** A bar chart race with music and no explanation is the textbook example of "inauthentic content" (templated, repetitive, low educational value). Each video needs a script that tells the viewer *why* the numbers move, written for that video. Read `references/originality-for-data-videos.md` before planning a series.
2. **Music comes only from a source we can prove we licensed for monetised YouTube use.** Default to the YouTube Audio Library. Never a commercial song, never "no copyright music" from a random channel, never a track with a NonCommercial licence. Read `references/music-and-audio.md`.
3. **Every asset gets a line in the licence log** at the moment we use it (music, voice, data, images, fonts). If a claim arrives in six months, the log is our proof. Template: `assets/licence-log.csv`.
4. **Every number has a source we are allowed to use, and the source is named** in the video and the description. Read `references/data-and-visuals.md`.
5. **Titles and thumbnails must match the video.** A thumbnail promising something the video does not show is "misleading metadata" under the spam policy, and it is checked at review. Read `references/metadata-and-community.md`.
6. **Never buy views, subscribers, likes or "promotion" packages, and never join sub-for-sub.** It breaks the fake engagement policy and it is one of the reasons channels are refused or removed.

## When we plan a video

Check these before writing the script:

- **Topic.** Is it advertiser-friendly? Data about wars, deaths, disasters, crime, suicide, drugs or tragedies usually gets limited ads, and content that profits from a recent tragedy gets none. We can still make it, but know the cost. See `references/metadata-and-community.md`.
- **Angle.** What does this video tell the viewer that the raw chart does not? If we cannot say it in one sentence, the video is not ready.
- **Data.** Which source, what licence, what year, any gaps or estimates the narration must mention.
- **Format.** Is this the fourth near-identical video this week? Vary format, length and structure across the channel.
- **Audience.** Not made for kids. Data and rankings for a general audience are "No, not made for kids", even with cartoon styling, unless they are clearly aimed at children.

## When we produce a video

- **Script:** written for this video, with analysis, context and a point of view. AI can help draft; the final words must carry our own insight. Do not read out Wikipedia or a news article. See `references/originality-for-data-videos.md`.
- **Voice:** a text-to-speech voice is fine if the plan we generate it on allows commercial use (ElevenLabs' free plan does not). Never clone or imitate a real person's voice. Do not present an AI narrator as a human expert giving financial, medical, legal or political advice; that alone makes a channel ineligible. See `references/voice-and-ai.md`.
- **Music:** YouTube Audio Library first. If the track says "Attribution required", copy its credit line into the description. Keep music under the voice, and vary tracks between videos. See `references/music-and-audio.md`.
- **Visuals:** flags, our own shapes, our own charts, Google Fonts or other fonts licensed for video. Photos and logos only with a licence we can show. See `references/data-and-visuals.md`.

## Before every upload (the checklist)

Run through this and tell the user if any line fails. Do not upload around a failure.

- [ ] The script explains the data; it is not only a chart with music.
- [ ] This video is meaningfully different from the last few (format, topic, structure).
- [ ] Every music track, sound effect, voice and image is in the licence log with its proof.
- [ ] Attribution lines that a licence requires are in the description.
- [ ] Data sources are named on screen and in the description, with the year.
- [ ] Numbers are checked against the source; estimates and projections are labelled as such.
- [ ] The title and thumbnail show what the video actually shows. No strong profanity, no shocking or sexual imagery in either.
- [ ] Tags and description are relevant; no lists of unrelated keywords.
- [ ] "Made for kids" is set correctly (normally No).
- [ ] Written for Europe: British English, metric, euros where it fits; captions checked; title and description translations added; scheduled for 16:00–18:00 CET.
- [ ] "Altered or synthetic content" is set to Yes if we used realistic AI imagery or video of real people, places or events, or AI-generated music. A chart, an animation or a synthetic narration voice alone does not need it. See `references/voice-and-ai.md`.
- [ ] Shorts: if over one minute, it contains no third-party claimed content (it would be blocked).

## When a claim, a warning or a strike arrives

Do not panic, do not dispute on reflex, and do not delete the video before reading `references/claims-and-strikes.md`. A Content ID claim is not a strike. A dispute without a real licence can turn a claim into a strike, and three copyright strikes end the channel and every linked channel.

## Before applying to YPP

Read `references/originality-for-data-videos.md` section "Self-audit before review" and go through the channel as the reviewer will: the main theme, the most-viewed videos, the newest videos, titles, thumbnails, descriptions and the About section. Fix or make private what would fail. A refused channel can usually reapply after 30 days, and the second refusal can mean a longer wait.

## Keeping this skill true

YouTube changes these rules several times a year. Everything here was checked against YouTube's own help pages on **2 November 2026**; the pages are listed in `references/sources.md`. Before we apply to YPP, before a new kind of video, or when this date is more than three months old, re-read the relevant primary page and update the reference file and the date. If a secondary blog disagrees with YouTube's own page, YouTube's page wins.

This skill is practical guidance, not legal or tax advice. For tax, ask an accountant in Sri Lanka; for a serious copyright dispute, ask a lawyer.

## Reference files

| File | Read it when |
|---|---|
| `references/audience-europe.md` | Choosing topics, language, units, publishing times, translations and where (not) to promote |
| `references/monetization-and-ypp.md` | Thresholds, the 2027 change, review, refusal and appeal, AdSense, payment, tax, how much Shorts and long-form pay |
| `references/originality-for-data-videos.md` | Planning a series or a format; before the YPP review; after a "reused content" refusal |
| `references/music-and-audio.md` | Choosing background music or sound effects for any video or Short |
| `references/voice-and-ai.md` | Choosing a voiceover, using AI for scripts, images, music or video; the AI disclosure question |
| `references/data-and-visuals.md` | Choosing a data source, citing it, using flags, logos, photos, maps or fonts |
| `references/metadata-and-community.md` | Titles, thumbnails, descriptions, tags, comments, made-for-kids, sensitive topics, ad suitability |
| `references/claims-and-strikes.md` | A Content ID claim, a copyright strike, a Community Guidelines warning or strike, limited ads |
| `references/sources.md` | Checking a rule against YouTube's own page |
| `assets/licence-log.csv` | Starting the licence log for the channel |
