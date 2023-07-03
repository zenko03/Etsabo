var map = L.map('map').setView([0, 0], 13); // Default view, will be updated with user's location

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
	attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors',
	maxZoom: 18,
}).addTo(map);

$.ajax({
	url: 'https://api.ipify.org?format=json',
	method: 'GET',
	dataType: 'json',
	success: function (data) {
		var ipAddress = data.ip;
		$.getJSON("https://ipfind.co/?ip=" + ipAddress + "&auth=4ab77373-9453-4a68-b1fc-22c2321a08bc", function (result) {
			var latitude = result.latitude;
			var longitude = result.longitude;

			// Request pharmacy data from Overpass API
			var overpassAPIUrl = "https://overpass-api.de/api/interpreter";
			var overpassQuery = `
		  [out:json];
		  (
			node["amenity"="pharmacy"](around:5000,${latitude},${longitude});
			way["amenity"="pharmacy"](around:5000,${latitude},${longitude});
			relation["amenity"="pharmacy"](around:5000,${latitude},${longitude});
		  );
		  out center;
		`;

			$.ajax({
				url: overpassAPIUrl,
				method: "POST",
				dataType: "json",
				data: {
					data: overpassQuery
				},
				success: function (data) {
					if (data.elements.length > 0) {
						var pharmacies = data.elements;
						console.log("Closest pharmacies:", pharmacies);



						pharmacies.forEach(function (pharmacy) {
							var pharmacyLat = pharmacy.lat;
							var pharmacyLon = pharmacy.lon;

							console.log([pharmacyLat, pharmacyLon])

							if (pharmacyLat != undefined || pharmacyLon != undefined) {
								L.marker([pharmacyLat, pharmacyLon]).addTo(map).bindPopup("Pharmacy");
							}

						});
					} else {
						console.log("No pharmacies found nearby.");
					}
				},
				error: function (error) {
					console.log("Error:", error);
				}
			});

			// Panning the map
			map.panTo(L.latLng(latitude, longitude))

			setTimeout(() => {
				map.setZoom(26)
			}, 1000)
		});
	},
	error: function (error) {
		console.log("Error:", error);
	}
});