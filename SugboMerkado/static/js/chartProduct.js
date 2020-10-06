var valueP = JSON.parse(document.getElementById('valProduct').textContent);

//line
var ctxL = document.getElementById("lineChartProduct").getContext('2d');
var myLineChart = new Chart(ctxL, {
    type: 'line',
    data: {
        labels: ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
        datasets: [{
            label: "2020 Product Registration Summary",
            data: valueP,
            backgroundColor: [
            'rgba(0, 137, 132, .2)',
            ],
            borderColor: [
            'rgba(0, 10, 130, .7)',
            ],
            borderWidth: 2 
        },
    ]
    },
    options: {
    responsive: true,
    scales: {
        yAxes: [{
            ticks: {
                min: 0,
                stepSize: 1
            }
        }]
    }
    }
});