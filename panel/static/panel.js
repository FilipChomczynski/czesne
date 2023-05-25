const elementsToDisable = [
    document.querySelector("#students-table"),
    document.querySelector("#status-table"),
    document.querySelector("#students-form"),
    document.querySelector("#status-form")]

function changeData(event) {
    const btnText = event;

    elementsToDisable.forEach(element=>{
        element.classList.toggle("disabled");
    })

    btnText.innerText = btnText.innerText == "Uczniowie" ? "Status": "Uczniowie";
}

function submitForm() {
   const frm = document.getElementsByName('add-student-form')[0];
   frm.submit();
   fmr.reset();
   return false;
}