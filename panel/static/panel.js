function changeData(event) {
    const btnText = event;
    const status = document.querySelector("#students-table");
    const students = document.querySelector("#status-table");

    status.classList.toggle("disabled");
    students.classList.toggle("disabled");

    btnText.innerText = btnText.innerText == "Uczniowie" ? "Status": "Uczniowie";
}

function submitForm() {
   const frm = document.getElementsByName('add-student-form')[0];
   frm.submit();
   fmr.reset();
   return false;
}