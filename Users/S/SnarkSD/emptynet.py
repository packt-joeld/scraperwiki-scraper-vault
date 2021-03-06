import scraperwiki
import lxml.etree
import lxml.html
import datetime
import time

gameurlstart = "http://www.nhl.com/scores/htmlreports/20122013/PL02"
gameurlend = ".HTM"

teamidlong = ["ANAHEIM DUCKS", "BOSTON BRUINS", "BUFFALO SABRES", "CALGARY FLAMES",  "CAROLINA HURRICANES",  "CHICAGO BLACKHAWKS",  "COLORADO AVALANCHE", "COLUMBUS BLUE JACKETS",  "DALLAS STARS", "DETROIT RED WINGS", "EDMONTON OILERS", "FLORIDA PANTHERS", "LOS ANGELES KINGS", "MINNESOTA WILD", "MONTREAL CANADIENS", "NASHVILLE PREDATORS", "NEW JERSEY DEVILS", "NEW YORK ISLANDERS", "NEW YORK RANGERS", "OTTAWA SENATORS", "PHILADELPHIA FLYERS", "PHOENIX COYOTES", "PITTSBURGH PENGUINS", "SAN JOSE SHARKS", "ST. LOUIS BLUES", "TAMPA BAY LIGHTNING", "TORONTO MAPLE LEAFS", "VANCOUVER CANUCKS", "WASHINGTON CAPITALS", "WINNIPEG JETS", "ATLANTA THRASHERS", "CANADIENS MONTREAL"]

teamid = ["ANA", "BOS", "BUF", "CGY",  "CAR",  "CHI",  "COL", "CBJ",  "DAL", "DET", "EDM", "FLA", "L.A", "MIN", "MTL", "NSH", "N.J", "NYI", "NYR", "OTT", "PHI", "PHX", "PIT", "S.J", "STL", "T.B", "TOR", "VAN", "WSH", "WPG", "ATL", "MTL"]
gid = j = 0
team = "DET"
TeamF = [-26, 1, 14, -2, 8, 16, 19, 37, 54, 46, 58, 34, 39, 39, 61, 75, 74, 59, 71, 81, 96, 84, 77, 98, 103, 112, 147, 166, 154, 184, 180, 158, 162, 176, 192, 192, 209]
gamenum = 37
season = "2012-2013s"
gidarray = [556,
569,
601,
608,
623,
642,
667,
678,
691,
699,
717]





#for gid in range((scraperwiki.sqlite.get_var('gid') + 1),(scraperwiki.sqlite.get_var('gid') + 1230)):
#for gid in gidarray[(scraperwiki.sqlite.get_var('gamenum')):]:
for gid in gidarray:
    if gid < 10:
        url = gameurlstart + "000" + str(gid) + gameurlend
    elif gid < 100:
        url = gameurlstart + "00" + str(gid) + gameurlend
    elif gid <1000:
        url = gameurlstart + "0" + str(gid) + gameurlend
    else:
        url = gameurlstart + str(gid) + gameurlend

    html = scraperwiki.scrape(url)
    root = lxml.html.fromstring(html) # turn HTML into an lxml object
    i = 0

    awayteam = teamid[teamidlong.index(root.cssselect("#Visitor td")[5].text)] # Matches the contents of the 5th <td> in the html element with id "Visitor" to short awayteam
    hometeam = teamid[teamidlong.index(root.cssselect("#Home td")[5].text)]
    
    if (team == awayteam) or (team == hometeam):
        TeamF.append(0)
        TeamF[gamenum] = TeamF[gamenum - 1]
        tds = root.cssselect("tr.evenColor td") # assign all <td> elements of PBP data only to a list called "tds"
        for td in tds: # iterate over each of the <td> elements (i.e. elements of the list called "tds")
            if ((tds[i-3].text != "5") and td.text =="GOAL") or ((tds[i-3].text != "5") and td.text =="SHOT") or ((tds[i-3].text != "5") and td.text =="MISS") or ((tds[i-3].text != "5") and td.text =="BLOCK"):
                try:
                    awayskate = (tds[i+5].text,tds[i+9].text,tds[i+13].text,tds[i+17].text,tds[i+21].text,tds[i+25].text)
                    homeskate = ([tds[i+29].text,tds[i+33].text,tds[i+37].text,tds[i+41].text,tds[i+45].text,tds[i+49].text])
                except IndexError:
                    pass
                if ('G' in awayskate or 'G' in homeskate) and tds[i + 1].text.startswith(team):
                    TeamF[gamenum] += 1
                elif ('G' in awayskate or 'G' in homeskate):
                    TeamF[gamenum] -= 1
                else:
                    pass
            i += 1
        gamenum += 1
    save = [team, gid, TeamF]
    print team, gid, gamenum, TeamF 
    #print save
    scraperwiki.sqlite.save_var(gid, save)
    scraperwiki.sqlite.save_var('gamenum', gamenum)
    time.sleep(3) # delay X seconds to throttle URL fetching   
import scraperwiki
import lxml.etree
import lxml.html
import datetime
import time

gameurlstart = "http://www.nhl.com/scores/htmlreports/20122013/PL02"
gameurlend = ".HTM"

teamidlong = ["ANAHEIM DUCKS", "BOSTON BRUINS", "BUFFALO SABRES", "CALGARY FLAMES",  "CAROLINA HURRICANES",  "CHICAGO BLACKHAWKS",  "COLORADO AVALANCHE", "COLUMBUS BLUE JACKETS",  "DALLAS STARS", "DETROIT RED WINGS", "EDMONTON OILERS", "FLORIDA PANTHERS", "LOS ANGELES KINGS", "MINNESOTA WILD", "MONTREAL CANADIENS", "NASHVILLE PREDATORS", "NEW JERSEY DEVILS", "NEW YORK ISLANDERS", "NEW YORK RANGERS", "OTTAWA SENATORS", "PHILADELPHIA FLYERS", "PHOENIX COYOTES", "PITTSBURGH PENGUINS", "SAN JOSE SHARKS", "ST. LOUIS BLUES", "TAMPA BAY LIGHTNING", "TORONTO MAPLE LEAFS", "VANCOUVER CANUCKS", "WASHINGTON CAPITALS", "WINNIPEG JETS", "ATLANTA THRASHERS", "CANADIENS MONTREAL"]

teamid = ["ANA", "BOS", "BUF", "CGY",  "CAR",  "CHI",  "COL", "CBJ",  "DAL", "DET", "EDM", "FLA", "L.A", "MIN", "MTL", "NSH", "N.J", "NYI", "NYR", "OTT", "PHI", "PHX", "PIT", "S.J", "STL", "T.B", "TOR", "VAN", "WSH", "WPG", "ATL", "MTL"]
gid = j = 0
team = "DET"
TeamF = [-26, 1, 14, -2, 8, 16, 19, 37, 54, 46, 58, 34, 39, 39, 61, 75, 74, 59, 71, 81, 96, 84, 77, 98, 103, 112, 147, 166, 154, 184, 180, 158, 162, 176, 192, 192, 209]
gamenum = 37
season = "2012-2013s"
gidarray = [556,
569,
601,
608,
623,
642,
667,
678,
691,
699,
717]





#for gid in range((scraperwiki.sqlite.get_var('gid') + 1),(scraperwiki.sqlite.get_var('gid') + 1230)):
#for gid in gidarray[(scraperwiki.sqlite.get_var('gamenum')):]:
for gid in gidarray:
    if gid < 10:
        url = gameurlstart + "000" + str(gid) + gameurlend
    elif gid < 100:
        url = gameurlstart + "00" + str(gid) + gameurlend
    elif gid <1000:
        url = gameurlstart + "0" + str(gid) + gameurlend
    else:
        url = gameurlstart + str(gid) + gameurlend

    html = scraperwiki.scrape(url)
    root = lxml.html.fromstring(html) # turn HTML into an lxml object
    i = 0

    awayteam = teamid[teamidlong.index(root.cssselect("#Visitor td")[5].text)] # Matches the contents of the 5th <td> in the html element with id "Visitor" to short awayteam
    hometeam = teamid[teamidlong.index(root.cssselect("#Home td")[5].text)]
    
    if (team == awayteam) or (team == hometeam):
        TeamF.append(0)
        TeamF[gamenum] = TeamF[gamenum - 1]
        tds = root.cssselect("tr.evenColor td") # assign all <td> elements of PBP data only to a list called "tds"
        for td in tds: # iterate over each of the <td> elements (i.e. elements of the list called "tds")
            if ((tds[i-3].text != "5") and td.text =="GOAL") or ((tds[i-3].text != "5") and td.text =="SHOT") or ((tds[i-3].text != "5") and td.text =="MISS") or ((tds[i-3].text != "5") and td.text =="BLOCK"):
                try:
                    awayskate = (tds[i+5].text,tds[i+9].text,tds[i+13].text,tds[i+17].text,tds[i+21].text,tds[i+25].text)
                    homeskate = ([tds[i+29].text,tds[i+33].text,tds[i+37].text,tds[i+41].text,tds[i+45].text,tds[i+49].text])
                except IndexError:
                    pass
                if ('G' in awayskate or 'G' in homeskate) and tds[i + 1].text.startswith(team):
                    TeamF[gamenum] += 1
                elif ('G' in awayskate or 'G' in homeskate):
                    TeamF[gamenum] -= 1
                else:
                    pass
            i += 1
        gamenum += 1
    save = [team, gid, TeamF]
    print team, gid, gamenum, TeamF 
    #print save
    scraperwiki.sqlite.save_var(gid, save)
    scraperwiki.sqlite.save_var('gamenum', gamenum)
    time.sleep(3) # delay X seconds to throttle URL fetching   
import scraperwiki
import lxml.etree
import lxml.html
import datetime
import time

gameurlstart = "http://www.nhl.com/scores/htmlreports/20122013/PL02"
gameurlend = ".HTM"

teamidlong = ["ANAHEIM DUCKS", "BOSTON BRUINS", "BUFFALO SABRES", "CALGARY FLAMES",  "CAROLINA HURRICANES",  "CHICAGO BLACKHAWKS",  "COLORADO AVALANCHE", "COLUMBUS BLUE JACKETS",  "DALLAS STARS", "DETROIT RED WINGS", "EDMONTON OILERS", "FLORIDA PANTHERS", "LOS ANGELES KINGS", "MINNESOTA WILD", "MONTREAL CANADIENS", "NASHVILLE PREDATORS", "NEW JERSEY DEVILS", "NEW YORK ISLANDERS", "NEW YORK RANGERS", "OTTAWA SENATORS", "PHILADELPHIA FLYERS", "PHOENIX COYOTES", "PITTSBURGH PENGUINS", "SAN JOSE SHARKS", "ST. LOUIS BLUES", "TAMPA BAY LIGHTNING", "TORONTO MAPLE LEAFS", "VANCOUVER CANUCKS", "WASHINGTON CAPITALS", "WINNIPEG JETS", "ATLANTA THRASHERS", "CANADIENS MONTREAL"]

teamid = ["ANA", "BOS", "BUF", "CGY",  "CAR",  "CHI",  "COL", "CBJ",  "DAL", "DET", "EDM", "FLA", "L.A", "MIN", "MTL", "NSH", "N.J", "NYI", "NYR", "OTT", "PHI", "PHX", "PIT", "S.J", "STL", "T.B", "TOR", "VAN", "WSH", "WPG", "ATL", "MTL"]
gid = j = 0
team = "DET"
TeamF = [-26, 1, 14, -2, 8, 16, 19, 37, 54, 46, 58, 34, 39, 39, 61, 75, 74, 59, 71, 81, 96, 84, 77, 98, 103, 112, 147, 166, 154, 184, 180, 158, 162, 176, 192, 192, 209]
gamenum = 37
season = "2012-2013s"
gidarray = [556,
569,
601,
608,
623,
642,
667,
678,
691,
699,
717]





#for gid in range((scraperwiki.sqlite.get_var('gid') + 1),(scraperwiki.sqlite.get_var('gid') + 1230)):
#for gid in gidarray[(scraperwiki.sqlite.get_var('gamenum')):]:
for gid in gidarray:
    if gid < 10:
        url = gameurlstart + "000" + str(gid) + gameurlend
    elif gid < 100:
        url = gameurlstart + "00" + str(gid) + gameurlend
    elif gid <1000:
        url = gameurlstart + "0" + str(gid) + gameurlend
    else:
        url = gameurlstart + str(gid) + gameurlend

    html = scraperwiki.scrape(url)
    root = lxml.html.fromstring(html) # turn HTML into an lxml object
    i = 0

    awayteam = teamid[teamidlong.index(root.cssselect("#Visitor td")[5].text)] # Matches the contents of the 5th <td> in the html element with id "Visitor" to short awayteam
    hometeam = teamid[teamidlong.index(root.cssselect("#Home td")[5].text)]
    
    if (team == awayteam) or (team == hometeam):
        TeamF.append(0)
        TeamF[gamenum] = TeamF[gamenum - 1]
        tds = root.cssselect("tr.evenColor td") # assign all <td> elements of PBP data only to a list called "tds"
        for td in tds: # iterate over each of the <td> elements (i.e. elements of the list called "tds")
            if ((tds[i-3].text != "5") and td.text =="GOAL") or ((tds[i-3].text != "5") and td.text =="SHOT") or ((tds[i-3].text != "5") and td.text =="MISS") or ((tds[i-3].text != "5") and td.text =="BLOCK"):
                try:
                    awayskate = (tds[i+5].text,tds[i+9].text,tds[i+13].text,tds[i+17].text,tds[i+21].text,tds[i+25].text)
                    homeskate = ([tds[i+29].text,tds[i+33].text,tds[i+37].text,tds[i+41].text,tds[i+45].text,tds[i+49].text])
                except IndexError:
                    pass
                if ('G' in awayskate or 'G' in homeskate) and tds[i + 1].text.startswith(team):
                    TeamF[gamenum] += 1
                elif ('G' in awayskate or 'G' in homeskate):
                    TeamF[gamenum] -= 1
                else:
                    pass
            i += 1
        gamenum += 1
    save = [team, gid, TeamF]
    print team, gid, gamenum, TeamF 
    #print save
    scraperwiki.sqlite.save_var(gid, save)
    scraperwiki.sqlite.save_var('gamenum', gamenum)
    time.sleep(3) # delay X seconds to throttle URL fetching   
import scraperwiki
import lxml.etree
import lxml.html
import datetime
import time

gameurlstart = "http://www.nhl.com/scores/htmlreports/20122013/PL02"
gameurlend = ".HTM"

teamidlong = ["ANAHEIM DUCKS", "BOSTON BRUINS", "BUFFALO SABRES", "CALGARY FLAMES",  "CAROLINA HURRICANES",  "CHICAGO BLACKHAWKS",  "COLORADO AVALANCHE", "COLUMBUS BLUE JACKETS",  "DALLAS STARS", "DETROIT RED WINGS", "EDMONTON OILERS", "FLORIDA PANTHERS", "LOS ANGELES KINGS", "MINNESOTA WILD", "MONTREAL CANADIENS", "NASHVILLE PREDATORS", "NEW JERSEY DEVILS", "NEW YORK ISLANDERS", "NEW YORK RANGERS", "OTTAWA SENATORS", "PHILADELPHIA FLYERS", "PHOENIX COYOTES", "PITTSBURGH PENGUINS", "SAN JOSE SHARKS", "ST. LOUIS BLUES", "TAMPA BAY LIGHTNING", "TORONTO MAPLE LEAFS", "VANCOUVER CANUCKS", "WASHINGTON CAPITALS", "WINNIPEG JETS", "ATLANTA THRASHERS", "CANADIENS MONTREAL"]

teamid = ["ANA", "BOS", "BUF", "CGY",  "CAR",  "CHI",  "COL", "CBJ",  "DAL", "DET", "EDM", "FLA", "L.A", "MIN", "MTL", "NSH", "N.J", "NYI", "NYR", "OTT", "PHI", "PHX", "PIT", "S.J", "STL", "T.B", "TOR", "VAN", "WSH", "WPG", "ATL", "MTL"]
gid = j = 0
team = "DET"
TeamF = [-26, 1, 14, -2, 8, 16, 19, 37, 54, 46, 58, 34, 39, 39, 61, 75, 74, 59, 71, 81, 96, 84, 77, 98, 103, 112, 147, 166, 154, 184, 180, 158, 162, 176, 192, 192, 209]
gamenum = 37
season = "2012-2013s"
gidarray = [556,
569,
601,
608,
623,
642,
667,
678,
691,
699,
717]





#for gid in range((scraperwiki.sqlite.get_var('gid') + 1),(scraperwiki.sqlite.get_var('gid') + 1230)):
#for gid in gidarray[(scraperwiki.sqlite.get_var('gamenum')):]:
for gid in gidarray:
    if gid < 10:
        url = gameurlstart + "000" + str(gid) + gameurlend
    elif gid < 100:
        url = gameurlstart + "00" + str(gid) + gameurlend
    elif gid <1000:
        url = gameurlstart + "0" + str(gid) + gameurlend
    else:
        url = gameurlstart + str(gid) + gameurlend

    html = scraperwiki.scrape(url)
    root = lxml.html.fromstring(html) # turn HTML into an lxml object
    i = 0

    awayteam = teamid[teamidlong.index(root.cssselect("#Visitor td")[5].text)] # Matches the contents of the 5th <td> in the html element with id "Visitor" to short awayteam
    hometeam = teamid[teamidlong.index(root.cssselect("#Home td")[5].text)]
    
    if (team == awayteam) or (team == hometeam):
        TeamF.append(0)
        TeamF[gamenum] = TeamF[gamenum - 1]
        tds = root.cssselect("tr.evenColor td") # assign all <td> elements of PBP data only to a list called "tds"
        for td in tds: # iterate over each of the <td> elements (i.e. elements of the list called "tds")
            if ((tds[i-3].text != "5") and td.text =="GOAL") or ((tds[i-3].text != "5") and td.text =="SHOT") or ((tds[i-3].text != "5") and td.text =="MISS") or ((tds[i-3].text != "5") and td.text =="BLOCK"):
                try:
                    awayskate = (tds[i+5].text,tds[i+9].text,tds[i+13].text,tds[i+17].text,tds[i+21].text,tds[i+25].text)
                    homeskate = ([tds[i+29].text,tds[i+33].text,tds[i+37].text,tds[i+41].text,tds[i+45].text,tds[i+49].text])
                except IndexError:
                    pass
                if ('G' in awayskate or 'G' in homeskate) and tds[i + 1].text.startswith(team):
                    TeamF[gamenum] += 1
                elif ('G' in awayskate or 'G' in homeskate):
                    TeamF[gamenum] -= 1
                else:
                    pass
            i += 1
        gamenum += 1
    save = [team, gid, TeamF]
    print team, gid, gamenum, TeamF 
    #print save
    scraperwiki.sqlite.save_var(gid, save)
    scraperwiki.sqlite.save_var('gamenum', gamenum)
    time.sleep(3) # delay X seconds to throttle URL fetching   
