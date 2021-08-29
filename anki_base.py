BASE_DECK = {
    "newToday": [0, 0],
    "revToday": [0, 0],
    "lrnToday": [0, 0],
    "timeToday": [0, 0],
    "conf": 1,
    "usn": 0,
    "desc": "",
    "dyn": 0,
    "collapsed": False,
    "extendNew": 10,
    "extendRev": 50,
    "id": 1,  # TBD
    "name": "",  # TBD
    "mod": 1625822113
}

BASE_DCONF = {}
BASE_TAGS = {}

BASE_FIELD = {"name": "TBD", "ord": 0, "sticky": False, "rtl": False, "font": "Arial", "size": 20, "media": []}
BASE_TMPL = {"name": "TBD",
             "ord": 0,
             "qfmt": "TBD",
             "afmt": "TBD",
             "did": None, "bqfmt": "", "bafmt": ""}
BASE_MODEL = {"sortf": 0, "did": 0,
              "latexPre": "\\documentclass[12pt]{article}\n\\special{papersize=3in,5in}\n\\usepackage[utf8]{inputenc}\n\\usepackage{amssymb,amsmath}\n\\pagestyle{empty}\n\\setlength{\\parindent}{0in}\n\\begin{document}\n",
              "latexPost": "\\end{document}", "mod": 1625636190, "usn": 0, "vers": [], "type": 0,
              "name": "",  # TBD
              # please append other css on the tail
              "css": ".card {\n  font-family: arial;\n  font-size: 20px;\n  text-align: center;\n  color: black;\n  background-color: white;\n}\n",
              "flds": [],  # TBD, BASE_FIELD
              "tmpls": [],  # TBD, BASE_TMPL
              "tags": [],
              "id": "",  # TBD
              "req": [[0, "all", [0]]], "latexsvg": False}

BASE_CONF = {"activeDecks": [1], "curDeck": 1, "newSpread": 0, "collapseTime": 1200, "timeLim": 0, "estTimes": True,
             "dueCounts": True, "curModel": "TBD", "nextPos": 1, "sortType": "noteFld",
             "sortBackwards": False, "addToCur": True, "dayLearnFirst": False, "newBury": True}

SCHEMA_VERSION = 11
