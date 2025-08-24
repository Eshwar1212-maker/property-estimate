const form = document.getElementById("estimateForm");
const spinner = document.getElementById("spinner");
const btnText = document.getElementById("btnText");
const submitBtn = document.getElementById("submitBtn");

window.addEventListener("pageshow", () => {
  spinner.classList.add("hidden");
  btnText.textContent = "Get Estimate";
  submitBtn.disabled = false;
});

form.addEventListener("submit", () => {
  spinner.classList.remove("hidden");
  btnText.textContent = "AI is generating..";
  submitBtn.disabled = true;
});
