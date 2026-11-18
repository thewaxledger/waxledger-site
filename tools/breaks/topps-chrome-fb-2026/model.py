# 2026 Topps Chrome Football team-break model. Checklist: Topps checklist via degreegrading.com / hobbymonitor.com (Nov 17, 2026).
# Official 2026 pack odds were not published when this ran; odds use 2025 Topps Chrome Football pack odds (Checklist Insider) as a proxy.
import json, math, os, sys
from collections import defaultdict
OUT = sys.argv[1]
NAMES = dict(ARI='Cardinals', ATL='Falcons', BAL='Ravens', BUF='Bills', CAR='Panthers', CHI='Bears', CIN='Bengals', CLE='Browns', DAL='Cowboys', DEN='Broncos', DET='Lions', GB='Packers', HOU='Texans', IND='Colts', JAX='Jaguars', KC='Chiefs', LV='Raiders', LAC='Chargers', LAR='Rams', MIA='Dolphins', MIN='Vikings', NE='Patriots', NO='Saints', NYG='Giants', NYJ='Jets', PHI='Eagles', PIT='Steelers', SF='49ers', SEA='Seahawks', TB='Buccaneers', TEN='Titans', WAS='Commanders')

def P(s):  # "TEAM: a, b; TEAM: c" -> [(player, team)]
    out = []
    for part in s.strip().split(';'):
        if not part.strip(): continue
        t, ps = part.split(':')
        out += [(p.strip(), t.strip()) for p in ps.split(',') if p.strip()]
    return out

BASE_RC = P("""ARI: Carson Beck, Jeremiyah Love, Reggie Virgil; ATL: Zachariah Branch, Avieon Terrell, Harold Perkins Jr.; BAL: Ja'Kobi Lane, Elijah Sarratt, Zion Young;
BUF: Skyler Bell, T.J. Parker, Davison Igbinosun; CAR: Chris Brazzell II, Lee Hunter, Will Lee III; CHI: Zavion Thomas, Sam Roush, Dillon Thieneman;
CIN: Colbie Young, Cashius Howell, Tacario Davis; CLE: Taylen Green, KC Concepcion, Denzel Boston, Emmanuel McNeil-Warren; DAL: Malachi Lawrence, Jaishawn Barham, Caleb Downs;
DEN: Jonah Coleman, Justin Joly, Dallen Bentley; DET: Kendrick Law, Derrick Moore, Keith Abney II; GB: Chris McClellan, Dani Dennis-Sutton, Brandon Cisse;
HOU: Marlin Klein, Keylan Rutledge, Kayden McDonald; IND: Deion Burks, CJ Allen, A.J. Haulcy; JAX: Josh Cameron, Nate Boerkircher, Albert Regis;
KC: Garrett Nussmeier, Emmett Johnson, Peter Woods, Mansoor Delane; LV: Fernando Mendoza, Mike Washington Jr., Jermod McCoy; LAC: Brenen Thompson, Akheem Mesidor, Genesis Smith;
LAR: Ty Simpson, CJ Daniels, Max Klare; MIA: Caleb Douglas, Jacob Rodriguez, Chris Bell; MIN: Demond Claiborne, Caleb Banks, Jake Golday;
NE: Behren Morton, Eli Raridon, Caleb Lomu; NO: Jordyn Tyson, Bryce Lance, Christen Miller; NYG: Malachi Fields, Francis Mauigoa, Arvell Reese, Colton Hood;
NYJ: Cade Klubnik, Omar Cooper Jr., Kenyon Sadiq, David Bailey; PHI: Cole Payton, Makai Lemon, Eli Stowers; PIT: Drew Allar, Germie Bernard, Daylen Everette;
SF: Kaelon Black, De'Zhaun Stribling, Romello Height; SEA: Jadarian Price, Julian Neal, Bud Clark; TB: Ted Hurst, Rueben Bain Jr., Josiah Trotter;
TEN: Nick Singleton, Carnell Tate, Keldric Faulk; WAS: Kaytron Allen, Antonio Williams, Sonny Styles""")
NO_RVA = {'Lee Hunter', 'Jonah Coleman', 'Chris McClellan', 'Omar Cooper Jr.', 'Eli Stowers', 'Julian Neal', 'Bud Clark', 'Josiah Trotter'}
RVA = [(p, t) for p, t in BASE_RC if p not in NO_RVA]
assert len(BASE_RC) == 100 and len(RVA) == 92

AUTOS = {
 '1991 Topps Autographs': P("""LV: Brock Bowers, Fernando Mendoza; DEN: Bo Nix; CAR: Bryce Young; SF: Christian McCaffrey; TEN: Carnell Tate, Cam Ward; CHI: Caleb Williams; TB: Emeka Egbuka;
   NYJ: Garrett Wilson; BUF: James Cook; NYG: Jaxson Dart; WAS: Jayden Daniels; DET: Jared Goff; ARI: Jeremiyah Love; CIN: Ja'Marr Chase; NO: Jordyn Tyson, Tyler Shough; CLE: Quinshon Judkins;
   SEA: Sam Darnold; LAR: Ty Simpson; KC: Xavier Worthy"""),
 'Base Variation Autographs': P("""LV: Ashton Jeanty, Brock Bowers, Dont'e Thornton Jr.; MIN: Aaron Jones Sr., Jordan Addison, Justin Jefferson; IND: Alec Pierce, Daniel Jones, Tyler Warren; NYJ: Breece Hall;
   DEN: Bo Nix, Pat Surtain II, RJ Harvey; SF: Brock Purdy, Christian McCaffrey, Fred Warner, Kyle Juszczyk; JAX: Bhayshul Tuten, Brian Thomas Jr., Trevor Lawrence; CAR: Bryce Young, Tetairoa McMillan;
   CIN: Chase Brown, Joe Burrow; DAL: CeeDee Lamb, Dak Prescott, Javonte Williams; CHI: Colston Loveland, Caleb Williams, Luther Burden III; NO: Chris Olave, Taysom Hill, Tyler Shough;
   MIA: Chop Robinson, De'Von Achane; TEN: Calvin Ridley, Cam Ward, Elic Ayomanor; CLE: Carson Schwesinger, Quinshon Judkins; BAL: Derrick Henry, Kyle Hamilton, Roquan Smith;
   BUF: Dawson Knox, Josh Allen, Keon Coleman; ATL: Drake London, Jalon Walker, Tua Tagovailoa; NE: Drake Maye, TreVeyon Henderson; GB: Edgerrin Cooper, Matthew Golden; TB: Emeka Egbuka, Tez Johnson;
   WAS: Jacory Croskey-Merritt, Jayden Daniels, Terry McLaurin; NYG: Jaxson Dart, Malik Nabers; DET: Jahmyr Gibbs, Jared Goff; LAC: Justin Herbert, Ladd McConkey, Omarion Hampton;
   HOU: Jayden Higgins, Kamari Lassiter, Woody Marks; PHI: Jalen Hurts, Saquon Barkley; SEA: Jaxon Smith-Njigba; PIT: Kaleb Johnson, T.J. Watt, Will Howard; LAR: Kyren Williams, Matthew Stafford, Puka Nacua;
   KC: Kenneth Walker III, Patrick Mahomes II, Xavier Worthy; ARI: Michael Wilson"""),
 'Chrome Legends Autographs': P("""ARI: Anquan Boldin, Kurt Warner; LAC: Antonio Gates; HOU: Andre Johnson; NO: Archie Manning; CIN: Boomer Esiason; MIA: Bob Griese; LV: Bo Jackson, Howie Long;
   CLE: Bernie Kosar, Joe Thomas; DET: Barry Sanders; PHI: Brian Westbrook, Eric Allen; DAL: Dez Bryant, DeMarco Murray; WAS: DeAngelo Hall, John Riggins; KC: Dante Hall; NYJ: Darrelle Revis;
   LAR: Eric Dickerson; NYG: Eli Manning; SF: Frank Gore, Jerry Rice; DEN: John Elway, Steve Atwater; CHI: Jim McMahon, William Perry; SEA: Kam Chancellor, Richard Sherman; GB: LeRoy Butler, Sterling Sharpe;
   BUF: LeSean McCoy, Thurman Thomas; TB: Mike Alstott, Warren Sapp; JAX: Maurice Jones-Drew; ATL: Michael Vick, Tony Gonzalez; IND: Peyton Manning; NE: Rob Gronkowski, Tom Brady;
   BAL: Ray Lewis, Terrell Suggs; MIN: Randy Moss; PIT: Rod Woodson, Troy Polamalu; TEN: Warren Moon"""),
 'Chromographs': P("""MIN: Aaron Jones Sr.; NO: Alvin Kamara; PIT: Aaron Rodgers; DET: Amon-Ra St. Brown; NYJ: Breece Hall; SF: Brock Purdy; JAX: Brian Thomas Jr.; DAL: CeeDee Lamb; TEN: Carnell Tate;
   ATL: Drake London; WAS: Deebo Samuel; TB: Emeka Egbuka; LV: Fernando Mendoza, Maxx Crosby; CIN: Joe Burrow; GB: Josh Jacobs; ARI: Jeremiyah Love; IND: Jonathan Taylor; CHI: Luther Burden III;
   PHI: Makai Lemon; LAR: Matthew Stafford, Ty Simpson; HOU: Nico Collins; BAL: Zay Flowers"""),
 'Class of 26 Autographs': P("NE: Adam Vinatieri; NO: Drew Brees; ARI: Larry Fitzgerald; CAR: Luke Kuechly; SF: Roger Craig"),
 'Future Stars Autographs': P("""LV: Ashton Jeanty; CHI: Colston Loveland, Luther Burden III; CLE: Carson Schwesinger, Quinshon Judkins; TEN: Cam Ward; TB: Emeka Egbuka; PHI: Jihaad Campbell; NYG: Jaxson Dart;
   HOU: Jayden Higgins, Woody Marks; GB: Matthew Golden; LAC: Omarion Hampton; DEN: RJ Harvey; NE: TreVeyon Henderson; CAR: Tetairoa McMillan; NO: Tyler Shough; IND: Tyler Warren"""),
 'Hall of Chrome Autographs': P("""CIN: Anthony Munoz; WAS: Art Monk; PHI: Brian Dawkins; TEN: Bruce Matthews; MIN: Cris Carter; LAC: Dan Fouts; MIA: Dan Marino; ATL: Deion Sanders; IND: Edgerrin James;
   PIT: Jerome Bettis; BUF: Jim Kelly; GB: James Lofton; SF: Joe Montana; BAL: Jonathan Ogden; LAR: Kurt Warner; NYG: Lawrence Taylor; DAL: Michael Irvin; CHI: Mike Singletary; CLE: Ozzie Newsome;
   SEA: Steve Largent; JAX: Tony Boselli; LV: Tim Brown; DEN: Terrell Davis; NE: Ty Law; TB: Warren Sapp"""),
 'Ring of Honor Autographs': P("BAL: Joe Flacco; SEA: Malcolm Smith; NE: Tom Brady, Tom Brady; DEN: Von Miller"),
 'Tecmo Autographs': P("""WAS: Art Monk; BUF: Cornelius Bennett; KC: Christian Okoye; BAL: Derrick Henry; NE: Drake Maye; CIN: Joe Burrow; MIN: Justin Jefferson; SF: Jerry Rice; LAR: Myles Garrett;
   PIT: Rod Woodson; GB: Sterling Sharpe; DAL: Troy Aikman; TEN: Warren Moon; CHI: William Perry"""),
}
DUALS = [("Ja'Marr Chase", 'CIN', 'Joe Burrow', 'CIN'), ('Carson Beck', 'ARI', 'Jeremiyah Love', 'ARI'), ('Denzel Boston', 'CLE', 'KC Concepcion', 'CLE'), ('Sam Darnold', 'SEA', 'Jaxon Smith-Njigba', 'SEA'),
 ('Amon-Ra St. Brown', 'DET', 'Jahmyr Gibbs', 'DET'), ('Saquon Barkley', 'PHI', 'Jalen Hurts', 'PHI'), ('Tom Brady', 'NE', 'Drake Maye', 'NE'), ('Fernando Mendoza', 'LV', 'Ty Simpson', 'LAR'),
 ('Bo Nix', 'DEN', 'John Elway', 'DEN'), ('Tony Romo', 'DAL', 'Dak Prescott', 'DAL'), ('Brock Purdy', 'SF', 'Steve Young', 'SF'), ('Arvell Reese', 'NYG', 'Caleb Downs', 'DAL'),
 ('Tyler Shough', 'NO', 'Drew Brees', 'NO'), ('Carnell Tate', 'TEN', 'Jordyn Tyson', 'NO'), ('Breece Hall', 'NYJ', 'Garrett Wilson', 'NYJ'), ('Tetairoa McMillan', 'CAR', 'Bryce Young', 'CAR')]
GOLD_SHIELD = P("CLE: Carson Schwesinger; SEA: Jaxon Smith-Njigba; LAR: Myles Garrett, Matthew Stafford; CAR: Tetairoa McMillan")
RETAIL_RRA = P("""CLE: Aaron Anderson, Joe Royer, Spencer Fano; TEN: Anthony Hill Jr.; WAS: Athan Kaliakmanis, Robert Henry Jr.; BAL: Adam Randall, Josh Cuevas; DAL: Anthony Smith, LT Overton, Michael Trigg;
   DET: Blake Miller, Luke Altmyer; KC: Cyrus Allen; ARI: Chase Bisontis; IND: Caden Curry, Seth McGowan; MIN: Caleb Tiernan; GB: Domani Jackson; PHI: Deontae Lawson; NYJ: D'Angelo Ponds;
   SEA: Emmanuel Henderson Jr.; SF: Ephesians Prysock; LAC: Isaiah World, Jake Slaughter; TB: Jalon Daniels; CIN: Jack Endries; BUF: Jalon Kilgore, Zane Durant; JAX: J'Mari Taylor, Tanner Koziol;
   MIA: Kevin Coleman Jr.; HOU: Lewis Bond, Noah Whittington; PIT: Lake McRee; CAR: Monroe Freeling, Zakee Wheatley; CHI: Miller Moss, Malik Muhammad; NO: Oscar Delp; LV: Roman Hemby; LAR: Tim Keenan III; DEN: Taurean York""")
PATCH = P("""CIN: Andrei Iosivas, Chase Brown, Amarius Mims, Kris Jenkins; LV: Aidan O'Connell, Michael Mayer, Tre Tucker, Brock Bowers; IND: Anthony Richardson, Josh Downs, Anthony Gould;
   DAL: Brandon Aubrey, Luke Schoonmaker, Brevyn Spann-Ford, Cooper Beebe, Marist Liufau, Tyler Guyton; DET: Brian Branch, Jahmyr Gibbs, Sam LaPorta; ATL: Bijan Robinson, Michael Penix Jr.;
   JAX: Brenton Strange, Parker Washington, Tank Bigsby, Brian Thomas Jr., Cam Little; CAR: Bryce Young, Jonathan Mingo, Jalen Coker, Ja'Tavion Sanders, Xavier Legette;
   NE: Christian Gonzalez, Kayshon Boutte, Drake Maye, Ja'Lynn Polk, Joe Milton III; HOU: CJ Stroud, Henry To'oTo'o, Will Anderson Jr., Calen Bullock, Cade Stover; CLE: Cedric Tillman;
   BUF: Dalton Kincaid, Cole Bishop, Keon Coleman; GB: Dontayvion Wicks, Luke Musgrave, Lukas Van Ness, Edgerrin Cooper, Javon Bullard, MarShawn Lloyd; MIA: De'Von Achane, Malik Washington;
   SEA: Devon Witherspoon, Jaxon Smith-Njigba, Zach Charbonnet, Byron Murphy II, George Holani; PIT: Darnell Washington, Payton Wilson; MIN: Jordan Addison, Dallas Turner, Will Reichard;
   PHI: Jalen Carter, Jeremiah Trotter, Will Shipley; SF: Jake Moody, Jacob Cowing; LAR: Kobie Turner, Puka Nacua, Blake Corum, Joshua Karty, Jared Verse, Kamren Kinchens;
   DEN: Marvin Mims Jr., Audric Estime, Bo Nix; ARI: Michael Wilson, Trey Benson; LAC: Quentin Johnston, Joe Alt, Junior Colson, Ladd McConkey; CHI: Roschon Johnson, Tyson Bagent, Caleb Williams, Rome Odunze;
   KC: Rashee Rice, Xavier Worthy; TEN: Tyjae Spears, Will Levis, T'Vondre Sweat; BAL: Zay Flowers, Nate Wiggins; NYJ: Braelon Allen; TB: Bucky Irving, Chris Braswell, Graham Barton, Jalen McMillan;
   WAS: Jayden Daniels, Luke McCaffrey, Mike Sainristil; NO: Spencer Rattler; NYG: Theo Johnson, Tyrone Tracy Jr.""")
assert len(PATCH) == 106, len(PATCH)
# Hobby short-print inserts (grouping per Haus of Sports Cards; Topps has not labelled SSPs). mult = rarity weight in the value model.
SSP = {
 'Kaiju': (5, P("BAL: Lamar Jackson; DAL: Dak Prescott; DEN: Bo Nix; TEN: Carnell Tate; NE: Drake Maye; TB: Tom Brady; MIN: Justin Jefferson; LAR: Myles Garrett; LV: Fernando Mendoza; ARI: Jeremiyah Love")),
 'Super Bowl at Night': (3, P("NE: Drake Maye, TreVeyon Henderson, Rhamondre Stevenson, Mack Hollins, Hunter Henry, Robert Spillane, Christian Gonzalez; SEA: Sam Darnold, Kenneth Walker III, Jaxon Smith-Njigba, Cooper Kupp, AJ Barner, Uchenna Nwosu, Devon Witherspoon, Nick Emmanwori")),
 'Helix': (2, P("ARI: Jeremiyah Love; BUF: Josh Allen; CAR: Bryce Young; DAL: Dak Prescott; DET: Amon-Ra St. Brown; GB: Brett Favre; LAR: Matthew Stafford, Ty Simpson; NE: Drake Maye; NO: Jordyn Tyson; PHI: Makai Lemon; SF: Jerry Rice; SEA: Sam Darnold; TB: Baker Mayfield; TEN: Carnell Tate")),
 'Shadow Etch': (0.5, P("ARI: Jeremiyah Love; BUF: Josh Allen; CAR: Tetairoa McMillan; CIN: Ja'Marr Chase; DAL: Dak Prescott; DEN: Bo Nix; DET: Jared Goff; JAX: Trevor Lawrence; KC: Patrick Mahomes II; LV: Fernando Mendoza; LAR: Matthew Stafford; NO: Jordyn Tyson; NE: Drake Maye; SF: Brock Purdy; SEA: Jaxon Smith-Njigba")),
 'Tecmo': (1, P("DAL: Troy Aikman; TEN: Warren Moon; BUF: QB Bills, Cornelius Bennett; KC: Christian Okoye; SF: Jerry Rice; GB: Sterling Sharpe; WAS: Art Monk; CHI: William Perry; PIT: Rod Woodson; CIN: Joe Burrow; NE: Drake Maye; MIN: Justin Jefferson; BAL: Derrick Henry; LAR: Myles Garrett; PHI: QB Eagles; CLE: QB Browns")),
 'Ultra Violet': (1, P("BUF: Josh Allen; CHI: Caleb Williams; KC: Patrick Mahomes II; LAC: Justin Herbert; LAR: Matthew Stafford, Myles Garrett, Ty Simpson; BAL: Derrick Henry; SF: Christian McCaffrey, George Kittle; DAL: CeeDee Lamb; DET: Amon-Ra St. Brown; SEA: Jaxon Smith-Njigba; GB: Micah Parsons; TB: Tom Brady; WAS: Sean Taylor; LV: Fernando Mendoza; ARI: Jeremiyah Love; PHI: Makai Lemon; TEN: Carnell Tate")),
 'Lightning Leaders': (1, P("BUF: Josh Allen; CAR: Bryce Young; CHI: Caleb Williams; DAL: Dak Prescott, CeeDee Lamb; DEN: Bo Nix; GB: Jordan Love; HOU: CJ Stroud; JAX: Trevor Lawrence; KC: Patrick Mahomes II; LV: Maxx Crosby; LAC: Justin Herbert; LAR: Puka Nacua; NE: Drake Maye; NYG: Jaxson Dart; PHI: Jalen Hurts; PIT: T.J. Watt; SF: George Kittle; SEA: Jaxon Smith-Njigba; WAS: Jayden Daniels")),
 'Radiating Rookies': (0.6, P("ARI: Carson Beck, Jeremiyah Love; CAR: Chris Brazzell II; CLE: KC Concepcion, Denzel Boston; DAL: Caleb Downs; LV: Fernando Mendoza; LAR: Ty Simpson; MIA: Chris Bell; NO: Jordyn Tyson; NYG: Arvell Reese; NYJ: Cade Klubnik, Kenyon Sadiq, David Bailey; PHI: Makai Lemon; PIT: Drew Allar; SF: Kaelon Black; SEA: Jadarian Price; TEN: Carnell Tate; WAS: Sonny Styles")),
 'Game Genies': (1, P("ARI: Jeremiyah Love; BUF: Josh Allen; CAR: Bryce Young; CIN: Joe Burrow; CLE: Shedeur Sanders; DAL: Dak Prescott; DEN: Jaylen Waddle; DET: Amon-Ra St. Brown; GB: Jordan Love; HOU: CJ Stroud; IND: Daniel Jones; JAX: Trevor Lawrence; KC: Patrick Mahomes II; LV: Fernando Mendoza; LAC: Justin Herbert; LAR: Ty Simpson; MIA: De'Von Achane; NO: Jordyn Tyson; NYJ: Garrett Wilson; PHI: Makai Lemon; PIT: Aaron Rodgers; SF: Brock Purdy; SEA: Sam Darnold; TB: Baker Mayfield; TEN: Carnell Tate")),
 'Glass Canvas': (1, P("ARI: Carson Beck; BAL: Lamar Jackson; BUF: Josh Allen; CAR: Bryce Young; CHI: Caleb Williams; CIN: Joe Burrow; KC: Patrick Mahomes II, Travis Kelce; DAL: Dak Prescott; DEN: Peyton Manning; DET: Barry Sanders; GB: Jordan Love; LV: Fernando Mendoza; LAC: Justin Herbert; LAR: Matthew Stafford; MIA: Dan Marino; MIN: Randy Moss; NE: Tom Brady; NO: Jordyn Tyson; NYG: Jaxson Dart; PHI: Jalen Hurts; SF: Jerry Rice; SEA: Jaxon Smith-Njigba; TB: Baker Mayfield; TEN: Carnell Tate")),
 'Gridlock': (1, P("ARI: Jeremiyah Love; ATL: Bijan Robinson; BAL: Lamar Jackson; BUF: Josh Allen; CHI: Colston Loveland; CIN: Ja'Marr Chase; CLE: Quinshon Judkins; DAL: George Pickens; DEN: Jaylen Waddle; DET: Jahmyr Gibbs; GB: Josh Jacobs; HOU: CJ Stroud; IND: Tyler Warren; JAX: Trevor Lawrence; KC: Kenneth Walker III; LV: Fernando Mendoza; LAC: Omarion Hampton; LAR: Puka Nacua; MIN: Kyler Murray; NE: TreVeyon Henderson; NO: Chris Olave; NYG: Cam Skattebo; PHI: Saquon Barkley; SF: Christian McCaffrey; TEN: Carnell Tate")),
 'Madden 99 Club': (1.5, P("BUF: Josh Allen; LAR: Matthew Stafford, Myles Garrett; CIN: Ja'Marr Chase; SEA: Jaxon Smith-Njigba; ARI: Trey McBride")),
}
SPECIAL = [('Lombardi Trophy SuperFractor 1/1', 'Super Bowl LX trophy card', 'SEA', 60), ('MVP Buyback', 'Matthew Stafford', 'LAR', 10)]

# Demand weights: my own estimates of relative card demand (not sales data). Mendoza = 100.
W = {'Fernando Mendoza': 100, 'Jeremiyah Love': 40, 'Carnell Tate': 40, 'KC Concepcion': 28, 'Denzel Boston': 26, 'Jordyn Tyson': 26, 'Jonah Coleman': 26, 'Ty Simpson': 22, 'Makai Lemon': 20,
 'Caleb Downs': 18, 'Carson Beck': 16, 'Arvell Reese': 16, 'Jadarian Price': 14, 'David Bailey': 12, 'Garrett Nussmeier': 12, 'Omar Cooper Jr.': 12, 'Kenyon Sadiq': 10, 'Drew Allar': 9, 'Cade Klubnik': 9,
 'Nick Singleton': 8, 'Sonny Styles': 8, 'Mike Washington Jr.': 7, "Ja'Kobi Lane": 7, "De'Zhaun Stribling": 7, 'Taylen Green': 6, 'Chris Bell': 6, 'Antonio Williams': 6, 'Zachariah Branch': 6,
 'Chris Brazzell II': 6, 'Rueben Bain Jr.': 6, 'Eli Stowers': 6, 'Skyler Bell': 5, 'Germie Bernard': 5, 'Kaytron Allen': 5, 'Zavion Thomas': 5, 'Elijah Sarratt': 5, 'Emmett Johnson': 5, 'Mansoor Delane': 5,
 'Cole Payton': 5, 'Deion Burks': 4, 'Francis Mauigoa': 4, 'Dillon Thieneman': 4, 'Jermod McCoy': 4, 'Keldric Faulk': 4, 'Peter Woods': 4, 'Kaelon Black': 4, 'Caleb Douglas': 4, 'Demond Claiborne': 4, 'Max Klare': 4,
 'Patrick Mahomes II': 150, 'Tom Brady': 150, 'Josh Allen': 80, 'Joe Burrow': 70, 'Drake Maye': 60, 'Lamar Jackson': 60, 'Caleb Williams': 50, 'Jayden Daniels': 45, 'Jaxson Dart': 40, 'Justin Jefferson': 40,
 "Ja'Marr Chase": 40, 'Jaxon Smith-Njigba': 40, 'Puka Nacua': 40, 'Jahmyr Gibbs': 35, 'Jalen Hurts': 35, 'Aaron Rodgers': 35, 'Saquon Barkley': 30, 'Bijan Robinson': 30, 'Matthew Stafford': 30,
 'Justin Herbert': 30, 'Travis Hunter': 30, 'CJ Stroud': 25, 'Brock Purdy': 25, 'CeeDee Lamb': 25, 'Dak Prescott': 25, 'Bo Nix': 25, 'Cam Ward': 25, 'Ashton Jeanty': 25, 'Christian McCaffrey': 25,
 'Derrick Henry': 25, 'Shedeur Sanders': 20, 'Brock Bowers': 20, 'Myles Garrett': 20, 'T.J. Watt': 20, 'Amon-Ra St. Brown': 20, 'Micah Parsons': 20, 'Travis Kelce': 20, 'Malik Nabers': 18,
 'Jordan Love': 15, 'Tetairoa McMillan': 15, 'Baker Mayfield': 15, 'Emeka Egbuka': 15, 'Cam Skattebo': 12, 'Trevor Lawrence': 12, 'Tyler Shough': 12, 'George Kittle': 12, 'Sam Darnold': 12,
 'Omarion Hampton': 12, 'TreVeyon Henderson': 12, 'Jonathan Taylor': 12, "De'Von Achane": 12, 'Tyler Warren': 10, 'Luther Burden III': 10, 'Colston Loveland': 10, 'Quinshon Judkins': 10, 'Bryce Young': 10,
 'Maxx Crosby': 10, 'Trey McBride': 10, 'Garrett Wilson': 10, 'Jared Goff': 10, 'Matthew Golden': 8, 'Xavier Worthy': 8, 'Carson Schwesinger': 8, 'Brian Thomas Jr.': 8, 'Drake London': 8, 'Breece Hall': 8,
 'Nico Collins': 8, 'James Cook': 8, 'Alvin Kamara': 8, 'Rome Odunze': 8, 'Rashee Rice': 8, 'Ladd McConkey': 8, 'Michael Penix Jr.': 8, 'Kenneth Walker III': 10, 'Anthony Richardson': 6,
 'Peyton Manning': 80, 'Joe Montana': 70, 'Barry Sanders': 60, 'Jerry Rice': 60, 'Dan Marino': 50, 'John Elway': 45, 'Deion Sanders': 45, 'Randy Moss': 40, 'Bo Jackson': 40, 'Drew Brees': 40, 'Brett Favre': 40,
 'Troy Aikman': 35, 'Lawrence Taylor': 30, 'Rob Gronkowski': 30, 'Steve Young': 30, 'Sean Taylor': 30, 'Eli Manning': 25, 'Michael Vick': 25, 'Troy Polamalu': 25, 'Ray Lewis': 25, 'Larry Fitzgerald': 20,
 'Tony Romo': 15, 'Kurt Warner': 15, 'Eric Dickerson': 15, 'Luke Kuechly': 15, 'Terrell Davis': 12, 'Jerome Bettis': 12, 'Michael Irvin': 12, 'Jim Kelly': 12}
ROOKIES = {p for p, _ in BASE_RC}
LEGEND_SETS = {'Chrome Legends Autographs', 'Hall of Chrome Autographs', 'Class of 26 Autographs', 'Ring of Honor Autographs'}
def w(p, legend=False):
    return W.get(p, 2 if p in ROOKIES else (8 if legend else 4))
FAN = dict(DAL=1.15, KC=1.10, PIT=1.05, GB=1.05, CHI=1.05, PHI=1.05, SF=1.05)

# Formats. Market box prices: Dave & Adam's presale via The Hobby Wire (Nov 17). Boxes per case: Cardsmiths Breaks.
# rk = assumed share of autograph slots that are Rookie Variation Autos (2025 hobby odds put rookie autos near 90% of hobby autos; FDI and Breaker ran heavier on veterans and legends).
# mix = how the break's value splits between autographs, base/rookie colour and short-print inserts (my assumption).
FORMATS = [
 dict(format='hobby', label='Hobby', boxes=12, autos_box=1, packs_case=240, box_msrp=439.99, box_market=674.95, rk=0.88, mix=(0.45, 0.35, 0.20), col='h'),
 dict(format='jumbo', label='Jumbo', boxes=8, autos_box=2, packs_case=96, box_msrp=789.99, box_market=1249.95, rk=0.88, mix=(0.45, 0.35, 0.20), col='j'),
 dict(format='delight', label="Breaker's Delight", boxes=6, autos_box=2, packs_case=6, box_msrp=None, box_market=1924.95, rk=0.85, mix=(0.70, 0.20, 0.10), col='b'),
 dict(format='fdi', label='First Day Issue', boxes=8, autos_box=3, packs_case=96, box_msrp=2500.0, box_market=3849.95, rk=0.75, mix=(0.60, 0.30, 0.10), col='f'),
]
# 2025 Topps Chrome Football pack odds (1 in N packs): hobby, jumbo, FDI, breaker. Source: Checklist Insider.
O25 = {'1991 Topps Autographs': (3391, 1018, 681, 85), 'Chrome Legends Autographs': (3654, 1099, 749, 92), 'Hall of Chrome Autographs': (3654, 1099, 749, 92), 'Future Stars Autographs': (3968, 1187, 789, 100),
 'Chromographs': (9264, 2786, 1872, 231), 'Tecmo Autographs': (36405, 6408, 1498, 632), 'Base Variation Autographs': (7546, 2434, 624, 316),
 'Kaiju': (2319, 929, 936, 58), 'Helix': (2559, 859, 881, 72), 'Game Genies': (928, 372, 375, 24), 'Tecmo': (928, 372, 375, 24), 'Lightning Leaders': (1160, 464, 468, 29), 'Ultra Violet': (1160, 464, 468, 29),
 'Radiating Rookies': (580, 232, 231, None), 'Shadow Etch': (387, 155, 155, None)}
SET_MULT = {'Chromographs': 1.5, '1991 Topps Autographs': 1.2, 'Dual Autographs': 2.0}
# Split of the non-rookie autograph slots between sets, from the 2025 hobby odds (Dual, Class of 26, Ring of Honor had no 2025 line: assumed).
OTHER = {'1991 Topps Autographs': 1/3391, 'Chrome Legends Autographs': 1/3654, 'Hall of Chrome Autographs': 1/3654, 'Future Stars Autographs': 1/3968, 'Chromographs': 1/9264,
 'Base Variation Autographs': 1/7546, 'Tecmo Autographs': 1/36405, 'Dual Autographs': 1/9264, 'Class of 26 Autographs': 1/50000, 'Ring of Honor Autographs': 1/50000}
tot = sum(OTHER.values()); OTHER = {k: v / tot for k, v in OTHER.items()}

def auto_cards(rk):  # [(set, player, team, prob per autograph slot, value weight)]
    out = [('Rookie Variation Autographs', p, t, rk / 92, w(p)) for p, t in RVA]
    for s, cards in AUTOS.items():
        for p, t in cards:
            out.append((s, p, t, (1 - rk) * OTHER[s] / len(cards), w(p, s in LEGEND_SETS) * SET_MULT.get(s, 1)))
    for a, ta, b, tb in DUALS:
        pr = (1 - rk) * OTHER['Dual Autographs'] / len(DUALS); val = (w(a, True) + w(b, True)) * SET_MULT['Dual Autographs'] / 2
        out += [('Dual Autographs', a + ' / ' + b, ta, pr / 2, val), ('Dual Autographs', a + ' / ' + b, tb, pr / 2, val)]
    return out

vets = defaultdict(set)
for s, cards in AUTOS.items():
    if s not in LEGEND_SETS and s != 'Tecmo Autographs':
        for p, t in cards: vets[t].add(p)
for s, (m, cards) in SSP.items():
    if s not in ('Tecmo', 'Kaiju', 'Glass Canvas', 'Helix', 'Ultra Violet'):
        for p, t in cards:
            if p not in ROOKIES: vets[t].add(p)
color = {t: sum(w(p) for p, tt in BASE_RC if tt == t) + 0.4 * sum(w(p) for p in vets[t]) for t in NAMES}
ssp = defaultdict(float); ssp_n = defaultdict(int)
for s, (m, cards) in SSP.items():
    for p, t in cards: ssp[t] += m * w(p, True); ssp_n[t] += 1
for name, who, t, val in SPECIAL: ssp[t] += val; ssp_n[t] += 1
def share(d): s = sum(d.values()); return {t: d.get(t, 0) / s for t in NAMES}
cs, ss = share(color), share(ssp)
def tier(x): return 'S' if x >= 7 else 'A' if x >= 4 else 'B' if x >= 2.5 else 'C' if x >= 1.5 else 'D'
def top(t, n=3): return ', '.join(p.split(' ', 1)[1] if p.count(' ') else p for p in sorted([p for p, tt in RVA if tt == t], key=lambda p: -w(p))[:n])
head = {}
for t in NAMES:
    r = sorted([p for p, tt in BASE_RC if tt == t], key=lambda p: -w(p))[0]
    v = sorted(vets[t], key=lambda p: -w(p))[:2]
    head[t] = r + (' (no auto)' if r in NO_RVA else '') + '; ' + ', '.join(v)

spots, summary, formats = [], [], []
for F in FORMATS:
    cards = auto_cards(F['rk']); n = F['boxes'] * F['autos_box']; case = round(F['boxes'] * F['box_market'], 2)
    av = defaultdict(float); pt = defaultdict(float); prk = defaultdict(float)
    for s, p, t, pr, val in cards:
        av[t] += pr * val; pt[t] += pr
        if s == 'Rookie Variation Autographs': prk[t] += pr
    a = share(av); raw = {t: (F['mix'][0] * a[t] + F['mix'][1] * cs[t] + F['mix'][2] * ss[t]) * FAN.get(t, 1) for t in NAMES}
    sh = share(raw); order = sorted(NAMES, key=lambda t: -sh[t])
    for i, t in enumerate(order):
        pct = round(100 * sh[t], 1)
        spots.append(dict(team=NAMES[t], abbr=t, format=F['format'], rank=i + 1, tier=tier(pct), share_pct=pct, share=round(sh[t], 5), p_slot=round(pt[t], 5), p_rookie_slot=round(prk[t], 5), fair_spot=round(sh[t] * case), exp_autos=round(n * pt[t], 2),
            p_any_auto=round(100 * (1 - (1 - pt[t]) ** n)), p_rookie_auto=round(100 * (1 - (1 - prk[t]) ** n)), rookie_signers=sum(1 for p, tt in RVA if tt == t), top_signers=top(t),
            other_autos=sum(1 for s, p, tt, pr, val in cards if tt == t and s != 'Rookie Variation Autographs'), ssp_inserts=ssp_n[t], patch_autos=sum(1 for p, tt in PATCH if tt == t), headline=head[t]))
    top4 = round(sum(100 * sh[t] for t in order[:4])); pm = F['rk'] / 92
    summary.append(dict(format=F['format'], label=F['label'], top_team=NAMES[order[0]], top_share=round(100 * sh[order[0]], 1), second_team=NAMES[order[1]], top4_share=top4,
        bottom12_share=round(sum(100 * sh[t] for t in order[-12:])), case_market=round(case), autos_case=n, mendoza_auto_pct=round(100 * (1 - (1 - pm) ** n), 1), mendoza_slot=round(pm, 5),
        teams_under_half=sum(1 for t in NAMES if (1 - (1 - pt[t]) ** n) < 0.5)))
    formats.append(dict(format=F['format'], label=F['label'], boxes_case=F['boxes'], autos_box=F['autos_box'], autos_case=n, box_presale=F['box_msrp'], box_market=F['box_market'], case_market=round(case), rookie_auto_share_pct=round(100 * F['rk'])))

def odds_rows(chase, kind, team, basis, rate_fn):
    for F in FORMATS:
        lam = rate_fn(F)
        if lam is None: txt, p = 'Not in this format in 2025', None
        else:
            p = 1 - math.exp(-lam)
            txt = ('%.1f per case' % lam) if lam >= 1 else ('1 in %s cases' % (('%.1f' % (1 / p)) if 1 / p < 20 else '{:,}'.format(round(1 / p))))
        chases.append(dict(chase=chase, kind=kind, team=team, basis=basis, format=F['format'], per_case=None if lam is None else round(lam, 4), per_box=None if lam is None else round(lam / F['boxes'], 6), odds=txt, sort=len(chases)))
chases = []
def proxy(setname, size=None):
    def f(F):
        o = O25[setname][dict(hobby=0, jumbo=1, fdi=2, delight=3)[F['format']]]
        return None if o is None else F['packs_case'] / o / (size or 1)
    return f
def model(setname, player):
    def f(F): return F['boxes'] * F['autos_box'] * sum(pr for s, p, t, pr, val in auto_cards(F['rk']) if s == setname and player in p)
    return f
for p, t in [('Fernando Mendoza', 'Raiders'), ('Jeremiyah Love', 'Cardinals'), ('Carnell Tate', 'Titans'), ('KC Concepcion', 'Browns'), ('Jordyn Tyson', 'Saints'), ('Ty Simpson', 'Rams')]:
    odds_rows(p + ' Rookie Variation Auto (any parallel)', 'Rookie auto', t, 'Model', model('Rookie Variation Autographs', p))
odds_rows('Fernando Mendoza Chromograph', 'Auto', 'Raiders', 'Model', model('Chromographs', 'Fernando Mendoza'))
odds_rows('Fernando Mendoza 1991 Topps Auto', 'Auto', 'Raiders', 'Model', model('1991 Topps Autographs', 'Fernando Mendoza'))
odds_rows('Mendoza / Simpson Dual Auto', 'Auto', 'Raiders / Rams', 'Model', model('Dual Autographs', 'Fernando Mendoza'))
odds_rows('Patrick Mahomes Base Variation Auto', 'Auto', 'Chiefs', 'Model', model('Base Variation Autographs', 'Patrick Mahomes II'))
odds_rows('Josh Allen Base Variation Auto', 'Auto', 'Bills', 'Model', model('Base Variation Autographs', 'Josh Allen'))
odds_rows('Tom Brady Chrome Legends Auto', 'Auto', 'Patriots', 'Model', model('Chrome Legends Autographs', 'Tom Brady'))
for s, lab in [('Chromographs', 'Any Chromograph (24 signers)'), ('1991 Topps Autographs', 'Any 1991 Topps Auto (22)'), ('Chrome Legends Autographs', 'Any Chrome Legends Auto (48)'), ('Hall of Chrome Autographs', 'Any Hall of Chrome Auto (25)'), ('Tecmo Autographs', 'Any Tecmo Auto (14)')]:
    odds_rows(lab, 'Auto set', 'Any', '2025 odds', proxy(s))
odds_rows('Any Kaiju (10 cards)', 'Insert', 'Any', '2025 odds', proxy('Kaiju'))
for p, t in [('Fernando Mendoza', 'Raiders'), ('Tom Brady', 'Buccaneers'), ('Jeremiyah Love', 'Cardinals')]:
    odds_rows(p + ' Kaiju', 'Insert', t, '2025 odds', proxy('Kaiju', 10))
for s, n in [('Helix', 15), ('Game Genies', 25), ('Tecmo', 17), ('Ultra Violet', 20), ('Lightning Leaders', 20), ('Radiating Rookies', 20), ('Shadow Etch', 15)]:
    odds_rows('Any %s (%d cards)' % (s, n), 'Insert', 'Any', '2025 odds', proxy(s))

checklist = []
def add(t, p, s, kind, note=''):
    checklist.append(dict(team=NAMES[t], abbr=t, player=p, set=s, kind=kind, rc='RC' if p in ROOKIES else '', weight=w(p, kind != 'Base rookie'), note=note))
for p, t in BASE_RC: add(t, p, 'Base rookie (301-400)', 'Base rookie', 'No autograph in this product' if p in NO_RVA else 'Rookie Variation Auto')
for s, cards in AUTOS.items():
    for p, t in cards: add(t, p, s, 'Auto')
for a, ta, b, tb in DUALS:
    add(ta, a + ' / ' + b, 'Dual Autographs', 'Auto', '' if ta == tb else 'Two teams: set the rule before the break')
    if tb != ta: add(tb, a + ' / ' + b, 'Dual Autographs', 'Auto', 'Two teams: set the rule before the break')
for p, t in GOLD_SHIELD: add(t, p, 'Gold Shield Autographs', 'Auto', '1/1 patch auto')
for p, t in PATCH: add(t, p, 'Prem1ere Patch Autographs', 'Patch auto 1/1')
for p, t in RETAIL_RRA: add(t, p, 'Retail Rookie Autographs', 'Retail auto', 'Retail boxes only')
for s, (m, cards) in SSP.items():
    for p, t in cards: add(t, p, s, 'Short-print insert')
for name, who, t, val in SPECIAL: add(t, who, name, 'Short-print insert')

STATUS = {'Fernando Mendoza': ('QB', 'Now starting after the Cousins trade; OROY favorite (about +225)'), 'Jeremiyah Love': ('RB', 'Preseason favorite; has faded after an ankle injury'),
 'Carnell Tate': ('WR', 'Led the OROY market into Week 10; now about +800'), 'KC Concepcion': ('WR', 'About +500, second on the board'), 'Denzel Boston': ('WR', 'About +800'),
 'Jordyn Tyson': ('WR', 'Back from injury; 11 catches in his second game'), 'Jonah Coleman': ('RB', 'About +550, top-three OROY odds'), 'Ty Simpson': ('QB', 'Behind Stafford'), 'Makai Lemon': ('WR', 'Has dealt with injuries'),
 'Caleb Downs': ('S', 'Top defensive name with Reese'), 'Carson Beck': ('QB', 'Expected to make his first start; about 16-1'), 'Arvell Reese': ('LB', 'DROY favorite'), 'Jadarian Price': ('RB', ''),
 'David Bailey': ('EDGE', 'DROY contender'), 'Garrett Nussmeier': ('QB', 'Behind Mahomes'), 'Omar Cooper Jr.': ('WR', 'Was as high as 12% on Kalshi in late October'), 'Kenyon Sadiq': ('TE', 'Has dealt with injuries'),
 'Drew Allar': ('QB', ''), 'Cade Klubnik': ('QB', ''), 'Nick Singleton': ('RB', ''), 'Eli Stowers': ('TE', '')}
sets_of = defaultdict(list)
for r in checklist:
    if r['kind'] in ('Auto', 'Short-print insert') and any(k in r['player'] for k in STATUS):
        for k in STATUS:
            if k in r['player']: sets_of[k].append((r['kind'], r['set']))
rookies = []
for p, (pos, note) in STATUS.items():
    t = dict(BASE_RC)[p]
    extra = sorted({s.replace(' Autographs', '') for k, s in sets_of[p] if k == 'Auto'})
    rookies.append(dict(player=p, team=NAMES[t], pos=pos, weight=W[p], rookie_auto='No' if p in NO_RVA else 'Yes', other_autos=', '.join(extra) or 'None',
        ssp_inserts=sum(1 for k, s in sets_of[p] if k == 'Short-print insert'), status=note))
weights = [dict(player=p, weight=v, type='Rookie' if p in ROOKIES else 'Veteran or legend') for p, v in sorted(W.items(), key=lambda kv: -kv[1])]

code = open(__file__).read()
def dump(name, rows, inputs):
    meta = ([dict(label='model.py', value=code, type='code', lang='python')] if name in ('spots', 'chases') else [dict(label='Made by', value='model.py, shown in full under the team model source')]) + [dict(label='Inputs', value=inputs)]
    json.dump(dict(rows=rows, meta=meta), open(os.path.join(OUT, name + '.json'), 'w'), ensure_ascii=False)
I = 'Topps checklist (degreegrading.com, hobbymonitor.com); 2025 pack odds (checklistinsider.com); box prices (thehobbywire.com); my demand weights'
dump('spots', spots, I); dump('summary', summary, I); dump('formats', formats, 'cardsmithsbreaks.com box table; thehobbywire.com prices; checklistinsider.com presale prices')
dump('chases', chases, I); dump('checklist', checklist, 'Topps checklist (degreegrading.com); my demand weights'); dump('rookies', rookies, 'Topps checklist; sportsbook and Kalshi odds, Nov 11-16; my demand weights')
dump('weights', weights, 'My own estimates')
for F in ('hobby', 'fdi'):
    print(F); [print(' ', r['rank'], r['team'], r['tier'], r['share_pct'], r['fair_spot'], r['p_any_auto'], r['p_rookie_auto'], r['exp_autos']) for r in spots if r['format'] == F]
print(summary); print(len(checklist), len(chases))
for c in chases:
    if c['format'] in ('hobby', 'delight'): print(c['format'], c['chase'], c['odds'])
print({k: len(v) for k, v in AUTOS.items()}, {k: len(v[1]) for k, v in SSP.items()})
