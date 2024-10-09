// Obtener los elementos del DOM
const searchIcon = document.getElementById('search-icon');
const searchContainer = document.getElementById('search-container');
const closeIcon = document.getElementById('close-icon');
const searchOverlay = document.getElementById('search-overlay');

// Mostrar el contenedor de búsqueda y el overlay al hacer clic en la lupa
searchIcon.addEventListener('click', function() {
    searchContainer.classList.add('active');
    searchOverlay.classList.add('active'); // Muestra el overlay
});

// Cerrar el contenedor de búsqueda y ocultar el overlay al hacer clic en la "X"
closeIcon.addEventListener('click', function() {
    searchContainer.classList.remove('active');
    searchOverlay.classList.remove('active'); // Oculta el overlay
});

document.addEventListener('DOMContentLoaded', function () {
    let initialDataElement = document.getElementById('graph');
    let initialData = JSON.parse(initialDataElement.getAttribute('data-initial-data'));

    let layout = {
        title: 'Visualización de Embeddings para Razas de Perros',
        scene: {
            xaxis: { title: 'PC1' },
            yaxis: { title: 'PC2' },
            zaxis: { title: 'PC3' }
        }
    };

    // Crear gráfica inicial
    Plotly.newPlot('graph', initialData, layout);

    const form = document.getElementById('textForm');
    const closestPointInfo = document.getElementById('closestPointInfo');

    form.addEventListener('submit', function (event) {
        event.preventDefault();
        const formData = new FormData(form);
        const searchedWord = formData.get('text_input');

        fetch("/visualize", {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            // Limpia las trazas anteriores
            Plotly.deleteTraces('graph', [1, 2]);

            // Agrega nueva traza con el nuevo punto y el punto más cercano
            const newPoint = {
                x: [data.new_vector[0]],
                y: [data.new_vector[1]],
                z: [data.new_vector[2]],
                mode: 'markers+text',
                type: 'scatter3d',
                marker: { size: 5, color: 'red' },
                text: ['Nuevo: ' + searchedWord],
                textposition: 'top center',
                name: searchedWord  // Aquí agregamos el nombre en la leyenda
            };

            const closestPoint = {
                x: [initialData[0].x[data.closest_index]],
                y: [initialData[0].y[data.closest_index]],
                z: [initialData[0].z[data.closest_index]],
                mode: 'markers+text',
                type: 'scatter3d',
                marker: { size: 5, color: 'green' },
                text: ['Cercano: ' + data.closest_title],
                textposition: 'top center',
                name: 'Punto más cercano: ' + data.closest_title
            };

            Plotly.addTraces('graph', [newPoint, closestPoint]);
            closestPointInfo.innerHTML = `La raza más cercana a <strong>${searchedWord}</strong> es <strong>${data.closest_title}</strong> a una distancia de <strong>${data.closest_distance.toFixed(2)}</strong>`;
        })
        .catch(error => console.error('Error:', error));
    });

    // Añadir funcionalidad de menú seleccionable
    const menuItems = document.querySelectorAll('.dropdown-link, .sub-dropdown-link');

    menuItems.forEach(item => {
        item.addEventListener('click', function() {
            // Elimina la clase active de todos los elementos
            menuItems.forEach(link => link.classList.remove('active'));

            // Añade la clase active a la subsección seleccionada y su sección principal
            item.classList.add('active');

            // Si es una subsección, también añade la clase active a su padre (sección principal)
            const parentDropdown = item.closest('.dropdown');
            if (parentDropdown) {
                const parentLink = parentDropdown.querySelector('.dropdown-link');
                if (parentLink) {
                    parentLink.classList.add('active');
                }
            }
        });
    });
});
