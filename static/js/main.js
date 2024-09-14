function separarInformacoes(str) {
  const regex = /^(\S+) - (.+?)\((\d+H)\)$/;
  const match = str.match(regex);
  if (match) {
    return {
      codigo: match[1],
      nome: match[2],
      cargaHoraria: match[3]
    };
  } else {
    return {
      codigo: str,
      nome: '',
      cargaHoraria: ''
    };
  }
}

const disciplinas = document.querySelectorAll('.disciplina-name');

disciplinas.forEach((element) => {
  const info = separarInformacoes(element.textContent);
  if (info) {element.innerHTML = info.nome}
})

const selectElement = document.getElementById('id_periodos');

selectElement.addEventListener('change', function() {
  const form = document.getElementById('id_boletim_form');
  form.submit();
});