"""Long-form videos 1-7 of the first 30-day plan. Every number was checked against
the downloaded data on 2 November 2026 (files in ~/Documents/YouTube/Data/downloaded-2026-11-02)."""
from datetime import date

LONG_A = [
dict(
    id="L01", date=date(2026, 11, 2), pillar="Economy over time", fmt="Bar chart race + annotations",
    title="Europe's Biggest Economies, 1970–2025: Who Rose and Who Fell",
    title_b="Poland Is About to Pass Switzerland: Europe's Economies Since 1970",
    thumb="Freeze-frame of the race at 2025, flags on bars. Text: 1970 → 2025",
    thumb_b="Polish flag bar touching the Swiss bar. Text: $9 BILLION APART",
    length="7–8 min", charts="Bar chart race 1970–2025; callouts for each swap; closing ranked bar",
    source="World Bank, GDP (current US$), NY.GDP.MKTP.CD, updated 8 Oct 2026",
    link="https://data.worldbank.org/indicator/NY.GDP.MKTP.CD", licence="CC BY 4.0",
    data_status="Checked 2 Nov 2026",
    checks="Confirm what the World Bank's Germany series covers before 1991 and say it on screen. Re-check the 2025 Swiss and Polish figures before render (revisions).",
    summary="Fourteen of Europe's largest economies, every year from 1970 to 2025. Why Italy briefly passed the UK, why second place kept changing hands, why Ireland looks richer than it feels, and how Poland went from 66 billion dollars to a trillion.",
    chapters=["0:00 Poland's trillion", "0:20 What the bars show", "0:55 The 1970s", "1:40 Il sorpasso", "2:30 The 1990s", "3:15 The financial crisis", "4:00 Ireland's catch", "4:40 Poland", "6:00 The 2025 ranking", "6:30 What it means"],
    data_note="GDP in current US dollars, so exchange rates move the bars. Countries: Germany, UK, France, Italy, Spain, Netherlands, Poland, Switzerland, Sweden, Belgium, Ireland, Austria, Norway, Denmark. Russia and Turkey are not included.",
    tags="Europe economy, biggest economies in Europe, European economies, GDP Europe, GDP 1970 to 2025, economic history, bar chart race, Germany economy, UK economy, France economy, Italy economy, Poland economy, Poland GDP, Switzerland economy, Ireland GDP, il sorpasso, data visualisation, Terrachart",
    hashtags="#Europe #Economy #DataVisualisation",
    music="Calm, slowly building cinematic track (Audio Library, attribution not required)",
    end_screen="L03 How Poland Caught Up (when live); until then the channel trailer or L02",
    pinned="Which swap surprised you most: Italy passing the UK in 1986, or Poland closing in on Switzerland?",
    script="""[0:00 HOOK]
In 1990, Poland's entire economy was worth 66 billion US dollars. That was about a quarter of Sweden's. In 2025 it crossed one trillion dollars, and it is now just nine billion short of Switzerland. Poland is only one of the stories in the last 55 years of Europe's economic race. Let's watch it happen.
[ON SCREEN: race frozen at 2025, Poland and Switzerland side by side, gap labelled "$9 bn"]

[0:20 WHAT THE BARS SHOW]
First, what we're measuring. Each bar is GDP: the value of everything a country produces in a year. It's in US dollars, at each year's prices and exchange rates, and it comes from the World Bank. We've included fourteen of Europe's largest economies: the big EU members, the United Kingdom, Switzerland and Norway. Russia and Turkey aren't in this race, because a large part of each lies outside Europe, and the World Bank's figures for Russia only start in 1989.
One more thing. Because these are dollars, a bar can jump or drop when a currency moves, even if nothing changed at home. Remember that. It explains several of the twists you're about to see.

[0:55 THE 1970s]
1970. Germany leads with 217 billion dollars. Then France, the United Kingdom and Italy. Spain is fifth, a long way behind.
Through the 1970s every bar grows fast, but a lot of that is inflation and a falling dollar, not just growth. By 1980, Germany has passed 950 billion.
[ON SCREEN: note on the Germany series before 1991, wording to confirm]

[1:40 IL SORPASSO]
Now watch Italy and the United Kingdom. In 1986, Italy moves ahead of Britain. Italians called it "il sorpasso", the overtaking, and it was big news in Rome. The UK takes the place back in 1988, loses it again a year later, and only settles ahead in 1994. Both economies were growing. The swaps mostly follow the exchange rate between the lira and the pound.

[2:30 THE 1990s]
1990. Germany is reunited and stays first, at 1.78 trillion dollars. In 1997, the UK passes France for second place, helped by a strong pound. And near the bottom of the chart a name we'll come back to: Poland, at 66 billion dollars, 13th of our 14.

[3:15 THE FINANCIAL CRISIS]
2007. Europe's bars are higher than ever. Germany 3.5 trillion, the UK 3.1, France 2.7. Then the financial crisis. The pound falls hard, and in 2009 France takes second place back from the UK. Second place changes hands again in 2012, 2013 and 2014: three swaps in three years. Since 2014, the UK has held second place in dollar terms.

[4:00 IRELAND'S CATCH]
Look at Ireland. In 1990 its economy was 49 billion dollars, smaller than Poland's. By 2025 it's 722 billion: bigger than Sweden's and level with Belgium's. Some of that is real growth. But a large part is the profit of big international companies that book their earnings in Ireland. That's why Ireland's own government uses a different measure, called modified national income, when it plans its budget. On this chart, Ireland looks richer than it feels on the ground.

[4:40 POLAND]
And Poland. In the 2010s it passes Belgium, then Sweden, and by 2020 it's in the top eight. In 2025 it crosses one trillion dollars: 1.035 trillion. Switzerland is at 1.044 trillion. A year earlier the gap was 52 billion. Now it's nine. If 2026 looks anything like 2025, Poland passes Switzerland next year.

[6:00 THE 2025 RANKING]
So here is 2025. Germany: 5.05 trillion dollars, first in every single year since 1970. The UK 4.0 trillion. France 3.37. Italy 2.55. Spain 1.91. The Netherlands 1.33. Then Switzerland and Poland, almost touching.

[6:30 WHAT IT MEANS]
Three things to take away.
One: the top four haven't changed in 55 years. Germany, the UK, France and Italy, in some order.
Two: most of the swaps between them come from exchange rates, not from one country suddenly getting rich.
Three: the real movers are the countries that started far behind. In dollar terms, Poland's economy is more than fifteen times bigger than in 1990.
But dollars per country don't tell you how well people live. In our next video we look at the same countries per person, adjusted for prices, and the story changes.
Sources are in the description. If you think we should have measured this differently, tell us in the comments. We read them.
"""),

dict(
    id="L02", date=date(2026, 11, 4), pillar="Money & life", fmt="Ranked bars, then re-ranked (euros → buying power)",
    title="Minimum Wage in Every EU Country (2026): Euros vs Real Buying Power",
    title_b="Which EU Country Has the Highest Minimum Wage? It Depends How You Count",
    thumb="Two bars: Luxembourg €2,771 and Bulgaria €620, flags. Text: €2,771 vs €620",
    thumb_b="German flag on top of a re-ranked list. Text: REAL #1: GERMANY",
    length="6–7 min", charts="Ranked horizontal bars in euros; animated re-sort into PPS; map of the EU coloured by PPS",
    source="Eurostat, Monthly minimum wages (earn_mw_cur), July 2026 (2026-S2), updated 31 Jul 2026",
    link="https://ec.europa.eu/eurostat/databrowser/view/earn_mw_cur/default/table", licence="CC BY 4.0 (Eurostat reuse policy)",
    data_status="Checked 2 Nov 2026",
    checks="Confirm Eurostat's note on countries with 14 payments a year before reading it out. If Eurostat publishes January 2027 figures before production, keep July 2026 (the title says 2026).",
    summary="Gross monthly minimum wages in the 22 EU countries that have one, as of July 2026. First in euros, then in purchasing power standards, which take out price differences. The gap halves, Luxembourg loses first place, and Romania passes Portugal and Greece.",
    chapters=["0:00 €2,771 vs €620", "0:30 What we're measuring", "1:15 The ranking in euros", "2:30 Adjusting for prices", "3:00 The ranking in buying power", "4:30 The US for comparison", "5:10 What it means"],
    data_note="Gross monthly minimum wages, July 2026. PPS = purchasing power standards, Eurostat's unit that removes price differences between countries. Austria, Denmark, Finland, Italy and Sweden have no national minimum wage.",
    tags="minimum wage Europe, EU minimum wage 2026, minimum wage by country, highest minimum wage in Europe, Luxembourg minimum wage, Germany minimum wage, Poland minimum wage, Romania minimum wage, Bulgaria minimum wage, purchasing power, PPS, cost of living Europe, wages in Europe, Eurostat, data visualisation, Terrachart",
    hashtags="#MinimumWage #Europe #CostOfLiving",
    music="Light, steady corporate/documentary track (Audio Library)",
    end_screen="L01 Europe's Biggest Economies",
    pinned="How far does the minimum wage go where you live? Tell us your country.",
    script="""[0:00 HOOK]
Luxembourg pays the highest minimum wage in the European Union: 2,771 euros a month. Bulgaria pays the lowest: 620. That's four and a half times more. But a euro in Sofia doesn't buy the same as a euro in Luxembourg. Take out the price differences, and the gap shrinks by half. And Luxembourg isn't first any more.
[ON SCREEN: two bars, Luxembourg and Bulgaria, then a question mark over the top spot]

[0:30 WHAT WE'RE MEASURING]
These are gross monthly minimum wages, before tax, as of July 2026. They come from Eurostat, the EU's statistics office.
Twenty-two of the 27 EU countries have a national minimum wage. Austria, Denmark, Finland, Italy and Sweden don't. There, wages are set in agreements between unions and employers, and they are often higher.
In some countries, such as Spain, Greece and Portugal, workers get fourteen payments a year. Eurostat spreads those over twelve months, so the numbers compare fairly.

[1:15 THE RANKING IN EUROS]
At the top: Luxembourg 2,771 euros. Ireland 2,391. Germany 2,343. The Netherlands 2,338. Belgium 2,234.
Then a gap, down to France at 1,867. Then Slovenia 1,482 and Spain 1,425.
In the middle: Lithuania 1,153, Poland 1,119, Cyprus 1,088, Greece and Portugal at 1,073 each, Croatia 1,050.
And below a thousand euros: Malta 994, Estonia 946, Czechia 923, Slovakia 915, Hungary 906, Romania 825, Latvia 780 and Bulgaria 620.
[ON SCREEN: the bars split into three colour groups: west, south and centre, east]

[2:30 ADJUSTING FOR PRICES]
But rent, food and transport cost very different amounts across the EU. So Eurostat also publishes these wages in purchasing power standards, or PPS. It's an artificial currency. One PPS buys the same basket of goods in every country. Watch what happens when we switch.
[ON SCREEN: bars re-sort with animation]

[3:00 THE RANKING IN BUYING POWER]
Germany moves to first place, with 2,164 PPS. Luxembourg is second at 2,108, then the Netherlands and Belgium.
Ireland falls from second to fifth, at 1,756. Prices in Ireland, especially rents, are among the highest in Europe.
France 1,692, Slovenia 1,660, Spain 1,556. And then Poland, at 1,547: in buying power, a Polish minimum wage now buys almost as much as a Spanish one.
Lithuania 1,393, Croatia 1,339. Then Romania, at 1,317, ahead of Portugal at 1,240 and Greece at 1,229.
At the bottom are Latvia and Estonia, both just under 940.
The biggest gap is now between Germany and Estonia: 2.3 times, not four and a half.

[4:30 THE US FOR COMPARISON]
Eurostat also publishes the United States for comparison. The US federal minimum wage, 7.25 dollars an hour and unchanged since 2009, works out at 1,103 euros a month, or 834 in PPS. That's lower than every EU country in buying power. But many US states set a higher minimum of their own, so the federal figure is a floor, not the typical wage.

[5:10 WHAT IT MEANS]
Three things.
One: the gap between east and west is real, but in what money actually buys, it's about half as big as the euro figures suggest.
Two: some countries have climbed fast. Poland and Romania now sit above Portugal and Greece.
Three: a high wage doesn't help as much when prices are high too. Ask anyone renting in Dublin.
A minimum wage isn't the whole picture: taxes, rents and how many people actually earn it differ a lot. But it's a good place to start.
Next on Terrachart: how Poland went from one of Europe's poorest economies to one of its fastest catch-up stories.
"""),

dict(
    id="L03", date=date(2026, 11, 7), pillar="Country story", fmt="Line chart race (per person, PPP) + milestones",
    title="How Poland Caught Up: 35 Years in Numbers (1990–2025)",
    title_b="Poland Was Poorer Than Greece in 2014. Not Any More.",
    thumb="Rising red-and-white line passing other flags. Text: ×3.7",
    thumb_b="Polish flag ahead of Greek and Portuguese flags. Text: OVERTAKING EUROPE",
    length="7–8 min", charts="Line race of GDP per person (PPP) 1990–2025 for 10 countries; milestone markers 1990, 2004, 2009; crossover callouts",
    source="World Bank, GDP per capita, PPP (constant 2021 international $), NY.GDP.PCAP.PP.KD, updated 8 Oct 2026; Penn World Table via Our World in Data (hours worked); UN World Population Prospects 2024 via Our World in Data",
    link="https://data.worldbank.org/indicator/NY.GDP.PCAP.PP.KD", licence="CC BY 4.0",
    data_status="Checked 2 Nov 2026",
    checks="Confirm Poland's 2009 GDP growth was positive (World Bank NY.GDP.MKTP.KD.ZG) before saying it was the only EU economy that grew. Say clearly that the 'two years' line is an extrapolation.",
    summary="Poland's GDP per person, adjusted for prices, from 1990 to 2025: from less than a third of Germany's to three quarters. The moments that mattered, the countries Poland overtook, and the catches: long hours and a shrinking population.",
    chapters=["0:00 From a third to three quarters", "0:25 What we're measuring", "1:00 1990: the starting line", "2:00 Joining the EU", "2:50 The crisis that skipped Poland", "3:40 Overtaking Hungary, Greece, Portugal", "5:00 2025", "5:40 The catches", "6:40 What's next"],
    data_note="GDP per person at purchasing power parity, in constant 2021 international dollars: it takes out inflation and price differences between countries.",
    tags="Poland, Poland economy, Poland GDP per capita, Poland growth, Polish economy, how Poland got rich, Poland vs Germany, Poland vs Spain, Poland vs Portugal, Poland vs Greece, EU membership, Eastern Europe economy, catch-up growth, GDP per capita PPP, data visualisation, Terrachart",
    hashtags="#Poland #Economy #Europe",
    music="Hopeful, rising piano/strings (Audio Library)",
    end_screen="L01 Europe's Biggest Economies; L05 Who Works the Longest Hours (when live)",
    pinned="Polish viewers: does this match what you've seen in your own town over the last 20 years?",
    script="""[0:00 HOOK]
In 1990, the average Pole produced less than a third of what the average German did. Today it's three quarters. On the way, Poland overtook Hungary, Greece and Portugal, and it's now within five percent of Spain. This is how it happened, and what the numbers don't show.

[0:25 WHAT WE'RE MEASURING]
We're using GDP per person, adjusted for prices. It's measured in constant international dollars, which take out both inflation and the difference in what things cost from country to country. It's the World Bank's best single measure of average living standards. It isn't everything, but it lets us compare a Pole, a Spaniard and a German fairly.

[1:00 1990: THE STARTING LINE]
1990. Communism has just ended. Poland's figure is 12,821 dollars a person. Hungary: 21,297. Greece and Portugal: about 27,000. Germany: 42,355.
In January 1990 Poland started a fast and painful reform programme, often called shock therapy. Prices were freed, state firms lost their support, and unemployment soared. But the economy began to grow, and it kept growing.
By 2000, Poland is at 18,566 dollars.

[2:00 JOINING THE EU]
2004. Poland joins the European Union, at 20,879 dollars a person.
Membership brought three things. Access to the single market for Polish firms. Investment from western companies building factories and offices. And EU funds for roads, railways and towns.
It also brought something harder to measure: hundreds of thousands of Poles moved to work in the UK, Ireland and Germany.

[2:50 THE CRISIS THAT SKIPPED POLAND]
2008. The financial crisis hits Europe. Watch Greece: 41,709 dollars in 2008, then down to 37,567 by 2010. Spain falls too.
Poland doesn't. From 25,554 in 2008 it keeps rising, to 27,112 in 2010. In 2009, Poland was the only economy in the EU that didn't shrink.
[ON SCREEN: fact to confirm before render]

[3:40 OVERTAKING]
Now the crossings. In 2011, Poland passes Hungary. In 2015, with Greece deep in its debt crisis, Poland passes Greece. In 2020, it passes Portugal.
[ON SCREEN: each crossing highlighted with both flags]

[5:00 2025]
2025. Poland: 46,925 dollars a person, three point seven times the 1990 level. Spain: 49,318. Czechia: 49,292. Italy and the UK: about 54,000. Germany: 62,824.
Poland is at 95 percent of Spain and 75 percent of Germany.

[5:40 THE CATCHES]
But three things don't show on this line.
First, hours. The average Polish worker works about 1,807 hours a year. The average German, 1,335. Per hour worked, the gap with Germany is still much bigger.
Second, not all of Poland is catching up at the same speed. Big cities like Warsaw have pulled far ahead of the rural east.
Third, people. The UN's central projection has Poland's population falling from 38 million today to about 19 million by 2100. Fewer workers make growth harder.

[6:40 WHAT'S NEXT]
Over the last ten years, Poland's figure grew about four percent a year and Spain's under one and a half. If both kept that pace, which is a big if, Poland would pass Spain in about two years.
In just over three decades, Poland went from one of the poorest countries in Europe to the edge of its middle. Few countries anywhere have done that without oil.
Next on Terrachart: how long Europeans live, and how the south overtook the north.
"""),

dict(
    id="L04", date=date(2026, 11, 9), pillar="Society over time", fmt="Line race + coloured map over time",
    title="Life Expectancy in Europe, 1950–2023: How the South Overtook the North",
    title_b="In 1950, Spaniards Lived 10 Years Less Than Norwegians. Not Any More.",
    thumb="Map of Europe, south glowing teal. Text: THE SOUTH WINS",
    thumb_b="Spanish flag with +22 YEARS",
    length="7 min", charts="Animated map 1950–2023; line race for 12 countries; dip callout 2020–21",
    source="UN World Population Prospects 2024, via Our World in Data (life expectancy at birth)",
    link="https://ourworldindata.org/grapher/life-expectancy", licence="CC BY 4.0 (credit OWID and UN WPP)",
    data_status="Checked 2 Nov 2026",
    checks="Keep the Russia and Ukraine lines neutral. Do not show war imagery. Hedge any explanation of why the south lives longer.",
    summary="How long a newborn can expect to live in each European country, from 1950 to 2023. How Spain and Italy went from the middle of the pack to the top, the collapse in the east in the 1990s, and the pandemic dip.",
    chapters=["0:00 62 years vs 72", "0:25 What life expectancy means", "1:00 1950", "2:00 The long climb", "2:50 The east in the 1990s", "3:40 The south takes over", "4:30 The pandemic dip", "5:10 2023", "6:00 Why the south?"],
    data_note="Period life expectancy at birth: how long a baby born that year would live if death rates stayed as they were that year.",
    tags="life expectancy Europe, life expectancy by country, longest living countries, Spain life expectancy, Italy life expectancy, Switzerland life expectancy, Germany life expectancy, Eastern Europe life expectancy, health in Europe, Mediterranean diet, demography, Our World in Data, data visualisation, Terrachart",
    hashtags="#LifeExpectancy #Europe #DataVisualisation",
    music="Warm, reflective strings (Audio Library)",
    end_screen="L07 Europe's Biggest Populations (when live) or L03",
    pinned="Why do you think Spain and Italy live longer than Germany and the UK? Wrong answers welcome, data even more.",
    script="""[0:00 HOOK]
In 1950, a baby born in Spain could expect to live about 62 years. A baby born in Norway, almost 72. Today Spain is one of the longest-living countries in the world, at nearly 84. Here's how southern Europe overtook the north.

[0:25 WHAT LIFE EXPECTANCY MEANS]
Life expectancy at birth is how long a baby born in a given year would live if the death rates of that year never changed. So it isn't a forecast for one person. It's a snapshot of how healthy a country is right now. The figures come from the United Nations, through Our World in Data.

[1:00 1950]
1950. Europe as a whole: 62 years. At the top: Norway at 71.6, the Netherlands at 71.4, Sweden at 71.1. The north-west, rich and well fed after the war.
Further south and east, much lower. Italy 65.7. Spain 61.8. Bulgaria 61.5. Romania 60.5. Portugal 58.5. Albania, 44.5.
[ON SCREEN: map, north-west dark, south and east pale]

[2:00 THE LONG CLIMB]
Then the climb. Through the 1950s, 60s and 70s, almost every country adds years, fast. Fewer children die young. Vaccines and antibiotics reach everyone. Clean water and better food do the rest.
By 1990, Europe's average is 73.

[2:50 THE EAST IN THE 1990s]
But watch the east after 1990. When the Soviet Union breaks up, life expectancy in Russia falls from 69.3 in 1990 to 65.0 by 2000. Ukraine and Moldova drop too. Economic collapse, alcohol and broken health systems all played a part.
For a decade, the gap between east and west grows instead of shrinking.

[3:40 THE SOUTH TAKES OVER]
Meanwhile, the south keeps climbing. By 2019, the top three in Europe are Switzerland at 83.8, Spain at 83.5 and Italy at 83.3. Spain, which started 10 years behind Norway, is now ahead of it.

[4:30 THE PANDEMIC DIP]
Then 2020. The pandemic pushes Europe's average down from 78.8 in 2019 to 77.0 in 2021. It's the biggest fall in decades. By 2023, it has recovered, to 79.1.

[5:10 2023]
2023. Switzerland 84.0. Italy 83.7. Spain 83.7. France and Sweden 83.3.
Further down: Germany 81.4, the UK 81.3. Both below the Mediterranean.
Poland 78.6, Hungary 77.0, Romania 75.9, Bulgaria 75.6.
And at the bottom: Ukraine 73.4, Russia 73.2, Moldova 71.2.
Spain's gain since 1950: almost 22 years.

[6:00 WHY THE SOUTH?]
Researchers point to several reasons, and no single one explains it. Lower rates of heart disease. Diet. Strong family ties into old age. Health systems that reach almost everyone.
And Germany is the puzzle: one of the biggest health budgets in Europe, but two years less than Spain.
Tell us your theory in the comments. Next, we look at how many hours Europeans work. The answer will surprise anyone who believes the stereotypes.
"""),

dict(
    id="L05", date=date(2026, 11, 11), pillar="Money & life", fmt="Ranked bars + 1970 vs 2023 slope chart",
    title="Who Works the Longest Hours in Europe? (It's Not Who You Think)",
    title_b="Germans Work the Fewest Hours in Europe. Here's Why.",
    thumb="Clock icon, German flag at the bottom of a ranking. Text: GERMANY: LAST",
    thumb_b="Big number 1,335 HOURS with German flag",
    length="6–7 min", charts="Ranked bars 2023; slope chart 1970→2023 for 8 countries; small US comparison",
    source="Penn World Table, via Our World in Data (annual working hours per worker)",
    link="https://ourworldindata.org/grapher/annual-working-hours-per-worker", licence="CC BY 4.0 (credit OWID and Penn World Table)",
    data_status="Checked 2 Nov 2026",
    checks="Say on screen that countries measure hours differently, so compare trends more than exact gaps. If we mention output per hour, check it against OECD data first.",
    summary="The average hours a worker actually works in a year, across Europe. Germany comes last and Greece near the top. Why the numbers look like that: part-time work, holidays, and what an 'average worker' hides.",
    chapters=["0:00 1,335 vs 1,893", "0:25 What we're measuring", "1:00 The 2023 ranking", "2:30 Since 1970", "3:30 Why Germany is last", "4:40 Long hours, low pay?", "5:30 The US", "6:00 What it means"],
    data_note="Average hours actually worked per worker per year, including part-time workers. Countries collect this differently, so small gaps are not meaningful.",
    tags="working hours Europe, who works the most hours, hours worked per year, Germany working hours, Greece working hours, Poland working hours, work life balance Europe, part time work, productivity Europe, four day week, average working hours by country, Our World in Data, data visualisation, Terrachart",
    hashtags="#WorkLifeBalance #Europe #Work",
    music="Upbeat but light, ticking-clock feel (Audio Library)",
    end_screen="L02 Minimum Wage in Every EU Country",
    pinned="How many hours do you actually work in a normal week? (No judgement.)",
    script="""[0:00 HOOK]
Germany has a reputation for hard work. Yet the average German worker works fewer hours than anyone else in Europe: 1,335 a year. A worker in Greece puts in 1,893. That's more than 550 hours, or about fourteen extra working weeks. So who is really working hardest, and does it pay?

[0:25 WHAT WE'RE MEASURING]
These are the hours actually worked in a year by the average worker, from the Penn World Table, through Our World in Data. They include overtime, and they include people who work part-time. Countries count hours in slightly different ways, so treat small gaps with caution. The big patterns are real.

[1:00 THE 2023 RANKING]
At the top in our European countries: Croatia, at 1,974 hours. Greece, 1,893. Malta, 1,848. Cyprus, 1,840. Romania, 1,826. Poland, 1,807.
At the bottom: Sweden, 1,432. Norway, 1,412. Denmark, 1,380. And Germany, 1,335.
[ON SCREEN: ranked bars, top and bottom highlighted]

[2:30 SINCE 1970]
Now go back to 1970. Germany then: 1,972 hours, close to Greece today. In five decades, the average German's working year shrank by a third.
Greece went from 2,114 hours to 1,893: a smaller fall. Ireland, which topped this list in 1970 at 2,359 hours, came down a long way too.
Almost everywhere in Europe, working years got shorter as countries got richer.

[3:30 WHY GERMANY IS LAST]
So why is Germany at the bottom? Three reasons.
First, part-time work. Germany has one of the highest shares of part-time workers in Europe, especially among women. They pull the average down.
Second, holidays. German law guarantees at least twenty days of paid leave on a five-day week, and many contracts give thirty, plus public holidays.
Third, shorter full-time weeks in many industries, often agreed with unions.
So it's not that Germans are lazy. Many of them simply work fewer hours, and get a lot done in each one.

[4:40 LONG HOURS, LOW PAY?]
Notice who's at the top: Greece, Romania, Poland. Mostly countries where wages are lower. When each hour earns less, people work more of them. And where there's more self-employment, as in Greece, hours tend to be longer too.
[ON SCREEN: link card to our minimum wage video]

[5:30 THE US]
For comparison, the average American worker: 1,789 hours a year. That's more than 450 hours above Germany, and close to Poland.

[6:00 WHAT IT MEANS]
Long hours aren't a sign of a strong economy. Across Europe, the richer a country gets, the fewer hours its people tend to work. Part of being rich, it seems, is buying back your time.
Next on Terrachart: what Europeans pay for electricity, and the winter it all went wrong.
"""),

dict(
    id="L06", date=date(2026, 11, 14), pillar="Money & life", fmt="Line chart over time + ranked bars + bill calculator graphic",
    title="Electricity Prices in Europe, 2008–2026: Who Pays the Most?",
    title_b="Ireland Now Pays the EU's Highest Electricity Prices",
    thumb="Light bulb with two price tags. Text: 39c vs 11c",
    thumb_b="Irish flag and a lightning bolt. Text: 3× MORE",
    length="6–7 min", charts="EU average line 2008–2026 with 2022 spike; ranked bars first half 2026; yearly bill comparison",
    source="Eurostat, Electricity prices for household consumers (nrg_pc_204), band 2,500–4,999 kWh, all taxes included, updated 19 Oct 2026",
    link="https://ec.europa.eu/eurostat/databrowser/view/nrg_pc_204/default/table", licence="CC BY 4.0 (Eurostat reuse policy)",
    data_status="Checked 2 Nov 2026",
    checks="Label the yearly bill as an illustration (3,500 kWh at the average price). Mention the 2022 war in Ukraine neutrally, no war imagery.",
    summary="What households pay per kilowatt-hour across the EU, every six months from 2008 to early 2026, all taxes included. The 2022 price shock, who pays the most today, and what that means for a yearly bill.",
    chapters=["0:00 39 cents vs 11", "0:25 What we're measuring", "1:00 2008", "1:50 The 2022 shock", "3:00 Early 2026", "4:10 Your yearly bill", "4:50 Why prices differ", "5:50 What it means"],
    data_note="Household electricity prices, consumption band 2,500–4,999 kWh a year, all taxes and levies included, in euros per kWh. First half of each year unless stated.",
    tags="electricity prices Europe, energy prices Europe, electricity bill, price per kWh, Ireland electricity prices, Germany electricity prices, Hungary electricity prices, energy crisis 2022, cost of living Europe, household energy, Eurostat, data visualisation, Terrachart",
    hashtags="#EnergyPrices #Europe #CostOfLiving",
    music="Tense-to-calm electronic underscore (Audio Library)",
    end_screen="L11 Which European Countries Run on Renewables (when live) or L02",
    pinned="What do you pay per kWh where you live? Check your last bill and tell us.",
    script="""[0:00 HOOK]
A household in Ireland pays 39 cents for every kilowatt-hour of electricity. In Hungary, 11 cents. Same electricity, more than three times the price. Here's how Europe's power bills changed since 2008, including the year they exploded.

[0:25 WHAT WE'RE MEASURING]
These are Eurostat's prices for a typical household using between 2,500 and 4,999 kilowatt-hours a year, with every tax and charge included. Prices are in euros, per kilowatt-hour, every six months.

[1:00 2008]
First half of 2008. The EU average is 16 cents. Denmark is the most expensive at 26 cents, then Germany at 21. The cheapest: Bulgaria at 7 cents, Estonia and Latvia at 8.
For the next decade, prices creep up slowly. By early 2021, the EU average is 22 cents, and Germany is the most expensive, at 32.

[1:50 THE 2022 SHOCK]
Then 2022. After Russia's invasion of Ukraine, gas prices across Europe soar, and gas often sets the price of electricity. In the second half of 2022, a Danish household pays 59 cents a kilowatt-hour. Belgium 45. Italy 36.
The EU average peaks in the first half of 2023, at 29 cents. Several governments cap prices or cut taxes to soften the blow, which is why some countries barely move on this chart.
[ON SCREEN: the spike, with a short neutral label: "2022: gas price shock"]

[3:00 EARLY 2026]
Now, the first half of 2026. The EU average is still 28 cents: almost exactly where it was at the peak.
Most expensive: Ireland 39 cents, Germany 36, Belgium 36, Austria 33. Then Italy 31, Sweden 31, Poland 30.
In the middle: Spain and France at 25, the Netherlands 24, Greece 24, Portugal 24.
Cheapest: Bulgaria 13, Malta 13, and Hungary 11.

[4:10 YOUR YEARLY BILL]
What does that mean for a home using 3,500 kilowatt-hours a year? At the EU average price, about 990 euros. In Ireland, about 1,355. In Germany, about 1,266. In Hungary, about 399.
[ON SCREEN: illustration only, real bills include standing charges and differ by contract]

[4:50 WHY PRICES DIFFER]
Three things decide most of the gap.
Taxes and network charges, which in some countries make up a large share of the bill.
The energy mix: countries with lots of hydro, nuclear or wind are less exposed when gas prices jump.
And regulation: in Hungary and Bulgaria, household prices are set or capped by the state.
Cheap in euros isn't always cheap for the people paying, though. Remember the minimum wages from last week.

[5:50 WHAT IT MEANS]
Europe's electricity is still about 75 percent more expensive than in 2008, and the 2022 shock never fully went away. Where your country sits on this chart depends less on the weather than on politics and pipes.
Next on Terrachart: Europe's population, from 1950 to 2100.
"""),

dict(
    id="L07", date=date(2026, 11, 16), pillar="Society over time", fmt="Bar chart race 1950–2100 with projection shading",
    title="Europe's Biggest Populations, 1950–2100 (UN Projections)",
    title_b="The UK Could Overtake Germany's Population by 2059",
    thumb="Race frozen with a dotted 'projection' zone. Text: 1950 → 2100",
    thumb_b="UK and German flags, arrow crossing. Text: UK > GERMANY?",
    length="7 min", charts="Bar race 1950–2100, bars turn striped after 2023 (projection); line chart for UK vs Germany; Italy peak marker",
    source="UN World Population Prospects 2024, via Our World in Data (estimates to 2023, medium projection after)",
    link="https://ourworldindata.org/grapher/population-with-un-projections", licence="CC BY 4.0 (credit OWID and UN WPP)",
    data_status="Checked 2 Nov 2026",
    checks="Say every time a year after 2023 is a projection. Keep the Ukraine section factual and neutral; no war imagery. Russia is shown as the whole country.",
    summary="Europe's most populous countries from 1950 to 2100, using UN estimates and the UN's central projection. Russia stays first, Italy has already peaked, and the UK passes Germany in 2059 on the UN's numbers.",
    chapters=["0:00 The UK passes Germany?", "0:25 Estimates and projections", "1:00 1950", "2:00 2000", "2:50 2025", "3:40 2050", "4:30 2100", "5:20 Why the lines bend", "6:20 What it means"],
    data_note="UN estimates up to 2023, then the UN medium-variant projection. Projections depend on assumptions about births, deaths and migration.",
    tags="Europe population, population by country, population 2100, UN population projections, most populous countries in Europe, Germany population, UK population, France population, Italy population decline, Poland population, Ukraine population, demographics, birth rate Europe, bar chart race, data visualisation, Terrachart",
    hashtags="#Population #Europe #Demographics",
    music="Slow, spacious ambient track (Audio Library)",
    end_screen="L04 Life Expectancy in Europe",
    pinned="Do you believe the 2100 projection for your country? What would change it?",
    script="""[0:00 HOOK]
Germany has had more people than Britain for as long as anyone can remember. But on the United Nations' central projection, the UK passes Germany in 2059. Italy has already started shrinking. And Poland could lose half its people by 2100. Let's watch 150 years of Europe's population.

[0:25 ESTIMATES AND PROJECTIONS]
Up to 2023, these are the UN's estimates. After that, they're projections: the UN's middle scenario, based on assumptions about births, deaths and migration. Projections aren't predictions. They show where today's trends lead if nothing changes. We'll shade the projected years so you always know which is which.
Russia is shown as the whole country, including its Asian part.

[1:00 1950]
1950. Russia, 103 million. Germany, 70 million. The UK, 50. Italy, 46. France, 42. Ukraine, 37.

[2:00 2000]
2000. Russia, about 147 million. Germany 82. France and the UK both just under 60. Italy 57. Ukraine is shrinking already, at 50 million.

[2:50 2025]
2025. Russia 144 million. Germany 84. The UK 70. France 67. Italy 59. Spain 48. Ukraine 39. Poland 38.
Italy's population actually peaked in 2014, at 60.7 million. It has been falling since.

[3:40 2050]
Now we're in projection territory. 2050. Germany down to 78 million, the UK up to 76. France 68. Italy 52.

[4:30 2100]
2100. Russia 126 million. And in second place, the UK, at 74 million. Germany 71. France 68. Then a long drop: Italy 35. Spain 33. Poland 19. Ukraine 15.
On these numbers, the UK passes Germany in 2059.
[ON SCREEN: crossing point highlighted, "UN medium projection"]

[5:20 WHY THE LINES BEND]
Two forces decide all of this.
Births. In almost every European country, women have fewer than the 2.1 children per woman needed to keep a population stable without migration.
And migration. The UK and France have had higher birth rates than Germany, and both have had steady immigration. That's what keeps them up. Italy, Spain and Poland combine very low birth rates with less immigration, or with emigration.
For Ukraine, war and emigration since 2022 have changed the numbers sharply, and the long-term projection is especially uncertain.

[6:20 WHAT IT MEANS]
A smaller population isn't a disaster by itself. But fewer young people paying for more older people is a challenge every country on this chart will face.
Next: 70 years of Europe's biggest club trophy, in one race.
"""),
]
