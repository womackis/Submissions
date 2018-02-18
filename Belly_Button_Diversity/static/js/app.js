/* data route */
var url = "/samples/<sample>";

function buildPlot() {
    Plotly.d3.json(url, function(error, response) {

        console.log(response);
        var trace1 = {
            type: "scatter",
            mode: "lines",
            name: "Belly Button Diversity",
            x: response.map(sample => sample.otu_id),
            y: response.map(sample => sample.sample_value),
            line: {
                color: "#17BECF"
            }
        };

        var sample = [trace1];

        var layout = {
            title: "Belly Button Diversity",
            xaxis: {
                type: "linear"
            },
            yaxis: {
                autorange: true,
                type: "linear"
            }
        };

        Plotly.newPlot("plot", sample, layout);
    });
}

buildPlot();