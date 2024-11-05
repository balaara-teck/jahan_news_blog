
//  for showing or hiding password
function togglePassword() {
    const passwordField = document.getElementById('id_password');
    const passwordIcon = document.getElementById('password-icon');
    
    if (passwordField.type === 'password') {
        passwordField.type = 'text'; 
        passwordIcon.classList.remove('fa-eye'); 
        passwordIcon.classList.add('fa-eye-slash');
    } else {
        passwordField.type = 'password'; 
        passwordIcon.classList.remove('fa-eye-slash'); 
        passwordIcon.classList.add('fa-eye');
    }
}


function execCommand(command) {
    document.execCommand(command, false, null);
}

document.querySelector(".news-editor-form").addEventListener("submit", function(event) {
    const editorContent = document.getElementById("editor").innerText;
    document.getElementById("body").value = editorContent;
});

// for handling image preview
function previewImage(event) {
    const previewContainer = document.getElementById("image-preview-container");
    const previewImage = document.getElementById("image-preview");
    
    const file = event.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
            previewImage.src = e.target.result;
            previewContainer.style.display = "block";
        };
        reader.readAsDataURL(file);
    } else {
        previewContainer.style.display = "none";
    }
}

const currentYear = new Date().getFullYear();
  document.querySelector('.year').textContent = currentYear;

// for comments limmit in detail.html





