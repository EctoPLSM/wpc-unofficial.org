// Requries asciify.js

(function () {
    if (typeof(asciify) != "function") {
        console.error("asciify not imported!");
        return;
    }
    var countries = null;
    var students = null;
    function loadCountries() {
        var xmlhttp = new XMLHttpRequest();
        xmlhttp.open("GET", "countries.csv", true);
        xmlhttp.overrideMimeType("text/plain");
        xmlhttp.onreadystatechange = function() {
            // Let's ignore xmlhttp.status as it doesn't work local
            if(xmlhttp.readyState == 4 && xmlhttp.responseText != null) {
                countries = [];
                countries[""] = "";
                var tx = xmlhttp.responseText;
                var lines = tx.split("\n");
                for(var i = 0; i < lines.length; i++) {
                    var ps = lines[i].split(",");
                    if (ps.length > 2) {
                        countries[ps[0]] = ps[1];
                    }
                }
            }
        }
        xmlhttp.send();
    }
    function loadStudents() {
        var xmlhttp = new XMLHttpRequest();
        xmlhttp.open("GET", "participants.csv", true);
        xmlhttp.overrideMimeType("text/plain");
        xmlhttp.onreadystatechange = function() {
            // Let's ignore xmlhttp.status as it doesn't work local
            if(xmlhttp.readyState == 4 && xmlhttp.responseText != null) {
                students = [];
                var tx = xmlhttp.responseText;
                var lines = tx.split("\n");
                for(var i = 0; i < lines.length; i++) {
                    var ps = lines[i].trim().split(",");
                    if (ps.length > 4) {
                        students.push({
                            year: ps[0],
                            rank: ps[1],
                            name: ps[2],
                            code: ps[3],
                            tier: ps[4],
                            official_rank: ps[5],
                            under_18: ps[6],
                            over_50: ps[7],
                            rookie: ps[8],
                            total_score: ps[9],
                            individual_1: ps[10],
                            individual_2: ps[11],
                            individual_3: ps[12],
                            individual_4: ps[13],
                            individual_5: ps[14],
                            individual_6: ps[15],
                            individual_7: ps[16],
                            individual_8: ps[17],
                            individual_9: ps[18],
                            individual_10: ps[19],
                            individual_11: ps[20],
                            individual_12: ps[21],
                            individual_13: ps[22],
                            individual_14: ps[23],
                            individual_15: ps[24],
                            individual_16: ps[25],
                            individual_17: ps[26],
                            name_ascii_lower: asciify(ps[2]).toLowerCase(),
                        });
                    }
                }
            }
        }
        xmlhttp.send();
    }
    window.wpc_search = function() {
        if(countries == null || students == null) {
          return;
        }
        var html = "";
        var t_row = document.getElementById("t_row").innerHTML;
        var query = document.getElementById("search_query").value;
        query = asciify(query).toLowerCase().trim();
        if(query.length <= 1) {
            return;
        }
        for(var i = 0; i < students.length; i++) {
            if(students[i].name_ascii_lower.indexOf(query) != -1) {
                var row = t_row.replace(/{{name}}/g, students[i].name)
                    .replace(/{{code}}/g, students[i].code)
                    .replace(/{{country}}/g, countries[students[i].code])
                    .replace(/{{team}}/g, students[i].tier)
                    .replace(/{{year}}/g, students[i].year)
                    .replace(/{{official}}/g, students[i].official_rank)
                    .replace(/{{position}}/g, students[i].rank);
                html += "<tr>" + row + "</tr>";
            }
        }
        document.getElementById("search_results").innerHTML = html;
    }
    loadCountries();
    loadStudents();
})();
