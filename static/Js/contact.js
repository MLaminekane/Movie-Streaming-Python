// Récupération des éléments du formulaire
const form = document.querySelector('form');
const nameInput = document.querySelector('#name');
const emailInput = document.querySelector('#email');
const messageInput = document.querySelector('#message');

// Fonction pour valider le formulaire
function validateForm() {
  let errors = 0;
  if (nameInput.value.trim() === '') {
    nameInput.classList.add('shake');
    errors++;
  }
  if (emailInput.value.trim() === '') {
    emailInput.classList.add('shake');
    errors++;
  }
  if (messageInput.value.trim() === '') {
    messageInput.classList.add('shake');
    errors++;
  }
  if (errors > 0) {
    setTimeout(() => {
      nameInput.classList.remove('shake');
      emailInput.classList.remove('shake');
      messageInput.classList.remove('shake');
    }, 300);
    return false;
  }
  return true;
}

// Écouteur d'événement pour soumettre le formulaire
form.addEventListener('submit', (event) => {
  if (!validateForm()) {
    event.preventDefault();
  }
});
