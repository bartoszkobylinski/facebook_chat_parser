const usersList = JSON.parse(document.getElementById('users_list').textContent);
const messagesList = JSON.parse(document.getElementById('messages_list').textContent);
const charactersList = JSON.parse(document.getElementById('characters_list').textContent);
const wordsList = JSON.parse(document.getElementById('words_list').textContent);
const photosList = JSON.parse(document.getElementById('photos_list').textContent);
const linksList = JSON.parse(document.getElementById('links_list').textContent);
const gifsList = JSON.parse(document.getElementById('gifs_list').textContent);
const backgroundColorsList = JSON.parse(document.getElementById('charts_colors_list').textContent);
const bordersColorsList = JSON.parse(document.getElementById('borders_color_list').textContent);



var ctx = document.getElementById('myChartMessages').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'doughnut',
    data: {
        labels: usersList,
        datasets: [{
            label: 'oooooooooooooooooooooooooooo',
            data: messagesList,
            backgroundColor: backgroundColorsList,
            borderColor: bordersColorsList,
            borderWidth: 1
        }]
    },

    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        }
    }
});
// next chart
var ctx = document.getElementById('myChartCharacters').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'pie',
    data: {
        labels: usersList,
        datasets: [{
            label: '',
            data: charactersList,
            backgroundColor: backgroundColorsList,
            borderColor: bordersColorsList,
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        }
    }
});
//next chart
var ctx = document.getElementById('myChartWords').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'doughnut',
    data: {
        labels: usersList,
        datasets: [{
            label: '',
            data: wordsList,
            backgroundColor: backgroundColorsList,
            borderColor: bordersColorsList,
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        }
    }
});
//next chart
var ctx = document.getElementById('myChartPhotos').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: usersList,
        datasets: [{
            label: 'Photos number',
            data: photosList,
            backgroundColor: backgroundColorsList,
            borderColor: bordersColorsList,
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        }
    }
});
// next chart
var ctx = document.getElementById('myChartLinks').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: usersList,
        datasets: [{
            label: 'Links number',
            data: linksList,
            backgroundColor: backgroundColorsList,
            borderColor: bordersColorsList,
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        }
    }
});
// next chart
var ctx = document.getElementById('myChartGifs').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: usersList,
        datasets: [{
            label: 'Gifs numbers',
            data: gifsList,
            backgroundColor: backgroundColorsList,
            borderColor: bordersColorsList,
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        }
    }
});
