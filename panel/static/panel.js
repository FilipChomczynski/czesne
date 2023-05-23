function changeData(event) {
    const btnText = event;
    const status = document.querySelector("#students-table");
    const students = document.querySelector("#status-table");

    status.classList.toggle("disabled-table");
    students.classList.toggle("disabled-table");

    btnText.innerText = btnText.innerText == "Uczniowie" ? "Status": "Uczniowie";
}

function submitForm() {
   const frm = document.getElementsByName('add-student-form')[0];
   frm.submit();
   fmr.reset();
   return false;
}