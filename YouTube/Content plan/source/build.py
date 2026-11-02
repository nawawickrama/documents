"""Builds the Terrachart 30-day content plan workbook from long_a.py, long_b.py and shorts.py.
Run with a Python that has openpyxl:  python build.py"""
import json
import re
from datetime import date, time
from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter
from openpyxl.workbook.properties import CalcProperties
from openpyxl.worksheet.datavalidation import DataValidation

from long_a import LONG_A
from long_b import LONG_B
from shorts import SHORTS

# Every tab lists videos in publishing order.
LONG = sorted(LONG_A + LONG_B, key=lambda v: v["date"])
SHORTS = sorted(SHORTS, key=lambda s: s["date"])
OUT = Path(__file__).resolve().parent.parent / "Terrachart content plan 2 Nov - 1 Dec 2026.xlsx"

NAVY, TEAL, AMBER, PAPER = "0D1B2A", "1FB5A3", "FFB23F", "F4F1EA"
F = "Arial"
HEAD = Font(name=F, bold=True, color="FFFFFF", size=10)
BODY = Font(name=F, size=10)
BOLD = Font(name=F, size=10, bold=True)
TITLE = Font(name=F, size=16, bold=True, color=NAVY)
SUB = Font(name=F, size=10, italic=True, color="555555")
LINK = Font(name=F, size=10, color="1F5FBF", underline="single")
HEAD_FILL = PatternFill("solid", fgColor=NAVY)
SECTION_FILL = PatternFill("solid", fgColor=TEAL)
INPUT_FILL = PatternFill("solid", fgColor="FFF2CC")
BAND_FILL = PatternFill("solid", fgColor="F7F7F5")
WRAP = Alignment(wrap_text=True, vertical="top")
TOP = Alignment(vertical="top")
THIN = Border(bottom=Side(style="thin", color="DDDDDD"))

LONG_TIME = {0: time(17, 0), 2: time(17, 0), 5: time(15, 0)}  # Mon, Wed, Sat (weekday numbers)
SHORT_TIME = time(19, 0)
STATUSES = ["Idea", "Scripted", "Data checked", "Voice done", "Edited", "Scheduled", "Published"]

wb = Workbook()


def header(ws, cols, row=1):
    for i, (name, width) in enumerate(cols, start=1):
        c = ws.cell(row=row, column=i, value=name)
        c.font, c.fill, c.alignment = HEAD, HEAD_FILL, Alignment(wrap_text=True, vertical="center")
        ws.column_dimensions[get_column_letter(i)].width = width
    ws.row_dimensions[row].height = 30
    ws.freeze_panes = ws.cell(row=row + 1, column=3)


def style_body(ws, first_row, last_row, ncols, wrap_cols=()):
    for r in range(first_row, last_row + 1):
        for c in range(1, ncols + 1):
            cell = ws.cell(row=r, column=c)
            cell.font = cell.font if cell.font.color and cell.font.underline else BODY
            cell.alignment = WRAP if c in wrap_cols else TOP
            cell.border = THIN
            if (r - first_row) % 2 == 1 and not (cell.fill and cell.fill.fgColor.rgb == "00FFF2CC"):
                cell.fill = BAND_FILL


def tz_formulas(ws, row, cet_col):
    """UK, Sri Lanka and New York times from the CET time in cet_col (all November/December, no DST)."""
    ref = f"{get_column_letter(cet_col)}{row}"
    for offset, hours in enumerate(["-1/24", "+4.5/24", "-6/24"], start=1):
        c = ws.cell(row=row, column=cet_col + offset, value=f"=MOD({ref}{hours},1)")
        c.number_format = "hh:mm"


def words_formula(ref):
    return f'=IF(LEN(TRIM({ref}))=0,0,LEN(TRIM({ref}))-LEN(SUBSTITUTE(TRIM({ref})," ",""))+1)'


STUDIO = Path.home() / "Documents" / "YouTube" / "Studio" / "src" / "videos"


def made(v):
    """The video's final words and timing from the Studio, once it has been made."""
    d = STUDIO / v["id"].lower()
    if not (d / "words.json").exists() or not (d / "timing.json").exists():
        return None
    words = json.loads((d / "words.json").read_text())
    timing = json.loads((d / "timing.json").read_text())["timing"]
    p = words["pacing"]
    at, starts = p["lead"], {}
    for line in words["lines"]:
        starts[line["id"]] = at
        at += timing[line["id"]] + p.get("pauseAfter", {}).get(line["id"], p["pause"])
    mmss = lambda s: f"{int(s // 60)}:{int(s % 60):02d}"
    chapters = [f"{'0:00' if i == 0 else mmss(starts[k])} {t}" for i, (k, t) in enumerate(words["chapters"].items())]
    script = []
    for line in words["lines"]:
        if line["id"] in words["chapters"]:
            script.append(f"\n[{mmss(starts[line['id']])} {words['chapters'][line['id']].upper()}]")
        script.append(line["say"])
    return chapters, "\n".join(script)


for v in LONG:
    final = made(v)
    if final:
        v["chapters"], v["script"] = final
        v["status"] = "Edited"
for s in SHORTS:
    d = STUDIO / s["id"].lower()
    if (d / "timing.json").exists():
        s["script"] = " ".join(line["say"] for line in json.loads((d / "words.json").read_text())["lines"])
        s["status"] = "Edited"


def description(v):
    chapters = "\n".join(v["chapters"])
    return (
        f"{v['summary']}\n\nChapters\n{chapters}\n\nSources\n- {v['source']}. {v['link']}\n"
        f"What we did to the data: {v['data_note']}\n\nMusic: original score by Terrachart\n"
        "Narration: AI voice (Kokoro)\n\n"
        f"Terrachart - the world, charted through time.\n{v['hashtags']}"
    )


# ---------------------------------------------------------------- Strategy
ws = wb.active
ws.title = "Strategy"
ws.column_dimensions["A"].width = 30
ws.column_dimensions["B"].width = 110
ws["A1"] = "Terrachart: 30-day content strategy"
ws["A1"].font = TITLE
ws["A2"] = "Monday 2 November to Tuesday 1 December 2026 (moved three days earlier on 2 November, the day L01 was finished). Made 2 November 2026. All numbers in the scripts were checked against the downloaded data, except the football video (L08)."
ws["A2"].font = SUB
ws.merge_cells("A2:B2")

sections = [
    ("The goal", [
        ("Why this month matters", "To earn from ads we need the YouTube Partner Program: 1,000 subscribers plus 4,000 public watch hours on long videos (last 12 months), or 10 million Shorts views in 90 days. On 1 February 2027 the bar for new channels doubles to 8,000 hours or 20 million Shorts views. Review takes about a month, so we want to qualify by late December 2026."),
        ("Where we start", "223 subscribers, 0 public videos, 0 watch hours (2 November 2026). Sri Lanka has no 500-subscriber starter tier, so 1,000 is the first gate."),
        ("30-day targets", "See the Tracker tab. Realistic: 500 subscribers, 800 watch hours, 300,000 Shorts views. Stretch: 1,000 subscribers, 2,000 watch hours, 2 million Shorts views. Every number is public, organic and from real viewers; we never buy views or subscribers."),
        ("What success also looks like", "Long-form click-through rate 4% or more, average view duration 35% or more, and at least 70% of watch time from Europe, the US, Canada and Australia."),
    ]),
    ("Audience and voice", [
        ("Who we make videos for", "Europe first (UK, Ireland, Germany, Austria, Switzerland, Netherlands, Belgium, the Nordics, France and the rest of the EU), then the US, Canada and Australia. Not Sri Lanka: ad rates follow the viewer's country. 'Country of residence' in YouTube Studio stays Sri Lanka."),
        ("How we write", "English for people whose first language may not be English. Short sentences. British spelling. Metric units, euros where it fits. Every number named with its source and year."),
        ("Translations", "Add the translated titles from the Translations tab in YouTube Studio > Languages for every long video. Ask a native speaker to check them when possible."),
        ("Promotion", "Never share new videos in Sri Lankan WhatsApp, Facebook or Telegram groups, or ask friends to watch. The first viewers decide who YouTube shows a video to next. Share only where the target audience is, and follow each community's rules."),
    ]),
    ("What we publish", [
        ("Cadence", "3 long videos a week (Monday, Wednesday, Saturday) and 1 Short every day. 13 long videos and 30 Shorts in 30 days."),
        ("Video length", "Long videos: 8–9 minutes, so YouTube allows mid-video ads and each view adds more watch hours. The scripts here are first drafts (330–680 words, every number checked). Each is expanded to about 1,100 words at its data check four days before release, using more beats from the same dataset. Shorts: 20–30 seconds, one idea each."),
        ("Publishing times (CET)", "Long videos Monday and Wednesday 17:00 CET, Saturday 15:00 CET. Shorts every day 19:00 CET. In Sri Lanka that is 21:30, 19:30 and 23:30. Always schedule in YouTube Studio with the time zone set to Central European Time; never publish live."),
        ("Why these times", "17:00 CET catches Europe after work and New York at lunch (11:00). Saturday 15:00 catches European afternoons and the US morning. Shorts at 19:00 CET catch the European evening scroll and US lunchtime."),
        ("Content pillars", "Economy over time, Money & life, Society over time, Country stories, Sport, Energy & climate. The mix is counted live below from the Long-form tab."),
        ("How Shorts work with long videos", "Each long video gets two Shorts: one on release day, one the day after. Four standalone Shorts fill the gaps. Every Short carries one idea with narration and links to its long video with YouTube's 'Related video' setting."),
    ]),
    ("Rules that keep us monetisable", [
        ("Originality", "Every video has narration that explains why the numbers move. No bar chart with only music. Vary chart types and structures; never two near-identical formats in a row. Keep screen recordings of the data work for a possible YPP appeal."),
        ("Music", "Our own score, made in code by ~/Documents/YouTube/Studio/scripts/music.py: owned by the channel, so no licence and no Content ID claims. A new track (key, tempo or seed) for each long video. The YouTube Audio Library is the fallback. Log every track in the Licence log tab."),
        ("Voice", "Kokoro, voice af_heart (American woman), chosen 2 November 2026. Free, runs on the Mac, Apache 2.0 licence, allowed in monetised videos. Never the Mac's built-in 'say' voices (non-commercial only). The narrator never poses as an expert giving advice. No AI label needed for a synthetic narration voice; the description says 'Narration: AI voice (Kokoro)'."),
        ("Data", "Only sources with a licence that allows reuse (see Sources tab). Name the source on screen and in the description. Label estimates and projections."),
        ("Titles and thumbnails", "Must show what the video shows. No shock images, no strong profanity, no fake 'breaking news' looks."),
        ("Upload settings", "Not made for kids. Category Education. Language English (UK). Altered or synthetic content: No for charts and a synthetic narration voice; Yes if we ever use AI music or realistic AI images of real people or events."),
        ("Full rules", "~/Documents/YouTube/Guidelines (the youtube-channel-compliance skill)."),
    ]),
    ("Production workflow (each long video)", [
        ("Day -4", "Re-download the dataset, re-check every number in the script, fix anything revised, and expand the draft to about 1,100 words. Mark 'Data checked'."),
        ("Day -3", "Record or generate the narration. Choose the Audio Library track. Log both."),
        ("Day -2", "Build the charts and edit the video. Make thumbnail A and B. Cut the two Shorts."),
        ("Day -1", "Upload as Private, paste the description, tags, chapters and translations, set the end screen. Run the upload checklist. Schedule."),
        ("Release day", "Pin the comment. Reply to early comments for the first two hours. Set the Short's 'Related video'."),
        ("After 48 hours", "Check click-through rate and retention. If CTR is under 3%, switch to title B or thumbnail B (or run YouTube's Test & compare)."),
    ]),
    ("Decisions waiting for the owner", [
        ("Narration voice", "Decided 2 November 2026: Kokoro af_heart. Samples in ~/Documents/YouTube/Voice samples."),
        ("Automatic dubbing", "YouTube offered early access. Test it on L01 into German, French and Spanish, and check the result before publishing."),
        ("Channel email", "The About section shows nawawickrama@gmail.com. A separate address keeps the personal one private."),
    ]),
    ("How to use this workbook", [
        ("Tabs", "Calendar (day by day) · Long-form (one row per video, description ready to paste) · Scripts (narration, section by section) · Shorts · Translations · Tags bank · Sources · Licence log · Tracker."),
        ("Cells you fill in", "Yellow cells: Status, the Tracker numbers, and the Licence log's music and voice rows. Everything else is filled in; the UK, Sri Lanka and New York times, word counts and run times calculate themselves."),
        ("Status values", ", ".join(STATUSES)),
    ]),
]
r = 4
for title, rows in sections:
    c = ws.cell(row=r, column=1, value=title)
    c.font, c.fill = Font(name=F, bold=True, color="FFFFFF", size=11), SECTION_FILL
    ws.cell(row=r, column=2).fill = SECTION_FILL
    r += 1
    for k, v in rows:
        ws.cell(row=r, column=1, value=k).font = BOLD
        cell = ws.cell(row=r, column=2, value=v)
        cell.font, cell.alignment = BODY, WRAP
        ws.cell(row=r, column=1).alignment = TOP
        r += 1
    if title == "What we publish":
        for pillar in ["Economy over time", "Money & life", "Society over time", "Country story", "Sport", "Energy & climate"]:
            ws.cell(row=r, column=1, value=f"  {pillar}").font = BODY
            c = ws.cell(row=r, column=2, value=f"=COUNTIF('Long-form'!$H$2:$H$14,\"{pillar}\")&\" long videos\"")
            c.font = BODY
            r += 1
    r += 1

# ---------------------------------------------------------------- Long-form
lf = wb.create_sheet("Long-form")
cols = [("ID", 6), ("Publish date", 12), ("Day", 6), ("Time CET", 8), ("UK", 7), ("Sri Lanka", 9), ("New York", 9),
        ("Pillar", 16), ("Format", 26), ("Title (A)", 42), ("Title B (for A/B test)", 40), ("Thumbnail A", 34), ("Thumbnail B", 30),
        ("Target length", 11), ("Draft script words", 9), ("Draft narration now (min)", 10), ("Charts", 34), ("Data source", 40), ("Link", 30),
        ("Licence", 18), ("Data status", 14), ("Checks before production", 40), ("Description (paste into YouTube)", 60),
        ("Tags", 50), ("Tags length (max 500)", 10), ("Hashtags", 22), ("Music (Audio Library)", 28), ("AI disclosure", 18),
        ("Made for kids", 9), ("End screen", 26), ("Pinned comment", 34), ("Shorts from this video", 14), ("Status", 12)]
header(lf, cols)
for i, v in enumerate(LONG, start=2):
    shorts_for = ", ".join(s["id"] for s in SHORTS if s["linked"] == v["id"])
    row = [v["id"], v["date"], v["date"].strftime("%a"), LONG_TIME[v["date"].weekday()], None, None, None,
           v["pillar"], v["fmt"], v["title"], v["title_b"], v["thumb"], v["thumb_b"], "8–9 min after expansion",
           f"=SUMIF(Scripts!$A:$A,A{i},Scripts!$E:$E)", f"=ROUND(O{i}/145,1)", v["charts"], v["source"], v["link"],
           v["licence"], v["data_status"], v["checks"], description(v), v["tags"], f"=LEN(X{i})", v["hashtags"], v["music"],
           "No (charts and narration only)", "No", v["end_screen"], v["pinned"], shorts_for, v.get("status", "Scripted")]
    for c, val in enumerate(row, start=1):
        lf.cell(row=i, column=c, value=val)
    lf.cell(row=i, column=2).number_format = "ddd d mmm yyyy"
    lf.cell(row=i, column=4).number_format = "hh:mm"
    tz_formulas(lf, i, 4)
    lf.cell(row=i, column=19).hyperlink = v["link"]
    lf.cell(row=i, column=33).fill = INPUT_FILL
    if v["data_status"] != "Checked 2 Nov 2026":
        lf.cell(row=i, column=21).fill = PatternFill("solid", fgColor="FCE4D6")
style_body(lf, 2, len(LONG) + 1, len(cols), wrap_cols=(9, 10, 11, 12, 13, 17, 18, 20, 21, 22, 23, 24, 27, 30, 31))
for i, v in enumerate(LONG, start=2):
    lf.cell(row=i, column=19).font = LINK
    lf.row_dimensions[i].height = 150
    if v["data_status"] != "Checked 2 Nov 2026":
        lf.cell(row=i, column=21).fill = PatternFill("solid", fgColor="FCE4D6")
status_list = '"' + ",".join(STATUSES) + '"'
dv = DataValidation(type="list", formula1=status_list, allow_blank=True)
lf.add_data_validation(dv)
dv.add(f"AG2:AG{len(LONG) + 1}")
lf.auto_filter.ref = f"A1:{get_column_letter(len(cols))}{len(LONG) + 1}"

# ---------------------------------------------------------------- Scripts
sc = wb.create_sheet("Scripts")
header(sc, [("Video", 7), ("Section", 26), ("Type", 11), ("Text", 100), ("Words", 8), ("Est. seconds", 9)])
r = 2
for v in LONG:
    section = ""
    for line in v["script"].strip().splitlines():
        line = line.strip()
        if not line:
            continue
        m = re.fullmatch(r"\[(\d+:\d\d) ([^\]]+)\]", line)
        if m:
            section = f"{m.group(1)} {m.group(2)}"
            continue
        if line.startswith("[ON SCREEN"):
            kind, text = "On screen", line.strip("[]").split(":", 1)[1].strip()
        elif line.startswith("["):
            kind, text = "Check", line.strip("[]")
        else:
            kind, text = "Narration", line
        sc.cell(row=r, column=1, value=v["id"])
        sc.cell(row=r, column=2, value=section)
        sc.cell(row=r, column=3, value=kind)
        sc.cell(row=r, column=4, value=text)
        sc.cell(row=r, column=5, value=words_formula(f"D{r}") if kind == "Narration" else 0)
        sc.cell(row=r, column=6, value=f"=ROUND(E{r}/145*60,0)")
        if kind == "Check":
            sc.cell(row=r, column=4).fill = PatternFill("solid", fgColor="FCE4D6")
        r += 1
style_body(sc, 2, r - 1, 6, wrap_cols=(4,))
for rr in range(2, r):
    if sc.cell(row=rr, column=3).value == "Check":
        sc.cell(row=rr, column=4).fill = PatternFill("solid", fgColor="FCE4D6")
    if sc.cell(row=rr, column=3).value == "On screen":
        sc.cell(row=rr, column=4).font = Font(name=F, size=10, italic=True, color="1F6F66")
sc.auto_filter.ref = f"A1:F{r - 1}"

# ---------------------------------------------------------------- Shorts
sh = wb.create_sheet("Shorts")
cols = [("ID", 6), ("Publish date", 12), ("Day", 6), ("Time CET", 8), ("UK", 7), ("Sri Lanka", 9), ("New York", 9),
        ("From long video", 9), ("Title", 44), ("Opening text on screen", 20), ("Narration script", 70), ("Words", 7),
        ("Est. seconds", 8), ("Visual", 36), ("Source (on screen and in description)", 34), ("Description (paste into YouTube)", 50),
        ("Hashtags", 26), ("Related video", 14), ("Music", 22), ("Status", 12)]
header(sh, cols)
long_titles = {v["id"]: v["title"] for v in LONG}
for i, s in enumerate(SHORTS, start=2):
    desc = (f"{s['title']}.\n\nSource: {s['source']}.\nFull video: {long_titles[s['linked']]} (link after it is published)\n\n"
            f"Terrachart - the world, charted through time.\n{s['hashtags']}")
    row = [s["id"], s["date"], s["date"].strftime("%a"), SHORT_TIME, None, None, None, s["linked"], s["title"], s["hook"],
           s["script"], words_formula(f"K{i}"), f"=ROUND(L{i}/150*60,0)", s["visual"], s["source"], desc, s["hashtags"],
           s["linked"], "Our own score (Studio/scripts/music.py)", s.get("status", "Scripted")]
    for c, val in enumerate(row, start=1):
        sh.cell(row=i, column=c, value=val)
    sh.cell(row=i, column=2).number_format = "ddd d mmm yyyy"
    sh.cell(row=i, column=4).number_format = "hh:mm"
    tz_formulas(sh, i, 4)
    sh.cell(row=i, column=20).fill = INPUT_FILL
style_body(sh, 2, len(SHORTS) + 1, len(cols), wrap_cols=(9, 10, 11, 14, 15, 16, 17))
for i in range(2, len(SHORTS) + 2):
    sh.row_dimensions[i].height = 90
dv2 = DataValidation(type="list", formula1=status_list, allow_blank=True)
sh.add_data_validation(dv2)
dv2.add(f"T2:T{len(SHORTS) + 1}")
sh.auto_filter.ref = f"A1:{get_column_letter(len(cols))}{len(SHORTS) + 1}"

# ---------------------------------------------------------------- Calendar
cal = wb.create_sheet("Calendar", 1)
cols = [("Date", 14), ("Day", 6), ("Week", 6), ("Long video", 8), ("Long video title", 52), ("Long CET", 8), ("Long in Sri Lanka", 10),
        ("Short", 7), ("Short title", 52), ("Short CET", 8), ("Short in Sri Lanka", 10), ("Note", 30)]
header(cal, cols)
notes = {date(2026, 11, 27): "Black Friday (S23 is about online shopping)", date(2026, 11, 23): "Black Friday week: L09 is about online shopping",
         date(2026, 11, 2): "First upload. Set the channel trailer after L01 is live.", date(2026, 12, 1): "Last day of this plan. Plan the next 30 days by 25 Nov."}
by_date_long = {v["date"]: v for v in LONG}
for i, s in enumerate(SHORTS, start=2):
    dday = s["date"]
    v = by_date_long.get(dday)
    cal.cell(row=i, column=1, value=dday).number_format = "ddd d mmm yyyy"
    cal.cell(row=i, column=2, value=dday.strftime("%a"))
    cal.cell(row=i, column=3, value=f"=INT((A{i}-DATE(2026,11,2))/7)+1")
    if v:
        cal.cell(row=i, column=4, value=v["id"])
        cal.cell(row=i, column=5, value=v["title"])
        cal.cell(row=i, column=6, value=LONG_TIME[dday.weekday()]).number_format = "hh:mm"
        cal.cell(row=i, column=7, value=f"=MOD(F{i}+4.5/24,1)").number_format = "hh:mm"
    cal.cell(row=i, column=8, value=s["id"])
    cal.cell(row=i, column=9, value=s["title"])
    cal.cell(row=i, column=10, value=SHORT_TIME).number_format = "hh:mm"
    cal.cell(row=i, column=11, value=f"=MOD(J{i}+4.5/24,1)").number_format = "hh:mm"
    cal.cell(row=i, column=12, value=notes.get(dday, ""))
style_body(cal, 2, len(SHORTS) + 1, len(cols), wrap_cols=(5, 9, 12))
for i in range(2, len(SHORTS) + 2):
    if cal.cell(row=i, column=4).value:
        for c in (4, 5):
            cal.cell(row=i, column=c).font = Font(name=F, size=10, bold=True, color=NAVY)
r = len(SHORTS) + 3
cal.cell(row=r, column=1, value="Totals").font = BOLD
cal.cell(row=r, column=4, value=f"=COUNTA(D2:D{len(SHORTS) + 1})").font = BOLD
cal.cell(row=r, column=8, value=f"=COUNTA(H2:H{len(SHORTS) + 1})").font = BOLD

# ---------------------------------------------------------------- Translations
TR = {
 "L01": ["Europas größte Volkswirtschaften 1970–2025: Wer aufstieg und wer fiel", "Les plus grandes économies d'Europe, 1970–2025 : qui a monté, qui a chuté", "Las mayores economías de Europa, 1970–2025: quién subió y quién cayó", "Le maggiori economie d'Europa, 1970–2025: chi è salito e chi è sceso", "De grootste economieën van Europa, 1970–2025: wie steeg en wie daalde", "Największe gospodarki Europy 1970–2025: kto awansował, a kto spadł"],
 "L02": ["Mindestlohn in jedem EU-Land (2026): Euro vs. echte Kaufkraft", "Le salaire minimum dans chaque pays de l'UE (2026) : en euros et en pouvoir d'achat réel", "El salario mínimo en cada país de la UE (2026): en euros y en poder adquisitivo real", "Il salario minimo in ogni paese UE (2026): in euro e in potere d'acquisto reale", "Het minimumloon in elk EU-land (2026): in euro's en in echte koopkracht", "Płaca minimalna w każdym kraju UE (2026): w euro i realna siła nabywcza"],
 "L03": ["Wie Polen aufgeholt hat: 35 Jahre in Zahlen (1990–2025)", "Comment la Pologne a rattrapé son retard : 35 ans en chiffres (1990–2025)", "Cómo Polonia alcanzó al resto: 35 años en cifras (1990–2025)", "Come la Polonia ha recuperato: 35 anni in numeri (1990–2025)", "Hoe Polen de achterstand inhaalde: 35 jaar in cijfers (1990–2025)", "Jak Polska dogoniła Europę: 35 lat w liczbach (1990–2025)"],
 "L04": ["Lebenserwartung in Europa 1950–2023: Wie der Süden den Norden überholte", "L'espérance de vie en Europe, 1950–2023 : comment le Sud a dépassé le Nord", "La esperanza de vida en Europa, 1950–2023: cómo el sur superó al norte", "L'aspettativa di vita in Europa, 1950–2023: come il Sud ha superato il Nord", "Levensverwachting in Europa, 1950–2023: hoe het zuiden het noorden inhaalde", "Średnia długość życia w Europie 1950–2023: jak Południe wyprzedziło Północ"],
 "L05": ["Wer arbeitet in Europa am längsten? (Nicht, wer du denkst)", "Qui travaille le plus d'heures en Europe ? (Pas ceux que vous croyez)", "¿Quién trabaja más horas en Europa? (No es quien crees)", "Chi lavora più ore in Europa? (Non chi pensi)", "Wie werkt de meeste uren in Europa? (Niet wie je denkt)", "Kto pracuje najdłużej w Europie? (To nie ten, o kim myślisz)"],
 "L06": ["Strompreise in Europa 2008–2026: Wer zahlt am meisten?", "Prix de l'électricité en Europe, 2008–2026 : qui paie le plus ?", "Precios de la electricidad en Europa, 2008–2026: ¿quién paga más?", "Prezzi dell'elettricità in Europa, 2008–2026: chi paga di più?", "Stroomprijzen in Europa, 2008–2026: wie betaalt het meest?", "Ceny prądu w Europie 2008–2026: kto płaci najwięcej?"],
 "L07": ["Europas bevölkerungsreichste Länder 1950–2100 (UN-Prognosen)", "Les pays les plus peuplés d'Europe, 1950–2100 (projections de l'ONU)", "Los países más poblados de Europa, 1950–2100 (proyecciones de la ONU)", "I paesi più popolosi d'Europa, 1950–2100 (proiezioni ONU)", "De volkrijkste landen van Europa, 1950–2100 (VN-prognoses)", "Najludniejsze kraje Europy 1950–2100 (prognozy ONZ)"],
 "L08": ["Alle Champions-League-Sieger seit 1956: Das Titelrennen nach Verein und Land", "Tous les vainqueurs de la Coupe d'Europe, 1956–2026 : la course aux titres par club et par pays", "Todos los campeones de Europa, 1956–2026: la carrera de títulos por club y país", "Tutti i vincitori della Coppa dei Campioni, 1956–2026: la corsa ai titoli per club e nazione", "Alle winnaars van de Europacup I, 1956–2026: de titelrace per club en land", "Wszyscy zwycięzcy Pucharu Europy 1956–2026: wyścig tytułów według klubów i krajów"],
 "L09": ["Wer kauft in Europa am meisten online ein? (2008–2025)", "Qui achète le plus en ligne en Europe ? (2008–2025)", "¿Quién compra más por internet en Europa? (2008–2025)", "Chi compra di più online in Europa? (2008–2025)", "Wie shopt het meest online in Europa? (2008–2025)", "Kto w Europie najczęściej kupuje online? (2008–2025)"],
 "L10": ["EU gegen USA 1995–2025: Wie groß ist der Abstand wirklich?", "UE contre États-Unis, 1995–2025 : quel est vraiment l'écart ?", "La UE frente a EE. UU., 1995–2025: ¿cuál es la brecha real?", "UE contro USA, 1995–2025: quanto è grande davvero il divario?", "De EU tegen de VS, 1995–2025: hoe groot is de kloof echt?", "UE kontra USA 1995–2025: jak duża jest naprawdę różnica?"],
 "L11": ["Welche Länder Europas setzen auf erneuerbare Energien? (2004–2025)", "Quels pays européens fonctionnent aux énergies renouvelables ? (2004–2025)", "¿Qué países europeos funcionan con energías renovables? (2004–2025)", "Quali paesi europei vanno a energie rinnovabili? (2004–2025)", "Welke Europese landen draaien op hernieuwbare energie? (2004–2025)", "Które kraje Europy stawiają na odnawialne źródła energii? (2004–2025)"],
 "L12": ["Immobilienpreise in Europa seit 2010: Wo Wohnen unbezahlbar wurde", "Les prix de l'immobilier en Europe depuis 2010 : où les logements sont devenus inabordables", "Los precios de la vivienda en Europa desde 2010: dónde se volvió inalcanzable", "I prezzi delle case in Europa dal 2010: dove sono diventate irraggiungibili", "Huizenprijzen in Europa sinds 2010: waar een huis onbetaalbaar werd", "Ceny mieszkań w Europie od 2010 roku: gdzie dom stał się nieosiągalny"],
 "L13": ["Die größten Volkswirtschaften der Welt 1970–2025: Wo steht Europa?", "Les plus grandes économies du monde, 1970–2025 : où en est l'Europe ?", "Las mayores economías del mundo, 1970–2025: ¿dónde queda Europa?", "Le maggiori economie del mondo, 1970–2025: dove si colloca l'Europa?", "De grootste economieën ter wereld, 1970–2025: waar staat Europa?", "Największe gospodarki świata 1970–2025: gdzie jest Europa?"],
}
tr = wb.create_sheet("Translations")
header(tr, [("ID", 6), ("English (UK)", 44), ("German", 44), ("French", 44), ("Spanish", 44), ("Italian", 44), ("Dutch", 44), ("Polish", 44)])
for i, v in enumerate(LONG, start=2):
    for c, val in enumerate([v["id"], v["title"]] + TR[v["id"]], start=1):
        tr.cell(row=i, column=c, value=val)
style_body(tr, 2, len(LONG) + 1, 8, wrap_cols=range(2, 9))
n = len(LONG) + 3
tr.cell(row=n, column=1, value="How to use: YouTube Studio > Languages > Add language > Title & description. Paste the title; translate the first two lines of the description too. Ask a native speaker to check before the video goes public.").font = SUB

# ---------------------------------------------------------------- Tags bank
tb = wb.create_sheet("Tags bank")
header(tb, [("Group", 22), ("Tags (comma-separated, use the ones that fit the video)", 120)])
bank = [
    ("Always", "Terrachart, data visualisation, data visualization, statistics"),
    ("Economy over time", "GDP, economy, economic history, bar chart race, biggest economies, GDP per capita, World Bank data, Europe economy"),
    ("Money & life", "cost of living Europe, wages in Europe, prices in Europe, Eurostat, comparison by country, EU countries compared"),
    ("Society over time", "demographics, population, life expectancy, Europe, Our World in Data, UN data"),
    ("Country stories", "[country] economy, [country] vs [country], how [country] got rich, Eastern Europe, EU membership"),
    ("Sport", "football history, European football, Champions League history, football statistics"),
    ("Energy & climate", "renewable energy Europe, energy prices, energy transition, climate, electricity"),
    ("Rules", "Only tags that describe this video. Total under 500 characters (the Long-form tab counts it). No other channels' names. Three hashtags at most, at the end of the description."),
]
for i, (g, t) in enumerate(bank, start=2):
    tb.cell(row=i, column=1, value=g)
    tb.cell(row=i, column=2, value=t)
style_body(tb, 2, len(bank) + 1, 2, wrap_cols=(2,))

# ---------------------------------------------------------------- Sources
src = wb.create_sheet("Sources")
header(src, [("Dataset", 44), ("Publisher", 20), ("Code", 22), ("Used in", 22), ("Licence", 26), ("Link", 48), ("Downloaded file", 26), ("Downloaded on", 13), ("Credit line", 44)])
D = date(2026, 11, 2)
sources = [
    ("GDP (current US$)", "World Bank", "NY.GDP.MKTP.CD", "L01, L10, L13, S01, S02, S05, S22, S29, S30", "CC BY 4.0", "https://data.worldbank.org/indicator/NY.GDP.MKTP.CD", "gdp.json, euus_gdp.json, world_gdp.json", "Source: World Bank, GDP (current US$)"),
    ("GDP per capita, PPP (constant 2021 international $)", "World Bank", "NY.GDP.PCAP.PP.KD", "L03, L10, S06, S25", "CC BY 4.0", "https://data.worldbank.org/indicator/NY.GDP.PCAP.PP.KD", "gdppc.json, euus_pc.json", "Source: World Bank, GDP per capita, PPP"),
    ("Monthly minimum wages, bi-annual", "Eurostat", "earn_mw_cur", "L02, S03, S04", "CC BY 4.0", "https://ec.europa.eu/eurostat/databrowser/view/earn_mw_cur/default/table", "mw.json", "Source: Eurostat (earn_mw_cur), July 2026"),
    ("Life expectancy at birth", "UN WPP 2024 via Our World in Data", "life-expectancy", "L04, S08, S09", "CC BY 4.0", "https://ourworldindata.org/grapher/life-expectancy", "lifeexp.csv", "Source: UN World Population Prospects (2024), via Our World in Data"),
    ("Annual working hours per worker", "Penn World Table via Our World in Data", "annual-working-hours-per-worker", "L03, L05, L10, S07, S10, S11", "CC BY 4.0", "https://ourworldindata.org/grapher/annual-working-hours-per-worker", "hours.csv", "Source: Feenstra et al., Penn World Table, via Our World in Data"),
    ("Electricity prices for household consumers", "Eurostat", "nrg_pc_204", "L06, S13, S14", "CC BY 4.0", "https://ec.europa.eu/eurostat/databrowser/view/nrg_pc_204/default/table", "elec.json", "Source: Eurostat (nrg_pc_204)"),
    ("Population with UN projections", "UN WPP 2024 via Our World in Data", "population-with-un-projections", "L03, L07, S15, S16, S19", "CC BY 4.0", "https://ourworldindata.org/grapher/population-with-un-projections", "pop.csv", "Source: UN World Population Prospects (2024), medium projection, via Our World in Data"),
    ("Internet purchases by individuals", "Eurostat", "isoc_ec_ibuy, isoc_ec_ib20", "L09, S20, S23", "CC BY 4.0", "https://ec.europa.eu/eurostat/databrowser/view/isoc_ec_ib20/default/table", "shopold.json, shop20.json", "Source: Eurostat (isoc_ec_ibuy, isoc_ec_ib20)"),
    ("Share of energy from renewable sources", "Eurostat", "nrg_ind_ren", "L11, S21, S24, S26", "CC BY 4.0", "https://ec.europa.eu/eurostat/databrowser/view/nrg_ind_ren/default/table", "ren.json", "Source: Eurostat (nrg_ind_ren)"),
    ("House price index, annual", "Eurostat", "prc_hpi_a", "L12, S12, S27, S28", "CC BY 4.0", "https://ec.europa.eu/eurostat/databrowser/view/prc_hpi_a/default/table", "hpi.json", "Source: Eurostat (prc_hpi_a), rebased to 2010 = 100 by Terrachart"),
    ("European Cup / Champions League finals", "UEFA", "-", "L08, S17, S18", "Facts only; no logos, crests or footage", "https://www.uefa.com/uefachampionsleague/history/", "(to compile)", "Source: UEFA"),
]
for i, s in enumerate(sources, start=2):
    vals = list(s[:6]) + [s[6], D if s[6] != "(to compile)" else None, s[7]]
    for c, val in enumerate(vals, start=1):
        src.cell(row=i, column=c, value=val)
    src.cell(row=i, column=6).hyperlink = s[5]
    src.cell(row=i, column=8).number_format = "d mmm yyyy"
style_body(src, 2, len(sources) + 1, 9, wrap_cols=(1, 2, 4, 5, 6, 7, 9))
for i in range(2, len(sources) + 2):
    src.cell(row=i, column=6).font = LINK
src.cell(row=len(sources) + 3, column=1, value="Raw files: ~/Documents/YouTube/Data/downloaded-2026-11-02. Re-download before each video and note the new date.").font = SUB

# ---------------------------------------------------------------- Licence log
ll = wb.create_sheet("Licence log")
header(ll, [("Date used", 12), ("Video", 10), ("Asset type", 12), ("Asset name", 34), ("Source", 30), ("Licence", 26), ("Proof", 40), ("Credit text", 34), ("Notes", 30)])
log = [
    (D, "All", "Font", "Inter", "Inter Project (rsms/inter)", "SIL Open Font License 1.1", "~/Documents/YouTube/Brand/source/fonts/Inter-LICENSE.txt", "", "Used in logo, banner and charts"),
    (D, "All", "Logo", "Terrachart logo, banner, watermark", "Own work (Claude for the owner)", "Owned by the channel", "~/Documents/YouTube/Brand/source/assets.html", "", ""),
] + [(D, s[3], "Data", s[0], s[1], s[4], f"{s[5]} (downloaded {D:%d %b %Y}: {s[6]})", s[7], "") for s in sources if s[6] != "(to compile)"]
for i, row in enumerate(log, start=2):
    for c, val in enumerate(row, start=1):
        ll.cell(row=i, column=c, value=val)
    ll.cell(row=i, column=1).number_format = "d mmm yyyy"
start = len(log) + 2
for i, (vid, kind) in enumerate([(v["id"], k) for v in LONG for k in ("Music", "Voice")], start=start):
    ll.cell(row=i, column=2, value=vid)
    ll.cell(row=i, column=3, value=kind)
    done = (STUDIO / vid.lower() / "timing.json").exists()
    if kind == "Voice":
        values = ((4, "Kokoro-82M, voice af_heart"), (5, "hexgrad/Kokoro-82M, run locally with kokoro-js"), (6, "Apache 2.0"),
                  (7, "https://huggingface.co/hexgrad/Kokoro-82M (model card checked 2 Nov 2026)"), (8, "Narration: AI voice (Kokoro)"))
    else:
        track = f"terrachart-bed-{vid[1:]}" if done else "terrachart-bed-NN (new key, tempo or seed)"
        values = ((4, track), (5, "Own work: ~/Documents/YouTube/Studio/scripts/music.py"), (6, "Owned by the channel"),
                  (7, "Generated in code; no samples or third-party audio"), (8, "Music: original score by Terrachart"))
    for c, val in values:
        ll.cell(row=i, column=c, value=val)
    if done:
        ll.cell(row=i, column=1, value=D)
    else:
        ll.cell(row=i, column=1).fill = INPUT_FILL
    ll.cell(row=i, column=1).number_format = "d mmm yyyy"
style_body(ll, 2, start + 2 * len(LONG) - 1, 9, wrap_cols=(2, 4, 5, 6, 7, 8, 9))

# ---------------------------------------------------------------- Tracker
tk = wb.create_sheet("Tracker")
tk["A1"] = "Weekly tracker: fill in the yellow cells every Sunday from YouTube Studio > Analytics"
tk["A1"].font = Font(name=F, size=12, bold=True, color=NAVY)
tk["A2"] = "Row 4 is the real starting point (2 November 2026). Subscribers and watch hours come from Studio > Earn; Shorts views from Analytics (last 90 days)."
tk["A2"].font = SUB
cols = [("Week ending", 14), ("Subscribers", 12), ("Gained this week", 11), ("% of 1,000", 10), ("Public watch hours (12 months)", 14),
        ("% of 4,000", 10), ("Shorts views (90 days)", 14), ("% of 10M", 10), ("Long videos published", 11), ("Shorts published", 10),
        ("Long-form CTR", 10), ("Avg view duration %", 11), ("Watch time from target countries %", 14), ("Notes", 40)]
header(tk, cols, row=3)
tk.freeze_panes = "B4"
weeks = [date(2026, 11, 2), date(2026, 11, 8), date(2026, 11, 15), date(2026, 11, 22), date(2026, 11, 29), date(2026, 12, 6)]
for i, wk in enumerate(weeks, start=4):
    tk.cell(row=i, column=1, value=wk).number_format = "ddd d mmm yyyy"
    if i == 4:
        for c, val in ((2, 223), (5, 0), (7, 0)):
            tk.cell(row=i, column=c, value=val)
        tk.cell(row=i, column=3, value=0)
        tk.cell(row=i, column=14, value="Starting point, before the first upload")
    else:
        tk.cell(row=i, column=3, value=f'=IF(B{i}="","",B{i}-B{i-1})')
    tk.cell(row=i, column=4, value=f'=IF(B{i}="","",MIN(1,B{i}/1000))').number_format = "0%"
    tk.cell(row=i, column=6, value=f'=IF(E{i}="","",MIN(1,E{i}/4000))').number_format = "0%"
    tk.cell(row=i, column=8, value=f'=IF(G{i}="","",MIN(1,G{i}/10000000))').number_format = "0.0%"
    tk.cell(row=i, column=9, value=f"=COUNTIF('Long-form'!$B$2:$B$14,\"<=\"&A{i})")
    tk.cell(row=i, column=10, value=f"=COUNTIF(Shorts!$B$2:$B$31,\"<=\"&A{i})")
    for c in (2, 5, 7, 11, 12, 13):
        if i > 4 or c in (11, 12, 13):
            tk.cell(row=i, column=c).fill = INPUT_FILL
    for c in (11, 12, 13):
        tk.cell(row=i, column=c).number_format = "0.0%"
    tk.cell(row=i, column=7).number_format = "#,##0"
style_body(tk, 4, 3 + len(weeks), len(cols), wrap_cols=(14,))
tk["A11"] = "Targets by 6 December"
tk["A11"].font = BOLD
targets = [("Subscribers", 500, 1000), ("Public watch hours", 800, 2000), ("Shorts views (90 days)", 300000, 2000000),
           ("Long-form CTR", 0.04, 0.06), ("Average view duration", 0.35, 0.5), ("Watch time from target countries", 0.7, 0.85)]
for c, h in enumerate(["Measure", "Realistic", "Stretch"], start=1):
    cell = tk.cell(row=12, column=c, value=h)
    cell.font, cell.fill = HEAD, HEAD_FILL
for i, (m, a, b) in enumerate(targets, start=13):
    tk.cell(row=i, column=1, value=m).font = BODY
    for c, val in ((2, a), (3, b)):
        cell = tk.cell(row=i, column=c, value=val)
        cell.font = BODY
        cell.number_format = "0%" if val < 1 else "#,##0"

# order the tabs
wb._sheets = [wb[n] for n in ["Strategy", "Calendar", "Long-form", "Scripts", "Shorts", "Translations", "Tags bank", "Sources", "Licence log", "Tracker"]]
for wsx in wb.worksheets:
    wsx.sheet_properties.tabColor = {"Strategy": AMBER, "Calendar": AMBER, "Tracker": AMBER}.get(wsx.title, TEAL)
wb.active = 0
wb.calculation = CalcProperties(fullCalcOnLoad=True)  # no cached values from openpyxl, so recalculate on open
OUT.parent.mkdir(parents=True, exist_ok=True)
wb.save(OUT)
print("saved", OUT)
