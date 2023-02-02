
const API_URL = 'http://127.0.0.1:5000/api/eventos';
let eventos = [];
let deleteId = '';


window.addEventListener('DOMContentLoaded', () => {
  geteventos();
})


const valores = document.querySelector('#formUsuario #idUsuario').value;
console.log(valores)

const geteventos = () => {
  fetch(API_URL+'/'+valores)
  .then(response => response.json())
  .catch(error => {
   // alertManager('error', 'Ocurrión un problema al cargar los eventos');
  })
  .then(data => {
    eventos = data;
    renderResult(eventos);
  })
}

const eventosList = document.querySelector('#eventosList');

const renderResult = (eventos) => {
  let listHTML = "";
  eventos.forEach(evento => {
    listHTML += `
      <div class="card">
        <div>Nombre del evento: ${evento.nombreEvento}</div>
        <div>Fecha de Inicio: ${evento.fechaInicio}</div>
        <div>Fecha de Fin: ${evento.fechaFin}</div>
        <div class="options">
          <button type="button" onclick="editEvento(${evento.idEvento})">Editar</button>
          <button type="button" onclick="deleteEvento(${evento.idEvento})">Eliminar</button>
        </div>
      </div>
    `
  })
  eventosList.innerHTML = listHTML;
}

const createEvento = () => {
  const formData = new FormData(document.querySelector('#formAdd'));

  if(!formData.get('nombreEvento') || !formData.get('fechaInicio') || !formData.get('fechaFin')) {
    document.querySelector('#msgFormAdd').innerHTML = '* Llena todos los campos';
    return;
  }
 
  document.querySelector('#msgFormAdd').innerHTML = '';

  const evento = {
    nombreEvento: formData.get('nombreEvento'),
    fechaInicio: formData.get('fechaInicio'),
    fechaFin: formData.get('fechaFin'),
    idUsuario: valores,
  }

  console.log(evento)

  fetch(API_URL +'/add' , {
    method: 'POST',
    body: JSON.stringify(evento),
    headers: {
      'Content-Type': 'application/json'
    }
  })
  .then(res => res.json())
  .catch(error => {
    alertManager('error', error);
    document.querySelector('#formAdd').reset();
  })
  .then(response => {
    alertManager('success', response.mensaje)
    geteventos();
  })
}

const editEvento = (idEvento) => {
  let evento = {};
  eventos.filter(event => {
    if(event.idEvento == idEvento){
      evento = event
    }
  });

  document.querySelector('#formEdit #nombreEvento').value = evento.nombreEvento;
  document.querySelector('#formEdit #fechaInicio').value = evento.fechaInicio;
  document.querySelector('#formEdit #fechaFin').value = evento.fechaFin;
  document.querySelector('#formEdit #idEvento').value = evento.idEvento;

  console.log(idEvento);
  openModalEdit();
}


const updateEvento = () => {
  const evento = {
    nombreEvento: document.querySelector('#formEdit #nombreEvento').value,
    fechaInicio: document.querySelector('#formEdit #fechaInicio').value,
    fechaFin: document.querySelector('#formEdit #fechaFin').value,
    idEvento: document.querySelector('#formEdit #idEvento').value,
    idUsuario: valores,
  }

 
  if(!evento.nombreEvento || !evento.fechaInicio || !evento.fechaFin) {
    document.querySelector('#msgFormEdit').innerHTML = '* Llena todos los campos';
    return;
  }
 
  document.querySelector('#msgFormEdit').innerHTML = '';

  fetch(API_URL+'/update/'+evento.idEvento, {
    method: 'PUT',
    body:JSON.stringify(evento),
    headers: {
      'Content-Type': 'application/json'
    }
  })
  .then(res => res.json())
  .catch(error => {
    alertManager('error', error);
  })
  .then(response => {
    alertManager('success', response.mensaje);
    geteventos();
  });
  document.querySelector('#formEdit').reset();
}

const deleteEvento = (idEvento) => {

  let evento = {};
  eventos.filter(event => {
    if(event.idEvento == idEvento){
      evento = event
    }
  });

  fetch(API_URL+'/delete/'+evento.idEvento, {
    method: 'DELETE'
  })
  .then(res => res.json())
  .catch(error => {
    alertManager('error', error);
  })
  .then(response => {
    alertManager('success', response.mensaje);
    closeModalConfirm();
    geteventos();
    deleteId = '';
  })

}







// MODAL ADD MANAGER
/** --------------------------------------------------------------- */
const btnAdd = document.querySelector('#btnAdd');
const modalAdd = document.querySelector('#modalAdd');

btnAdd.onclick = () => openModalAdd();

window.onclick = function(event) {
  if (event.target == modalAdd) {
    //modalAdd.style.display = "none";
  }
}

const closeModalAdd = () => {
  modalAdd.style.display = 'none';
}

const openModalAdd = () => {
  modalAdd.style.display = 'block';
}

// MODAL ADIT MANAGER
/** --------------------------------------------------------------- */
const modalEdit = document.querySelector('#modalEdit');

const openModalEdit = () => {
  modalEdit.style.display = 'block';
}

const closeModalEdit = () => {
  modalEdit.style.display = 'none';
}

window.onclick = function(event) {
  if (event.target == modalEdit) {
    //modalEdit.style.display = "none";
  }
}

// MODAL CONFIRM MANAGER
/** --------------------------------------------------------------- */
const modalConfirm = document.getElementById('modalConfirm');

window.onclick = function(event) {
  if (event.target == modalConfirm) {
    modalConfirm.style.display = "none";
  }
}

const closeModalConfirm = () => {
  modalConfirm.style.display = 'none';
}

const openModalConfirm = (id) => {
  deleteEvento(id);
  //modalConfirm.style.display = 'block';
}


/** ALERT */
const alertManager = (typeMsg, message) => {
  const alert = document.querySelector('#alert');

  alert.innerHTML = message || 'Se produjo cambios';
  alert.classList.add(typeMsg);
  alert.style.display = 'block';

  setTimeout(() => {
    alert.style.display = 'none';
    alert.classList.remove(typeMsg);
  }, 3500);

}
