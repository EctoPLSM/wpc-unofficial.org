# Source code
Run main.py to build the project:
```
python2.7 -B main.py
```

This generates the whole website to the parent folder by filling in the
pages in the templates folder with data from the database folder.

You can generate individual pages with scripts as well.

After adding a new year increment config.py counters.

## Assumptions

CSV files don't strictly obey CSV format. They are literally "comma separated values". Thus, names should not include commas.

##### database/estudiantes.csv:
* Columns: year, unofficial rank (before playoff), name, country code, team tier, official rank (after playoff), U18 rank, O50 rank, rookie rank, total score, scores of each individual rounds.
* Ordered first by year then by rank.
* Don't assume ranks are numbers. They can be in two forms: 1234 or >=1234
* Country-code can be empty if unknown.

##### database/timeline.csv:
* Columns: number, year, date, country code, city, website, # of teams, # of students 
* Ordered by year

##### database/countries.csv:
* Columns: country code, name, website, if former

##### database/teams.csv:
* Columns: year, unofficial rank (before playoff), country code, team tier, official rank (after playoff), total score, total of team rounds, scores of each team rounds, total of individual rounds, scores of each individual rounds.

##### database/rounds.csv:
* Columns: year, date, time, number, name, duration, max points.
* Asterisk indicates that max points can't be defined from instructions alone. (e.g. optimisers.) Top score is shown instead.
