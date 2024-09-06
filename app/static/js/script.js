document.getElementById("getDataButton").addEventListener("click", function() {
    fetch('/api/data')
        .then(response => response.json())
        .then(data => {
            document.getElementById("dataDisplay").textContent = data.message;
        })
        .catch(error => console.error('Error:', error));
});


document.addEventListener('DOMContentLoaded', function () {
    const dropdown = document.querySelector('.dropdown');
    const container = document.querySelector('.container');

    dropdown.addEventListener('mouseover', function () {
        container.style.marginTop = '100px'; // Aumenta el espacio cuando se pasa el cursor sobre el dropdown
    });

    dropdown.addEventListener('mouseout', function () {
        container.style.marginTop = '20px'; // Vuelve al espacio original cuando se retira el cursor
    });
});

document.body.style.backgroundColor = "lightblue";
