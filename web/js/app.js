const button = document.querySelector("button");
const modal = document.getElementById("processing-modal");

button.addEventListener("click", () => {
  modal.style.display = "flex";
  
  pywebview.api.authenticate().then(response => {
    modal.style.display = "none";
    if (response == true) {
      alert("Success!");
    }
    else {
      alert("Failure!");
    }
  });
});
