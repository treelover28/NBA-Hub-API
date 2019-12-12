// const axios = require("axios");
var today = new Date().toISOString().split('T')[0];
var date_form = document.getElementsByName("date")[0];
date_form.min = today;
date_form.style.display = "inline-block";
date_form.style.textAlign = "center";
var original_team_form = document.getElementById("team_simulation").cloneNode(true).innerHTML;
var original_date_form = document.getElementById("date_simulation").cloneNode(true).innerHTML;
show_date_result = function () {
    form = document.getElementById("date_simulation");
    // get form data
    // convert form to FormData
    var data = new FormData(form);
    // send POST request to API endpoint/handle_date
    var xhr = new XMLHttpRequest();
    url = "http://127.0.0.1:5000/handle_date";
    xhr.open('POST', url, true);
    // send data
    xhr.send(data);

    // after it finished loading, convert all JSON data into table
    xhr.onload = function () {
        var obj = JSON.parse(this.responseText);
        date = form.elements[0].value;
        var html = "<h3> Predictions for games on " + date + "</h3>";
        //iterating through all the item one by one.
        obj.forEach(function (val) {
            //getting all the keys in val (current array item)
            var keys = Object.keys(val);
            //assigning HTML string to the variable html
            html += "<div class='result_table'><table border='1'>";
            //iterating through all the keys presented in val (current array item)
            keys.forEach(function (key) {
                //appending more HTML string with key and value aginst that key;
                html += "<tr><td><strong>" + key + "</strong></td><td class='data'>" + val[key] + "</td></tr>";
            });
            //final HTML sting is appending to close the DIV element.
            html += "</table></div><br><br>";
        });

        // change form's HTML to display result
        form.innerHTML = html;
        // make reset button appear
        reset_button = document.getElementById("reset");
        reset_button.className = "";
    };

};

function show_team_result() {
    form = document.getElementById("team_simulation");
    // og_form = String(form);
    // name_A = form[0].value;
    // season_A = form[1].value;
    // name_B = form[2].value;
    // season_B = form[3].value;
    // console.log(name_A)
    var data = new FormData(form);

    var xhr = new XMLHttpRequest();
    url = "http://127.0.0.1:5000/handle_teams";
    xhr.open('POST', url, true);
    // send data
    xhr.send(data);
    xhr.onload = function () {
        var obj = JSON.parse(this.responseText);
        // console.log(obj);
        var html = "<h3> Predictions for this matchup </h3>";
        //getting all the keys in val (current array item)
        var keys = Object.keys(obj);
        //assigning HTML string to the variable html
        html += "<div class='result_table'><table border='1'>";
        //iterating through all the keys presented in val (current array item)
        keys.forEach(function (key) {
            //appending more HTML string with key and value aginst that key;
            html += "<tr><td><strong>" + key + "</strong></td><td class='data'>" + obj[key] + "</td></tr>";
        });
        //final HTML sting is appending to close the DIV element.
        html += "</table></div><br><br>";

        form.innerHTML = html;
        // make reset button appear
        reset_button = document.getElementById("reset2");
        reset_button.className = "";
    };
}



function loadFile(fileName) {
    var result = null;
    var request = new XMLHttpRequest();
    request.open("GET", fileName, false);
    request.send();
    console.log(request.statusText);
    if (request.status === 200) {
        result = request.responseText;
    }
    return result;
};

function reset_form() {
    console.log("called");

    form = document.getElementById("date_simulation");
    form.innerHTML = original_date_form;

    reset_button = document.getElementById("reset");
    reset_button.className = "hide";
};

function reset_form2() {
    console.log("called");
    // html = original_team_form;
    // console.log(html);


    form = document.getElementById("team_simulation");
    form.innerHTML = original_team_form;

    reset_button = document.getElementById("reset2");
    reset_button.className = "hide";

};


