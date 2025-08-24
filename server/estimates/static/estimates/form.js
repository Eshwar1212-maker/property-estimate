const form = document.getElementById("estimateForm");
const spinner = document.getElementById("spinner");
const btnText = document.getElementById("btnText");
const submitBtn = document.getElementById("submitBtn");

form.addEventListener("submit", () => {
  spinner.classList.remove("hidden");
  btnText.textContent = "Loading...";
  submitBtn.disabled = true;
});