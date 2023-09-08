function obtenerClimaEnChile() {
  var apiKey = "91542ac12986a6d893fb9a79aacfcaeb";
  var url = "https://api.openweathermap.org/data/2.5/weather?q=Chile&appid=" + apiKey;
  
  fetch(url)
    .then(response => response.json())
    .then(data => {
      console.log(data);
      document.getElementById("demo").innerHTML = "La temperatura en " + data.name + " es de " + (data.main.temp - 273.15).toFixed(2) + "°C";
    });
}

document.addEventListener("DOMContentLoaded", obtenerClimaEnChile);
