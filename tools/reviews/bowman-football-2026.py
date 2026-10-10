"""Add the 2026 Bowman Football deep review to the master page (idempotent)."""
import json, re
import os
P = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'src/index.src.html')
s = open(P).read()

REVIEW = {
 "kind": "Review", "n": "2026 Bowman Football", "when": "Out now · reviewed Oct 9", "score": "6.7",
 "facts": [
  "Hobby: 20 packs of 8, 2 autographs. $309.99 at Fanatics, $389 median on eBay (118 sold, Sep 30 to Oct 9)",
  "Jumbo: 4 autographs, $660 median on eBay. First Day Issue about $1,035, down from $1,399 presale",
  "401-card checklist: 100 NFL base, 100 NFL rookies, 201 college prospects in paper and Chrome",
  "Case hits (Anime, GPK, Crystallized, Spotlights, Etched) average 1 per 23 hobby boxes",
  "Arch Manning's only autograph is the Chrome Prospect Auto. Most week-one copies are redemptions"
 ],
 "bars": [["Rookie class", 7.0], ["Hit quality", 7.5], ["Print run", 5.0], ["Price vs. value", 5.5]],
 "deep": {
  "lede": "The first Bowman Football with college and NFL players in one box. The NFL rookie half is the weakest part: the No. 1 pick has not taken a regular-season snap, and no rookie quarterback is starting. The college half is what people are paying for. Every price below is an eBay sold median from Sep 30 to Oct 9, with the sale count in parentheses, and our take on whether the price makes sense.",
  "sections": [
   {"h": "Tier 1 · The cards that carry the product", "items": [
    {"c": "Arch Manning Chrome Prospect Autograph #BCPA-AMA", "p": "Base $770 (11) · Refractor /499 $860 (10) · Blue /150 $1,100 to $1,750 · Green /99 $960 to $1,200 · Gold /50 $4,255 to $6,000 · Orange /25 $3,500 to $5,000 · Black /10 $9,500 and $13,500 · Red /5 $22,000",
     "w": "His only autograph in the set, under a Topps exclusive, a candidate for the No. 1 pick in 2027, and third in the Heisman odds after Texas came back from 20 down to beat Ohio State. It is the most liquid high-end card in the product. Two cautions: most week-one copies are redemptions, so price in the wait and the small risk Topps swaps it, and the base-to-Gold ladder is already steep. The Refractor /499 at $860 is the sane entry; the numbered colors under /50 are trophy pricing."},
    {"c": "Arch Manning 1st Bowman Chrome #ALT-1 (no auto)", "p": "Blue /150 $240 (6) · Green /99 $235 (7) · Purple /75 $275 (4) · Gold /50 $900 to $1,500 · Orange /25 $700 to $1,200 · Black /10 $1,300 and $2,750 · Red /5 $2,225",
     "w": "The ALT-1 number is a short print. No unnumbered base or Refractor sales showed up in week one, only the colors. The Blue /150 and Green /99 around $240 are the cheapest way to own his first Bowman Chrome, and the one we would grade: raw copies at $240 against numbered-parallel demand is the kind of spread the calculator likes once a PSA 10 comp exists."},
    {"c": "Arch Manning Anime NIL and GPK", "p": "Anime $1,500 to $4,000, median about $2,800 (7) · GPK $1,975 to $10,000, median about $2,750 (9)",
     "w": "His only case hits. Both are unnumbered base inserts selling at four figures, which is the product's print run talking: one case hit per 23 hobby boxes across 130 or so cards in the five families. If you pull one, sell into week-two demand rather than holding; these fall as cases get ripped."},
    {"c": "CJ Carr Chrome Prospect Autograph and Anime", "p": "Auto base $255 (19) · Refractor /499 $305 (12) · Green /99 $600 (6) · Gold /50 $1,100 (4) · Orange /25 $950 to $1,000 · Red /5 $2,500 · Anime base $1,200 · Anime Black /10 $2,700 · Anime Red /5 $15,000",
     "w": "Notre Dame's quarterback is the second name in the set, with six autograph sets including the Joe Montana dual. His Anime Red /5 at $15,000 is the biggest public sale of the release. The base auto at $255 is a third of Manning's for a player with a real shot at the same 2027 draft board; that is the better risk-reward buy."},
    {"c": "Veteran case hits: Brady, Mahomes, Allen, Caleb Williams", "p": "Brady Anime $4,200 to $7,800 (4) · Brady GPK 'Bejeweled Brady' $3,425 and $3,949 · Mahomes Anime $2,500 and $2,900 · Allen GPK $4,400 · Caleb Williams Anime $1,500 to $2,800 (9) · Lamar Anime $1,250 and $1,800",
     "w": "Mahomes and Lamar do not sign in this product, so the case hits are their only chase cards. Brady appears in Anime, GPK and Spotlights and leads every family. These are the cards that make a $389 box defensible: one per 23 boxes at a $1,200 median across all case hits is about $52 of expected value per box."}
   ]},
   {"h": "Tier 2 · College quarterbacks with momentum", "items": [
    {"c": "Darian Mensah, Miami · Chrome Prospect Auto", "p": "Base $250 (4) · Green /99 $275 (7) · Blue /150 $228 (5) · Gold /50 $375 (4) · Orange /25 $450 (4) · Black /10 $1,300 and $2,500",
     "w": "Miami opened the season unbeaten and he led the Heisman odds in September, and the market has noticed: his base auto trades level with CJ Carr. He is draft-eligible and productive, which is the profile that holds value into the spring. Fair at $250, not cheap."},
    {"c": "Drew Mestemaker, North Texas · Chrome Prospect Auto", "p": "Base $168 (7) · Refractor /499 $205 (11) · Green /99 $250 (8) · Blue /150 $433 (3) · Gold /50 $600 · Orange /25 $749",
     "w": "The sleeper of the release. A Group of Five passer out-selling most Power Four names and every NFL rookie except Mendoza. Eleven Refractor /499 sales at $205 is real liquidity. Buy the unnumbered Refractor, not the colors; the colors are already pricing in a breakout."},
    {"c": "Jaron-Keawe Sagapolutele, Cal · Chrome Prospect Auto", "p": "Base $111 (3) · Blue Mojo /150 $150 (10) · Green /99 $120 (7) · Gold /50 $250 (5) · Orange /25 $625 (4) · Anime $1,499",
     "w": "Five autograph sets and a spot in every case-hit family, so Topps built him as a pillar. The price is a third of Mensah's for similar draft timing. Good value at base or Blue Mojo."},
    {"c": "Bear Bachmeier, BYU · Chrome Prospect Auto", "p": "Base $110 (14) · Green /99 $152 (7) · Blue Mojo /150 $225 (7) · Gold /50 $275 (5) · Orange /25 $293 and $750",
     "w": "Fourteen base auto sales in nine days is the deepest liquidity in the college tier after Carr. The Steve Young dual is the lottery ticket; the base auto at $110 is the sensible buy."},
    {"c": "Jared Curtis, Georgia · Chrome Prospect Auto and GPK", "p": "Auto base $102 (6) · Green /99 $150 (7) · Gold /50 $404 · Red /5 $1,600 · GPK 'Commodore Curtis' $2,500 and $3,200",
     "w": "A freshman with a GPK case hit selling at $2,500-plus says the demand is for the name and the school. Fine at $100 as a two-year hold; do not chase the colors."}
   ]},
   {"h": "Tier 3 · NFL rookies, where the value is uneven", "items": [
    {"c": "Fernando Mendoza, Raiders · Chrome Rookie Auto #BCRA-FM", "p": "Base $560 (23, range $500 to $810) · Refractor /499 $710 (5) · Green Mojo /99 $777 (9) · Green /99 $900 (4) · Gold /50 $1,250 · Orange /25 about $2,500 · Etched in Glass variation $700 (4)",
     "w": "The No. 1 pick, and the most expensive rookie auto by a factor of five. He has zero regular-season snaps through Week 4 behind Kirk Cousins on a 3-1 team. That is a draft-slot premium with no production under it. If Cousins holds the job all season, $560 looks heavy by December; if Mendoza starts and plays well, it is cheap. We would wait for the first start rather than pay the premium now."},
    {"c": "Jeremiyah Love, Cardinals · Chrome Rookie Auto #BCRA-JLO", "p": "Base $98 (19) · Blue Mojo /150 $225 (8) · Green /99 $215 (3) · FDI /14 $724 · Black Mojo /10 $900",
     "w": "No. 2 in NFL.com's quarter-season rookie rankings (223 yards, 2 TDs) and the consensus 1.01 in dynasty formats, at a fifth of Mendoza's price. The ankle he tweaked in Week 4 is the risk. Best value among the NFL rookies."},
    {"c": "Carnell Tate, Titans · Chrome Rookie Auto #BCRA-CT", "p": "Base $65 (13) · Blue /150 $205 (5) · Green /99 $140 (5) · Gold /50 $475 · Orange /25 $600 · Black /10 $760 · Anime $2,500",
     "w": "Ranked No. 3 among rookies after a 145-yard Week 4, 268 yards on the season, and his base auto is $65. That is the mispriced card in the rookie tier. Buy base autos and Refractors."},
    {"c": "Jordyn Tyson, Saints · Chrome Rookie Auto #BCRA-JT", "p": "Base $40 (18) · Green Refractor /99 $185 (3) · Anime Black /10 $1,676",
     "w": "A top-10 pick receiver at $40. New Orleans is not the offense you want him in, but at this price it is a cheap call option on a top-10 pick."},
    {"c": "Ty Simpson, Rams · Chrome Rookie Auto #BCRA-TS", "p": "Base $95 (20) · Blue /150 $255 (5) · Gold /50 $375 (5) · Orange /25 $650 · FDI /14 $1,095 · Anime $1,300 to $1,775",
     "w": "Drafted to sit behind Matthew Stafford, so this is a 2027 or 2028 story. The Mendoza-Simpson dual and the Anime are the chases; the base auto is a patient hold, not a flip."},
    {"c": "Caleb Downs, Cowboys · Chrome Rookie Auto #BCRA-CDO", "p": "Base $99 (18) · Refractor /499 $180 (7) · Gold /50 $900 (4) · Black /10 $999 · Red /5 $1,000",
     "w": "A safety at $99 base is the Cowboys premium at work. Fine for team collectors; the colors are expensive for a non-skill position."},
    {"c": "Jacob Rodriguez, Dolphins · Chrome Rookie Auto #BCRA-JRO", "p": "Base $102 (46) · Green /99 $220 (10) · Gold /50 $386 (7) · Black /10 $544 to $700 · Red Mojo /5 $3,000",
     "w": "The surprise of the release: a second-round linebacker is the most-traded rookie auto in the product by volume, with 46 base sales. His selection was front-page news in Mexico (he is of Mexican descent), and that collector base is where the demand is coming from. Liquidity is real; treat it as a flip into that demand rather than a hold."},
    {"c": "Drew Allar, Steelers · Chrome Rookie Auto #BCRA-DA", "p": "Base $60 (14) · Gold /50 $300 (7) · Gold Mojo /50 $499 (4) · Black Mojo /10 $2,000 and $2,500 · Red /5 $1,600 and $4,000 · Superfractor 1/1s $6,800, $7,500 and $19,998",
     "w": "The base auto is $60 and the one-of-ones sold for up to $20,000. That gap is Steelers collectors paying for scarcity, not for a rookie quarterback who has yet to show anything in the NFL. Sell colors into it; do not buy them."},
    {"c": "Kenyon Sadiq, Jets · Chrome Rookie Auto #BCRA-KS", "p": "Base $60 (18) · Green /99 $300 (6) · Orange /25 $300",
     "w": "A 7-catch, 105-yard Week 3 has him at No. 7 in the rookie rankings. Tight ends rarely carry card value, so the $60 base is about right; the Green /99 at $300 is not."}
   ]}
  ],
  "avoid": [
   "Mendoza above $600 until he starts a game. The premium is the draft slot, and the slot does not throw passes.",
   "Cade Klubnik autos ($26 base): the Jets have 23 autographs in the set, the most of any NFL team, and a $26 base says the market has no conviction.",
   "Cam Coleman at $73 base. He was pitched as the best non-quarterback card and the market disagrees; wait for it to fall under $50 or for a 2027 draft-stock jump.",
   "Bryce Underwood and LaNorris Sellers autos as flips. Nine and 22 sales respectively, base autos at $65 to $130. The Brady dual and the Future Script 1/1 are their only real chases.",
   "Standard inserts (Rockstar Rookies, Gen Next, Talent Tracker, Verified, VIP) and paper base. Mendoza and Carr paper base cards sell for $3.",
   "Hobby boxes above $400. Two autographs where 57% come from a 97-name rookie list and the long tail of that list sells for $10 to $40. Jumbo at $660 for four autographs is the better per-auto price if you must rip."
  ],
  "notes": [
   "Not in the set: Jeremiah Smith and Julian Sayin. Ohio State's college slot is Bo Jackson with two autographs. Mahomes and Lamar Jackson do not sign.",
   "Redemptions: almost every Arch Manning auto listed in week one is a redemption card. Topps redemption fulfilment runs months. Factor that into any price above $1,000.",
   "Exclusives by format: hobby Mini-Diamond Refractor; Jumbo Gridiron /125 and X-Fractors; Breaker Delight Geometric; Mega Mojo (Rose Gold Mojo 1/1); Blaster and Mega FireFractor /3; First Day Issue autos /14 and parallels /8.",
   "Rarest autographs by odds: Dual Cross Sport (Burrow/Skenes, Stafford/Edwards, Vince Young/Durant) about 1 per 265 cases; 1955 All American auto variations (Sanders, Young, Marino, Lewis, Emmitt) about 1 per 345 cases, a Red /5 sold at $5,555; Dual NIL (Brady/Underwood, Montana/Carr, Young/Bachmeier) about 1 per 413 cases. No public sales of the duals yet.",
   "Verdict: rip only for the case hits and only at jumbo or MSRP hobby pricing. Otherwise buy singles: Manning Refractor /499 auto or ALT-1 colors, Carr base auto, Mensah and Mestemaker Refractors, Tate and Love base autos."
  ],
  "src": "Prices: eBay sold listings Sep 30 to Oct 9, 2026, medians with counts. Odds and checklist: Cardsmiths Breaks, Checklist Insider, Topps Ripped, CardHitlist. Player context: NFL.com quarter-season rookie rankings, RotoWire, Sports Illustrated Heisman odds (Sep 13)."
 }
}

MARK = '/* bowman-fb-2026 */'
# 1) data: insert as the first REVIEWS entry (replace if present)
entry = ' ' + MARK + json.dumps(REVIEW, ensure_ascii=False, separators=(',', ':')) + ',\n'
if MARK in s:
    s = re.sub(r' ' + re.escape(MARK) + r'.*?\n', entry, s, count=1, flags=re.S)
else:
    s = s.replace('var REVIEWS=[\n', 'var REVIEWS=[\n' + entry, 1)

# 2) renderer: add the deep section
old = """'<div class="bars">'+r.bars.map(function(b){return "<span>"+b[0]+'</span><span class="bar"><i style="width:'+(b[1]*10)+'%"></i></span><span class="mono">'+b[1].toFixed(1)+"</span>"}).join("")+'</div></article>';
  }).join("");
}"""
new = """'<div class="bars">'+r.bars.map(function(b){return "<span>"+b[0]+'</span><span class="bar"><i style="width:'+(b[1]*10)+'%"></i></span><span class="mono">'+b[1].toFixed(1)+"</span>"}).join("")+'</div>'+reviewDeep(r.deep)+'</article>';
  }).join("");
}
function reviewDeep(d){
  if(!d)return "";
  var h='<details class="review-deep"><summary>Full breakdown: who to chase and what they are selling for</summary>';
  h+='<p class="deep-lede">'+esc(d.lede)+'</p>';
  (d.sections||[]).forEach(function(sec){
    h+='<h4>'+esc(sec.h)+'</h4><ul class="chase">'+sec.items.map(function(it){return '<li><b>'+esc(it.c)+'</b><span class="chase-p">'+esc(it.p)+'</span><p>'+esc(it.w)+'</p></li>'}).join("")+'</ul>';
  });
  if(d.avoid&&d.avoid.length)h+='<h4>What to skip</h4><ul class="chase skip">'+d.avoid.map(function(t){return '<li><p>'+esc(t)+'</p></li>'}).join("")+'</ul>';
  if(d.notes&&d.notes.length)h+='<h4>Notes</h4><ul class="chase notes">'+d.notes.map(function(t){return '<li><p>'+esc(t)+'</p></li>'}).join("")+'</ul>';
  if(d.src)h+='<p class="src">'+esc(d.src)+'</p>';
  return h+'</details>';
}"""
if 'function reviewDeep' not in s:
    assert s.count(old) == 1, s.count(old)
    s = s.replace(old, new)

# 3) CSS
css = """.review-deep{border-top:1px solid var(--line);padding-top:12px;font-size:13.5px;color:var(--ink-2)}
.review-deep summary{cursor:pointer;font-weight:600;color:var(--ink);list-style:none;display:flex;gap:8px;align-items:baseline}
.review-deep summary::-webkit-details-marker{display:none}
.review-deep summary::before{content:"+";font-family:var(--mono);color:var(--gold-ink);flex:none}
.review-deep[open] summary::before{content:"–"}
.review-deep .deep-lede{margin:12px 0 0;line-height:1.55}
.review-deep h4{margin:18px 0 8px;font-size:11.5px;letter-spacing:.07em;text-transform:uppercase;color:var(--ink-3)}
.chase{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:12px}
.chase li{padding-left:14px;position:relative;line-height:1.5}
.chase li::before{content:"";position:absolute;left:0;top:.68em;width:6px;height:2px;background:var(--gold-ink)}
.chase b{display:block;color:var(--ink)}
.chase .chase-p{display:block;font-family:var(--mono);font-size:11.5px;color:var(--gold-ink);margin-top:2px;line-height:1.5}
.chase p{margin:4px 0 0}
.chase.skip li::before,.chase.notes li::before{background:var(--ink-3)}
.review-deep .src{font-family:var(--mono);font-size:11px;color:var(--ink-3);margin:16px 0 0;line-height:1.5}
.review:has(.review-deep[open]){grid-column:1/-1}
"""
if '.review-deep{' not in s:
    s = s.replace('.reviews{display:grid;', css + '.reviews{display:grid;', 1)

open(P, 'w').write(s)
print('ok', len(s))
