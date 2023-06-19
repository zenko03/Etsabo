var map = L.map('map').setView([0, 0], 13); // Default view, will be updated with user's location

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors',
  maxZoom: 18,
}).addTo(map);

// Get user's location using browser geolocation API
document.getElementById('locate-btn').addEventListener('click', function() {
    fetch("https://www.googleapis.com/geolocation/v1/geolocate?key=").then((response) => {
        console.log(response);
    })
});
