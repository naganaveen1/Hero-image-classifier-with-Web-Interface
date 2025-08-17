function predict() {
    const fileInput = document.getElementById("fileInput");
    const result = document.getElementById("result");

    if (fileInput.files.length === 0) {
        result.innerText = "Please choose a file!";
        result.style.color = "red";
        return;
    }

    const formData = new FormData();
    formData.append("file", fileInput.files[0]);

    fetch("/predict", {
        method: "POST",
        body: formData
    })
    .then(res => res.json())
    .then(data => {
        if (data.error) {
            result.innerText = "Error: " + data.error;
            result.style.color = "red";
        } else {
            result.innerText = "Predicted Hero: " + data.prediction;
            result.style.color = "green";
        }
    })
    .catch(err => {
        result.innerText = "Error: " + err;
        result.style.color = "red";
    });
}

document.getElementById("fileInput").addEventListener("change", function(event) {
    const file = event.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
            document.getElementById("preview").src = e.target.result;
        };
        reader.readAsDataURL(file);
    }
});
