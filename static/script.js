function approveStudent(name) {

    alert(
        name +
        "'s career guidance has been marked for approval."
    );
}


function addNote(name) {

    const note = prompt(
        "Enter counselor note for " + name + ":"
    );

    if (note) {

        alert(
            "Note saved for this practice demo: " +
            note
        );
    }
}