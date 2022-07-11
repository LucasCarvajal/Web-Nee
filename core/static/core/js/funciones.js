//$("#cursos").chained("#escuelas");


window.addEventListener('DOMContentLoaded', (e) => {
    fetch(`http://localhost:8000/api/escuela/`, {
        method: 'GET'
    }).then(respuesta => respuesta.json()).then(data => data.forEach(d => {
        let selectEscuela = document.getElementById('escuelas');
        let option = document.createElement('option');
        option.value = d.id_escuela;
        option.innerHTML = d.nombre_escuela;
        selectEscuela.appendChild(option);
    }));
});

function seleccionarCurso() {

    let URL_CURSOS = 'http://localhost:8000/api/curso/';

    let selectEscuela = Number(document.getElementById('escuelas').value);
    let selectCursos = document.getElementById('cursos');

    let optionDefault = document.createElement('option');
    optionDefault.value = -1;
    optionDefault.innerHTML = 'Seleccione Curso';
    optionDefault.selected = true;
    optionDefault.disabled = true;

    selectCursos.innerHTML = "";
    selectCursos.appendChild(optionDefault);

    fetch(URL_CURSOS, { method: 'GET' })
        .then(response => response.json())
        .then(data => data.forEach(d => {
            if (d.escuela === selectEscuela) {
                let optionEscuela = document.createElement('option');
                optionEscuela.value = d.id_curso;
                optionEscuela.innerHTML = d.nomcurso;
                selectCursos.appendChild(optionEscuela);
            }
        }));

}

window.addEventListener('DOMContentLoaded', (e) => {
    fetch(`http://localhost:8000/api/apoderado/`, {
        method: 'GET'
    }).then(respuesta => respuesta.json()).then(data => data.forEach(d => {
        let selectApoderado = document.getElementById('apoderado');
        let option = document.createElement('option');
        option.value = d.id_apoderado;
        option.innerHTML = d.nombre_apoderado;
        selectApoderado.appendChild(option);
    }));
});


