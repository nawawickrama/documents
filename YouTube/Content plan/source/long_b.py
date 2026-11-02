"""Long-form videos 8-13 of the first 30-day plan. Numbers checked against the downloaded
data on 2 November 2026, except L08 (football), which must be compiled from UEFA's records."""
from datetime import date

LONG_B = [
dict(
    id="L08", date=date(2026, 11, 18), pillar="Sport", fmt="Bar chart race of titles by club, then by country",
    title="Every European Cup Winner, 1956–2026: The Title Race by Club and Country",
    title_b="70 Years of Europe's Biggest Club Trophy, in One Race",
    thumb="Trophy silhouette (our own drawing, not UEFA's) with club colours. Text: 70 YEARS, ONE TROPHY",
    thumb_b="Spanish and English flags head to head. Text: SPAIN vs ENGLAND",
    length="7 min", charts="Title race by club 1956–2026; second race by country; era labels",
    source="UEFA, official list of European Champion Clubs' Cup and UEFA Champions League finals (compile by hand)",
    link="https://www.uefa.com/uefachampionsleague/history/", licence="Facts (results) are not owned; do not use UEFA logos, the starball, club crests or match footage",
    data_status="To compile and verify",
    checks="Build the winners table from UEFA's site and check every year twice. Fill in the 2026 winner (final played 30 May 2026). Counts below are to 2025 and must be re-checked. Use club colours and names, never crests or UEFA marks.",
    summary="Every winner of Europe's top club competition, from the first European Cup in 1956 to the Champions League today, as a race by club and by country. Dynasties, one-time winners, and the countries that have never won it.",
    chapters=["0:00 70 finals", "0:25 How we counted", "0:50 Real Madrid's first five", "1:40 Lisbon, Milan and Glasgow", "2:30 Dutch and German hat-tricks", "3:20 England's golden run", "4:10 The Champions League era", "5:10 By country", "6:10 What it means"],
    data_note="One title per final. The European Champion Clubs' Cup (1956–1992) and the UEFA Champions League (since 1993) are counted as one competition, as UEFA does.",
    tags="Champions League winners, European Cup winners, Champions League history, every Champions League winner, Real Madrid titles, AC Milan, Bayern Munich, Liverpool, Barcelona, Ajax, football history, football bar chart race, Spain vs England football, European football, data visualisation, Terrachart",
    hashtags="#ChampionsLeague #Football #Europe",
    music="Energetic but not anthemic sports-style track (Audio Library). No real anthems.",
    end_screen="L01 Europe's Biggest Economies (different audience, same channel) or best-performing video so far",
    pinned="Which club's run would you rather have watched live: Real Madrid 1956–60 or Ajax 1971–73?",
    script="""[0:00 HOOK]
Seventy finals, and almost a third of them won by Spanish clubs. But one country's clubs have won it with six different teams, and some of Europe's biggest football nations have never won it at all. Here's every European Cup and Champions League winner, as a race.
[2026 WINNER: VERIFY AND ADD. All counts below are to 2025.]

[0:25 HOW WE COUNTED]
We count one title for each final, from the first European Cup in 1956 to today's Champions League. UEFA treats them as one competition, so do we. Results come from UEFA's official records.

[0:50 REAL MADRID'S FIRST FIVE]
1956 to 1960: Real Madrid win the first five finals in a row. No one has come close to that start. Spain leads the country race from day one.

[1:40 LISBON, MILAN AND GLASGOW]
Benfica win in 1961 and 1962. Then Milan's clubs: AC Milan in 1963, Inter in 1964 and 1965. Real Madrid again in 1966.
In 1967, Celtic become the first British club to win it, then Manchester United in 1968.

[2:30 DUTCH AND GERMAN HAT-TRICKS]
The 1970s belong to two countries. Feyenoord win in 1970, then Ajax win three in a row, 1971 to 1973. Then Bayern Munich win three in a row, 1974 to 1976.

[3:20 ENGLAND'S GOLDEN RUN]
From 1977 to 1984, English clubs win seven finals out of eight: Liverpool four times, Nottingham Forest twice, and Aston Villa once. Hamburg's 1983 win is the only break.
Then the mid-1980s bring some of the most surprising winners: Steaua Bucharest in 1986, Porto in 1987, PSV Eindhoven in 1988, and Red Star Belgrade in 1991.

[4:10 THE CHAMPIONS LEAGUE ERA]
In 1992 the competition takes its new name. Marseille win the first Champions League final in 1993.
Since then, the big clubs pull away. Real Madrid add title after title, including three in a row from 2016 to 2018. Barcelona win four between 2006 and 2015. Bayern, Liverpool, Chelsea, and Milan keep adding theirs. Manchester City win their first in 2023, and Paris Saint-Germain theirs in 2025.
[2026: ADD WINNER]
By club, to 2025: Real Madrid 15, AC Milan 7, Bayern and Liverpool 6 each, Barcelona 5, Ajax 4, Inter and Manchester United 3 each.

[5:10 BY COUNTRY]
Now the same titles by country. To 2025: Spain 20, England 15, Italy 12, Germany 8, the Netherlands 6, Portugal 4, France 2, and one each for Scotland, Romania and Serbia, then part of Yugoslavia.
England's 15 came from six different clubs. Spain's 20 came from just two.
[ON SCREEN: country race; update with 2026]

[6:10 WHAT IT MEANS]
24 clubs have won Europe's biggest club trophy. Only a handful have won it more than twice. And countries with huge football cultures, like Turkey, Greece or Belgium, are still waiting for their first.
Which club's run would you have liked to see live? Tell us below.
"""),

dict(
    id="L09", date=date(2026, 11, 23), pillar="Money & life", fmt="Line race + ranked bars, Black Friday week",
    title="Who Shops Online the Most in Europe? (2008–2025)",
    title_b="In 2008, 3% of Bulgarians Shopped Online. Now It's Half.",
    thumb="Shopping basket icon, Irish and Bulgarian flags. Text: 95% vs 51%",
    thumb_b="Bulgarian flag with an arrow. Text: 3% → 51%",
    length="6 min", charts="Line race 2008–2025 for 12 countries; ranked bars 2025; series-break marker at 2020",
    source="Eurostat, Internet purchases by individuals (isoc_ec_ibuy to 2019, isoc_ec_ib20 from 2020), people aged 16–74 who bought online in the last 12 months",
    link="https://ec.europa.eu/eurostat/databrowser/view/isoc_ec_ib20/default/table", licence="CC BY 4.0 (Eurostat reuse policy)",
    data_status="Checked 2 Nov 2026",
    checks="Mark the series break in 2020 on the chart. Keep 'why' explanations hedged.",
    summary="The share of people in each EU country who bought something online in the last year, from 2008 to 2025, just in time for Black Friday. Ireland and the Netherlands near 95 percent, Bulgaria and Italy far behind, and the pandemic jump.",
    chapters=["0:00 95 vs 51", "0:25 What we're measuring", "0:55 2008", "1:50 The 2010s", "2:40 The pandemic jump", "3:20 2025", "4:30 Why the gaps?", "5:20 What it means"],
    data_note="Share of people aged 16–74 who bought or ordered goods or services online in the previous 12 months. Eurostat changed the survey in 2020, so the line has a break there.",
    tags="online shopping Europe, e-commerce Europe, Black Friday Europe, who shops online the most, online shopping by country, internet shopping, Ireland online shopping, Netherlands online shopping, Bulgaria online shopping, Italy online shopping, digital economy, Eurostat, data visualisation, Terrachart",
    hashtags="#BlackFriday #OnlineShopping #Europe",
    music="Bright, playful track (Audio Library)",
    end_screen="L02 Minimum Wage in Every EU Country",
    pinned="Are you buying anything this Black Friday? Online or in a shop?",
    script="""[0:00 HOOK]
Black Friday is this week. In Ireland, 95 out of every 100 people bought something online in the past year: the highest share in the EU. In Bulgaria, it's 51. In 2008, it was fewer than 3. Here's how Europe moved its shopping online.

[0:25 WHAT WE'RE MEASURING]
This is Eurostat's survey of people aged 16 to 74: did you buy or order anything online in the last twelve months? Goods or services, from a book to a train ticket. In 2020, Eurostat changed the survey, so we've marked a small break in the line there.

[0:55 2008]
2008. In the EU as a whole, 29 percent. The leaders: Denmark at 59 percent, the Netherlands 56, Sweden and Germany 53.
At the other end, online shopping barely existed: Lithuania 6 percent, Romania 4, Bulgaria under 3.

[1:50 THE 2010s]
Through the 2010s, every line climbs. By 2015, the EU average is 49 percent. Denmark reaches 79, Luxembourg 78, Germany 73. Romania is still at 11.
By 2019, the EU is at 60 percent. And look at Italy: only 38 percent, one of the lowest in the EU, despite being one of its biggest economies.

[2:40 THE PANDEMIC JUMP]
2020. Shops close, and the EU average jumps from 60 to 65 percent in a single year. Bulgaria goes from 22 to 31. Romania from 23 to 38. For many people, the first online order happened that spring.

[3:20 2025]
2025. EU average: 74 percent.
Top: Ireland 95, the Netherlands 94, Denmark 91, Sweden 89.
Germany 81, France 80, Spain 71, Poland 70, Greece and Hungary 68, Portugal 61, Romania 60.
And at the bottom: Italy at 56, and Bulgaria at 51.

[4:30 WHY THE GAPS?]
A few things seem to matter. How common bank cards are, and how much people trust paying online. How fast and cheap delivery is. And age: in countries with older populations, fewer people shop online.
Italy is an interesting case. It has a large, older population, and cash and small local shops are still a big part of daily life.

[5:20 WHAT IT MEANS]
In seventeen years, online shopping went from something a third of Europeans did to something three quarters do. The gap between north and south-east is closing, but it's still there.
If you're shopping this Friday, you're in good company. Next on Terrachart: which European countries run on renewables.
"""),

dict(
    id="L10", date=date(2026, 11, 21), pillar="Economy over time", fmt="Two-line race, then a second chart per person (PPP)",
    title="The EU vs the USA, 1995–2025: How Big Is the Gap Really?",
    title_b="The EU's Economy Was Bigger Than America's in 2011. What Happened?",
    thumb="EU and US flags on two diverging lines. Text: $21T vs $31T",
    thumb_b="EU flag ahead of US flag in 2011. Text: EU WAS BIGGER",
    length="7–8 min", charts="Total GDP lines 1995–2025 (US$); per-person PPP lines; hours-worked aside",
    source="World Bank, GDP (current US$) NY.GDP.MKTP.CD and GDP per capita PPP (constant 2021 international $) NY.GDP.PCAP.PP.KD, EU = today's 27 members, updated 8 Oct 2026; Penn World Table via OWID for hours",
    link="https://data.worldbank.org/indicator/NY.GDP.MKTP.CD?locations=EU-US", licence="CC BY 4.0",
    data_status="Checked 2 Nov 2026",
    checks="Keep it neutral: no 'Europe is dying' or 'America is better' framing. Do not quote euro/dollar exchange rates unless checked against ECB data.",
    summary="The EU and the United States compared for thirty years, two ways: total size in dollars, where the US pulls far ahead, and living standards per person adjusted for prices, where the gap has barely moved. Why both are true.",
    chapters=["0:00 The EU was bigger in 2011", "0:30 Two ways to measure", "1:00 Total size, 1995–2025", "2:40 Why the lines split", "3:50 Per person, adjusted for prices", "5:00 Time off", "5:50 What it means"],
    data_note="Total GDP in current US dollars (exchange rates matter). Per person: GDP per capita at purchasing power parity, constant 2021 international dollars. EU means today's 27 members throughout.",
    tags="EU vs USA, Europe vs America economy, EU economy, US economy, GDP EU vs US, GDP per capita Europe America, euro dollar, transatlantic gap, European economy decline, living standards, productivity, World Bank data, data visualisation, Terrachart",
    hashtags="#EU #USA #Economy",
    music="Measured, neutral documentary track (Audio Library)",
    end_screen="L13 The World's Largest Economies (when live) or L01",
    pinned="Which measure matters more to you: total economic size, or living standards per person?",
    script="""[0:00 HOOK]
In 2011, the European Union's economy was bigger than the United States'. Today the US economy is 45 percent larger: 30.8 trillion dollars against 21.2. That sounds like Europe collapsed. But look at living standards per person instead, and the gap has barely moved in thirty years. Both of these are true. Here's how.

[0:30 TWO WAYS TO MEASURE]
We'll use two World Bank measures. First, total GDP in US dollars: the size of each economy. Second, GDP per person, adjusted for prices and inflation: a better guide to how well the average person lives. "EU" here means today's 27 members, in every year.

[1:00 TOTAL SIZE]
1995. The EU: 8.3 trillion dollars. The US: 7.6. Europe is ahead.
By 2000 the US has pulled ahead: 10.3 trillion against 7.3. The euro launched weak against the dollar, and that shrank Europe's figures.
Then the euro strengthens, and from 2007 to 2009 the EU is bigger again: 16.4 trillion against 14.8 in 2008. The last year the EU comes out on top is 2011.
After that, the lines split. 2013: US 16.9, EU 15.4. 2020: US 21.4, EU 15.5. And 2025: US 30.8 trillion, EU 21.2.

[2:40 WHY THE LINES SPLIT]
Three reasons.
One, the exchange rate. When the euro falls against the dollar, every European number on this chart falls with it, even if nothing changed in Europe.
Two, people. The US population has grown faster than the EU's, and more people means a bigger economy.
Three, real growth. Since the financial crisis, the US has grown faster, helped by its technology giants and energy production.

[3:50 PER PERSON, ADJUSTED FOR PRICES]
Now the second chart: GDP per person, adjusted for prices.
1995: the average European, 35,114 international dollars. The average American, 47,227. Europe is at 74 percent of the US level.
2025: Europe 55,087. America 76,931. Europe is at 72 percent.
Both grew by about 60 percent over thirty years. The gap is real, and it's large, but it's almost exactly the same size it was in 1995.

[5:00 TIME OFF]
There's one more difference. The average American worker works about 1,789 hours a year. In Germany, it's 1,335. Europeans take part of their wealth as free time: longer holidays, shorter weeks, more part-time work. GDP counts the work, not the holiday.

[5:50 WHAT IT MEANS]
So, is Europe falling behind? In total dollars, clearly yes, and exchange rates and population explain a lot of it. In living standards per person, the gap is about where it has been for a generation.
Next on Terrachart: who shops online the most in Europe, just in time for Black Friday.
"""),

dict(
    id="L11", date=date(2026, 11, 25), pillar="Energy & climate", fmt="Ranked bars race 2004–2025 + target line",
    title="Which European Countries Run on Renewables? (2004–2025)",
    title_b="Norway Gets 82% of Its Energy From Renewables. Belgium: 15%.",
    thumb="Wind turbine icon, Norwegian and Belgian flags. Text: 82% vs 15%",
    thumb_b="EU flag with rising bar. Text: 10% → 26%",
    length="6–7 min", charts="Bar race of renewable share 2004–2025; EU line with 2030 target at 42.5%; electricity-vs-all-energy explainer",
    source="Eurostat, Share of energy from renewable sources (nrg_ind_ren), share in gross final energy consumption",
    link="https://ec.europa.eu/eurostat/databrowser/view/nrg_ind_ren/default/table", licence="CC BY 4.0 (Eurostat reuse policy)",
    data_status="Checked 2 Nov 2026",
    checks="Check whether the 2025 values are final or provisional and say so. Do not quote a renewable share of electricity unless it is checked separately.",
    summary="How much of each European country's energy comes from renewables, from 2004 to 2025: electricity, heating and transport together. The Nordic leaders, the countries that started from almost nothing, and how far the EU is from its 2030 target.",
    chapters=["0:00 82% vs 15%", "0:25 Energy, not just electricity", "1:00 2004", "2:00 The climb", "3:10 2025", "4:20 The 2030 target", "5:10 What it means"],
    data_note="Renewables' share of gross final energy consumption: all energy used for electricity, heating and cooling, and transport, not electricity alone.",
    tags="renewable energy Europe, renewables by country, share of renewable energy, green energy Europe, Norway renewable energy, Sweden renewable energy, Germany energy transition, Netherlands renewables, EU 2030 target, energy transition, climate, Eurostat, data visualisation, Terrachart",
    hashtags="#RenewableEnergy #Europe #Climate",
    music="Airy, optimistic track (Audio Library)",
    end_screen="L06 Electricity Prices in Europe",
    pinned="Does your country get more or less of its energy from renewables than you expected?",
    script="""[0:00 HOOK]
In 2004, renewables supplied about a tenth of the energy the EU used. In 2025, more than a quarter. Norway is at 82 percent. Belgium, 15. And the EU has promised 42.5 percent by 2030. Who's on track?

[0:25 ENERGY, NOT JUST ELECTRICITY]
One thing first. These numbers aren't about electricity alone. They cover all the energy a country uses: electricity, but also heating homes and powering cars and lorries. Renewables have grown fastest in electricity, so a country's share of renewable electricity is usually much higher than the numbers you'll see here. The data is Eurostat's.

[1:00 2004]
2004. The EU average: 9.6 percent. The leaders are countries with lots of rivers and forests: Norway at 58 percent, thanks to hydropower, Sweden 38, Latvia 33, Finland 29.
At the bottom, countries with almost none: Belgium 1.9 percent, Luxembourg 0.9, Malta 0.1. Germany is at 6.2 percent, the Netherlands just 2.

[2:00 THE CLIMB]
Then the climb begins. Wind farms in the North Sea, solar panels on roofs across Germany, Spain and Italy, heat pumps and biomass in Scandinavia.
Watch the Netherlands: from 2 percent to over 22, more than eleven times higher. Germany: from 6 to 24, nearly four times higher.

[3:10 2025]
2025. Norway 82 percent. In the EU: Sweden 65, Finland 53, Denmark 48, Latvia 46. Portugal 37.
In the middle: Greece 27, Spain 26, Romania 26, Germany and France 24, the Netherlands and Bulgaria 23, Italy 21.
At the bottom: Poland 19, Ireland 17, Slovakia 16, and Belgium 15.
EU average: 26.2 percent.

[4:20 THE 2030 TARGET]
The EU's target is 42.5 percent by 2030. From 26.2 in 2025, that means adding more than three percentage points every year. Over the last twenty years, the EU managed less than one a year on average. So the next five years would have to move far faster than anything so far.
[ON SCREEN: target line, gap shaded]

[5:10 WHAT IT MEANS]
Geography gives some countries a head start: rivers, forests, wind. But the biggest jumps came from countries that started with almost nothing, which shows how fast things can change when they decide to.
Next on Terrachart: house prices since 2010, and where homes got out of reach.
"""),

dict(
    id="L12", date=date(2026, 11, 28), pillar="Money & life", fmt="Index line race (2010 = 100) + ranked bars",
    title="House Prices in Europe Since 2010: Where Homes Got Out of Reach",
    title_b="House Prices in Hungary Almost Quadrupled. In Italy They Fell.",
    thumb="House icon with a tall Hungarian bar and a flat Italian bar. Text: +291%",
    thumb_b="Two houses, one huge one small. Text: ×4 vs −2%",
    length="6–7 min", charts="Index lines rebased to 2010 = 100; ranked bars of change 2010–2025; note on nominal prices",
    source="Eurostat, House price index (prc_hpi_a), all dwellings, annual average, rebased by Terrachart to 2010 = 100, updated 1 Oct 2026",
    link="https://ec.europa.eu/eurostat/databrowser/view/prc_hpi_a/default/table", licence="CC BY 4.0 (Eurostat reuse policy)",
    data_status="Checked 2 Nov 2026",
    checks="Say on screen that prices are not adjusted for inflation. If we compare with wage growth, check Eurostat wage data first.",
    summary="How house prices changed in every EU country between 2010 and 2025. Hungary's nearly fourfold rise, the Baltic boom, Portugal's surge, and why prices in Italy are lower than fifteen years ago.",
    chapters=["0:00 +291% vs −2%", "0:25 What we're measuring", "1:00 The leaders", "2:20 The middle", "3:20 The flat-liners", "4:10 Why 2010 matters", "5:10 What it means"],
    data_note="House price index for all dwellings, annual average, nominal (not adjusted for inflation), rebased so that 2010 = 100.",
    tags="house prices Europe, property prices Europe, housing crisis Europe, house prices by country, Hungary house prices, Portugal house prices, Netherlands house prices, Germany house prices, Spain house prices, Italy house prices, housing affordability, real estate Europe, Eurostat, data visualisation, Terrachart",
    hashtags="#HousePrices #Housing #Europe",
    music="Mellow, slightly melancholic track (Audio Library)",
    end_screen="L02 Minimum Wage in Every EU Country",
    pinned="Could you afford to buy where you grew up? Tell us the country.",
    script="""[0:00 HOOK]
Since 2010, house prices in Hungary have risen by 291 percent: almost four times what they were. In Italy, they're 2 percent lower than in 2010. Same continent, same fifteen years. Here's where homes got expensive, and why.

[0:25 WHAT WE'RE MEASURING]
We're using Eurostat's house price index for all homes, new and existing. To compare countries fairly, we've set every country to 100 in 2010. A value of 200 means prices doubled. These are actual prices, not adjusted for inflation, so part of every rise is simply prices in general going up.

[1:00 THE LEADERS]
2025. At the top: Hungary, plus 291 percent. Estonia, plus 245. Lithuania, plus 207. Latvia, plus 166. Czechia, plus 158. Portugal, plus 146. Bulgaria, plus 136.
Most of the leaders are in central and eastern Europe, where prices started low and incomes grew fast. Portugal is the exception: there, a wave of foreign buyers and short-term holiday rentals pushed up prices in Lisbon and on the coast.

[2:20 THE MIDDLE]
Poland: prices doubled, plus 105 percent. The Netherlands, plus 93. Ireland, plus 86. Germany, plus 82. Sweden, plus 80.

[3:20 THE FLAT-LINERS]
And then the countries where prices barely moved. Romania, plus 38. Spain and Cyprus, plus 34. France, plus 28. Finland, plus 5.
And Italy: minus 2 percent. In fifteen years, the average Italian home has lost value, before even counting inflation.

[4:10 WHY 2010 MATTERS]
The starting year matters. In 2010, Spain and Ireland had just been through enormous housing crashes. Prices kept falling for a few more years before they recovered. Start the clock in 2014 instead, and both would look very different.
Italy never had a big boom, and its population and economy have barely grown, so demand stayed flat.
[ON SCREEN: Spain and Ireland lines dipping, then rising]

[5:10 WHAT IT MEANS]
Across most of the EU, homes cost far more than in 2010. Whether that means "out of reach" depends on wages, interest rates and rents, which we'll come back to. But in Hungary, the Baltics and Portugal, prices have run far ahead of almost everything else.
Next on Terrachart: the world's largest economies since 1970.
"""),

dict(
    id="L13", date=date(2026, 11, 30), pillar="Economy over time", fmt="World bar chart race 1970–2025, Europe highlighted",
    title="The World's Largest Economies, 1970–2025: Where Does Europe Stand?",
    title_b="India Passed the UK in 2022. In 2025 the UK Took Its Place Back.",
    thumb="World race frozen at 2025, European bars in teal. Text: EUROPE vs THE WORLD",
    thumb_b="UK and Indian flags neck and neck. Text: UK vs INDIA",
    length="8 min", charts="Top-10 world race 1970–2025 with European countries highlighted; EU-as-one-bar comparison at the end",
    source="World Bank, GDP (current US$), NY.GDP.MKTP.CD, all countries, updated 8 Oct 2026",
    link="https://data.worldbank.org/indicator/NY.GDP.MKTP.CD", licence="CC BY 4.0",
    data_status="Checked 2 Nov 2026",
    checks="Name that these are dollar figures and that exchange rates explain the UK–India and Germany–Japan swaps. Russia appears in the race as itself; keep the narration neutral.",
    summary="The ten largest economies in the world from 1970 to 2025, with Europe's countries highlighted. How Japan rose and fell back, China's climb, Germany passing Japan, India and the UK swapping places, and what the EU would look like as one economy.",
    chapters=["0:00 Four of six, then two", "0:25 What we're measuring", "1:00 1970", "2:00 Japan's rise", "3:00 China arrives", "4:20 Germany passes Japan", "5:00 India vs the UK", "6:00 2025", "6:40 The EU as one"],
    data_note="GDP in current US dollars, so exchange-rate moves can change the order. The EU figure covers today's 27 members.",
    tags="largest economies in the world, world GDP ranking, biggest economies 1970 to 2025, GDP bar chart race, US economy, China economy, Germany economy, Japan economy, India economy, UK economy, India vs UK, Germany vs Japan, EU economy, world economy history, data visualisation, Terrachart",
    hashtags="#WorldEconomy #GDP #Europe",
    music="Big, cinematic but restrained track (Audio Library)",
    end_screen="L10 The EU vs the USA",
    pinned="Where will Europe be in this ranking by 2050? Your guess.",
    script="""[0:00 HOOK]
In 1970, four of the world's six largest economies were in Europe. In 2025, only two are. And one of them, the United Kingdom, has just taken fifth place back from India. Here's the world's economic race since 1970, with Europe highlighted.

[0:25 WHAT WE'RE MEASURING]
This is GDP in US dollars at each year's prices and exchange rates, from the World Bank. Remember: when a currency moves, a country can jump up or down this chart without anything changing at home.

[1:00 1970]
1970. The United States is far ahead, at 1.07 trillion dollars. Then Japan, Germany, France, the United Kingdom and Italy, all between about 110 and 220 billion. China is seventh, at 93 billion.
[ON SCREEN: European bars in teal]

[2:00 JAPAN'S RISE]
Through the 1970s and 80s, Japan races ahead. By 1990: the US at 6.0 trillion, Japan 3.3, Germany 1.8, France 1.3, Italy 1.2, the UK 1.1. Japan's economy is more than half the size of America's.

[3:00 CHINA ARRIVES]
Then China. In 2000 it's sixth, at 1.2 trillion, just behind France. In 2010 it passes Japan to become the world's second-largest economy. By 2025 it's at 19.5 trillion.

[4:20 GERMANY PASSES JAPAN]
Japan's economy stalls in dollar terms, and the yen weakens. In 2023, Germany passes Japan for third place: 4.56 trillion against 4.39.

[5:00 INDIA vs THE UK]
Now watch India. In 2022, it passes the United Kingdom: 3.25 trillion against 3.18. It stays ahead in 2023 and 2024. But in 2025, with a stronger pound, the UK edges back in front: 4.00 trillion against India's 3.96.
At India's recent growth rate, that lead may not last long.

[6:00 2025]
2025. The United States, 30.8 trillion. China, 19.5. Germany, 5.05. Japan, 4.44. The UK, 4.00. India, 3.96. France, 3.37. Russia, 2.56. Italy, 2.55. Canada, 2.32.
Germany, the UK, France and Italy are still in the top ten. But only Germany and the UK are in the top six.

[6:40 THE EU AS ONE]
One more way to look at it. If the European Union were counted as one economy, it would be 21.2 trillion dollars: second in the world, behind the US and ahead of China.
Divided, Europe's countries are mid-sized. Together, they're a giant. Whether that matters depends on how much they act as one.
"""),
]
