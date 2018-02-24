// Store our API endpoint inside queryUrl
var queryUrl = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson";

// second link for techtonicplates
var tectonicUrl = "https://raw.githubusercontent.com/fraxen/tectonicplates/master/GeoJSON/PB2002_boundaries.json";


// Perform a GET request to the query URL
d3.json(queryUrl, function(data) {
    // Once we get a response, send the data.features object to the createFeatures function
    createFeatures(data.features);
});

// Perform a GET request to the tectonic URL
d3.json(tectonicUrl, function(data) {
    // Once we get a response, send the data.features object to the createFeatures function
    tectonicFeatures(data.features);
});


// set colors for each level of magnitude from 1 to 
function getColor(mag) {
    return mag < 1 ? '#FAF200' :
        mag < 2 ? '#EBCE00' :
        mag < 3 ? '#E2B600' :
        mag < 4 ? '#D39100' :
        mag < 5 ? '#CA7900' :
        mag < 6 ? '#BB5500' :
        mag < 7 ? '#AC3000' :
        '#9E0C00';
}

function createFeatures(earthquakeData) {

    // Define a function we want to run once for each feature in the features array
    // Give each feature a popup describing the place and time of the earthquake
    function onEachFeature(feature, layer) {
        layer.bindPopup("<h3>Magnitude: " + feature.properties.mag +
            "</h3><hr><p>Where: " + feature.properties.place + "</p>" +
            "<hr><p>When: " + new Date(feature.properties.time) + "</p>");
    }

    // Create a GeoJSON layer containing the features array on the earthquakeData object
    // Run the onEachFeature function once for each piece of data in the array


    var earthquakes = L.geoJSON(earthquakeData, {
        pointToLayer: function(feature, latlng) {
            return new L.CircleMarker(latlng, {
                fillColor: getColor(feature.properties.mag),
                radius: feature.properties.mag * 3,
                opacity: feature.properties.mag / 6,
                fillOpacity: feature.properties.mag / 3,
                weight: 1,
                color: "black"
            });
        },
        onEachFeature: onEachFeature,

    });

    // Sending our earthquakes layer to the createMap function
    createMap(earthquakes);
}


function tectonicFeatures(tectonicData) {

    // Define a function we want to run once for each feature in the features array
    // Give each feature a popup providing name and source of boundary data
    function onEachFeature(feature, layer) {
        layer.bindPopup("<h3>Tectonic Boundary</h3><hr><p>Name: " + feature.properties.Name +
            "</p><hr><p>Source: " + feature.properties.Source + "</p>").addTo(tectonic1);
    }

    // Create a GeoJSON layer containing the features array on the tectonicData object
    // Run the onEachFeature function once for each piece of data in the array

    var tectonic = L.geoJSON(tectonicData, {
        pointToLayer: function(feature, latlng) {
            return new L.polyline(latlng, {
                className: 'my_polyline'
                    // tried to adjust polyline style but was not successful


            })
        },
        onEachFeature: onEachFeature,

    });


}

var tectonic1 = new L.LayerGroup();


function createMap(earthquakes) {

    // Define streetmap and darkmap layers
    var streetmap = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/outdoors-v10/tiles/256/{z}/{x}/{y}?" +
        "access_token=pk.eyJ1Ijoid29tYWNraXMiLCJhIjoiY2pkaGtxdXE1MHdyNTMzcmw2MmFocmNicCJ9.5dU070fAsJkfmLNDaMbznw");

    var darkmap = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/dark-v9/tiles/256/{z}/{x}/{y}?" +
        "access_token=pk.eyJ1Ijoid29tYWNraXMiLCJhIjoiY2pkaGtxdXE1MHdyNTMzcmw2MmFocmNicCJ9.5dU070fAsJkfmLNDaMbznw");

    var satellite = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/satellite-streets-v9/tiles/256/{z}/{x}/{y}?" +
        "access_token=pk.eyJ1Ijoid29tYWNraXMiLCJhIjoiY2pkaGtxdXE1MHdyNTMzcmw2MmFocmNicCJ9.5dU070fAsJkfmLNDaMbznw");

    // Define a baseMaps object to hold our base layers
    var baseMaps = {
        "Street Map": streetmap,
        "Dark Map": darkmap,
        "Satellite Map": satellite
    };

    // Create overlay object to hold our overlay layer
    var overlayMaps = {
        Earthquakes: earthquakes,
        Tectonics: tectonic1
    };

    // Create our map, giving it the satellite, earthquakes, and tectonic1 layers to display on load
    var myMap = L.map("map", {
        center: [
            37.09, -95.71
        ],
        zoom: 5,
        layers: [satellite, earthquakes, tectonic1]
    });


    // Create a layer control
    // Pass in our baseMaps and overlayMaps
    // Add the layer control to the map
    L.control.layers(baseMaps, overlayMaps, {
        collapsed: false
    }).addTo(myMap);


    // Add a legend for magnitude with color boxes matching circles on map
    var legend = L.control({ position: 'bottomleft' });

    legend.onAdd = function(map) {

        var div = L.DomUtil.create('div', 'info legend'),
            magnitude = [0, 1, 2, 3, 4, 5, 6, 7];


        // create legend title
        div.innerHTML += "<h4><strong>Magnitude</h4><hr>";


        // loop through our density intervals and generate a label with a colored square for each interval
        for (var i = 0; i < magnitude.length; i++) {
            div.innerHTML +=
                '<i style="background:' + getColor(magnitude[i]) + '"></i> ' +
                magnitude[i] + (magnitude[i + 1] ? '&ndash;' + magnitude[i + 1] + '<br>' : '+');
        }

        return div;
    };

    legend.addTo(myMap);







}