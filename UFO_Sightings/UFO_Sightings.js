//Definitions
var current_page = 1;
var records_per_page = 10;
var filteredData = dataSet;
var numPages = filteredData.length / records_per_page;
var btn_next = document.getElementById("btn_next");
var btn_prev = document.getElementById("btn_prev");
var page_span = document.getElementById("page");


// Page Button functions
function prevPage() {
    if (current_page > 1) {
        current_page--;
        changePage(current_page);
    }
}

function nextPage() {
    if (current_page < numPages) {
        current_page++;
        changePage(current_page);
    }
}

// Render Table function
function renderTable() {
    $tbody.innerHTML = "";
    var first_record = (current_page - 1) * records_per_page;
    for (var i = 0; i < records_per_page; i++) {
        var data = filteredData[first_record];

        // only insert data if exists
        if (data != null) {
            var fields = Object.keys(data);

            // Create a new row in the tbody, set the index to be i + startingIndex
            var $row = $tbody.insertRow(i);
            for (var j = 0; j < fields.length; j++) {
                // For every field in the address object, create a new cell at set its inner text to be the current value at the current address's field
                var field = fields[j];
                var $cell = $row.insertCell(j);

                response = data[field];
                $cell.innerText = capitalizeFirstLetters(response);


            }
            first_record++;
        }
    }
}

// Change Page function
function changePage(page) {
    // Validate page
    current_page = page;
    if (page < 1) current_page = 1;
    if (page > numPages) current_page = numPages;

    // reduce max pages based on filters
    numPages = Math.round(filteredData.length / records_per_page);

    // show or hide Previous and Next buttons depending on whether on first or last page of results
    page_span.innerHTML = current_page + "/" + numPages;

    if (page == 1) {
        btn_prev.style.visibility = "hidden";
    } else {
        btn_prev.style.visibility = "visible";
    }

    if (page == numPages) {
        btn_next.style.visibility = "hidden";
    } else {
        btn_next.style.visibility = "visible";
    }

    renderTable();

}


function capitalizeFirstLetters(str) {
    return str.toString().toLowerCase().replace(/^\w|\s\w/g, function(letter) {
        return letter.toString().toUpperCase();
    })
}


window.onload = function() {
    changePage(1);
};


//Filters


// Get references to the tbody element, input field and button
var $tbody = document.querySelector("tbody");
var $datetimeInput = document.querySelector("#datetime");
var $cityInput = document.querySelector("#city");
var $stateInput = document.querySelector("#state");
var $countryInput = document.querySelector("#country");
var $shapeInput = document.querySelector("#shape");
var $searchBtn = document.querySelector("#search");
var $citysearchBtn = document.querySelector("#citysearch");
var $statesearchBtn = document.querySelector("#statesearch");
var $countrysearchBtn = document.querySelector("#countrysearch");
var $shapesearchBtn = document.querySelector("#shapesearch");
var $resetsearchBtn = document.querySelector("#resetsearch");

// Add an event listener to the searchButton, call handleSearchButtonClick when clicked
$searchBtn.addEventListener("click", handleSearchButtonClick);
$citysearchBtn.addEventListener("click", handleCityButtonClick);
$statesearchBtn.addEventListener("click", handleStateButtonClick);
$countrysearchBtn.addEventListener("click", handleCountryButtonClick);
$shapesearchBtn.addEventListener("click", handleShapeButtonClick);
$resetsearchBtn.addEventListener("click", handleResetButtonClick);


function handleSearchButtonClick() {
    // Format the user's search by removing leading and trailing whitespace, lowercase the string
    var filterDateTime = $datetimeInput.value.trim().toLowerCase();

    // Set filteredData to an array of all data whose "DateTime" matches the filter
    filteredData = filteredData.filter(function(data) {
        var dataDateTime = data.datetime.toLowerCase();

        // If true, add the data to the filteredData, otherwise don't add it to filteredData
        return dataDateTime === filterDateTime;
    });
    changePage(1);

}

function handleCityButtonClick() {
    // Format the user's search by removing leading and trailing whitespace, lowercase the string
    var filterCity = $cityInput.value.trim().toLowerCase();

    // Set filteredData to an array of all data whose "City" matches the filter
    filteredData = filteredData.filter(function(data) {
        var dataCity = data.city.toLowerCase();

        // If true, add the data to the filteredData, otherwise don't add it to filteredData
        return dataCity === filterCity;
    });
    changePage(1);

}

function handleStateButtonClick() {
    // Format the user's search by removing leading and trailing whitespace, lowercase the string
    var filterState = $stateInput.value.trim().toLowerCase();

    // Set filteredData to an array of all data whose "State" matches the filter
    filteredData = filteredData.filter(function(data) {
        var dataState = data.state.toLowerCase();

        // If true, add the data to the filteredData, otherwise don't add it to filteredData
        return dataState === filterState;
    });
    changePage(1);

}

function handleCountryButtonClick() {
    // Format the user's search by removing leading and trailing whitespace, lowercase the string
    var filterCountry = $countryInput.value.trim().toLowerCase();

    // Set filteredData to an array of all data whose "Country" matches the filter
    filteredData = filteredData.filter(function(data) {
        var dataCountry = data.country.toLowerCase();

        // If true, add the data to the filteredData, otherwise don't add it to filteredData
        return dataCountry === filterCountry;
    });
    changePage(1);

}

function handleShapeButtonClick() {
    // Format the user's search by removing leading and trailing whitespace, lowercase the string
    var filterShape = $shapeInput.value.trim().toLowerCase();

    // Set filteredData to an array of all data whose "Shape" matches the filter
    filteredData = filteredData.filter(function(data) {
        var dataShape = data.shape.toLowerCase();

        // If true, add the data to the filteredData, otherwise don't add it to filteredData
        return dataShape === filterShape;
    });
    changePage(1);

}

// function to reset page
function handleResetButtonClick() {
    location.reload();

}