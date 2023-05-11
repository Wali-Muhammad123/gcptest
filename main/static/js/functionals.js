const radios = document.querySelectorAll('input[type="radio"]');
const textInput = document.querySelector('#investbox');

// Disable text input when any radio button is checked
for (let radio of radios) {
  radio.addEventListener('change', () => {
    if (radio.checked) {
      textInput.disabled = true;
    } else {
      textInput.disabled = false;
    }
  });
}

// Uncheck all radio buttons when text input is added
textInput.addEventListener('input', () => {
  for (let radio of radios) {
    radio.checked = false;
  }
});
