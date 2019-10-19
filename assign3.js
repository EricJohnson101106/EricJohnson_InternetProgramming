// Thinking I will make a global array that will be initialized to an empty string
// When the cell is created, it should pull the value from the array. The initial
// creation of a cell will then be an empty string.
// However, if a row is deleted, it will first copy the elements in the textbox
// into the array for storage. If the cell is recreated, then it will again pull
// the value from the global array.
// The idea is the index of the row (or cell? need to confirm) will be used to
// pull the values or assign to the correct array position
// How large to make the array? Nvm, can do a dynamic array I believe


var index = 0;
var cellContents = [""];


function ejAddCell() {
    var table = document.getElementById("assign3Table");
    var row = table.insertRow();
    var cell1 = row.insertCell(0);
    var cell2 = row.insertCell(1);
    cell2.innerHTML = "<p>";
    var textbox = document.createElement("input");


    cell1.appendChild(textbox);
    //on input within textbox, update the count
    textbox.addEventListener("input", function () {
        ejTextboxCount(cell2, textbox)
    });

    index++;
    //fill textbox with contents from array
    if (cellContents[index - 1] == null) {
        textbox.value = "";
        cell2.innerText = "0"; //initialize to 0 to be overwritten later
    }
    else {
        textbox.value = cellContents[index - 1];
        ejTextboxCount(cell2, textbox);
    }

}

function ejRemoveCell() {
    var table = document.getElementById("assign3Table");
    var lastRow = table.rows.length - 1;
    var lastRowContents = table.rows[lastRow].cells[0].childNodes[0].value;

    //Put contents of last row text box into the global array cellContents
    //First, check if index is null, if so then push onto the array
    //else add the contents into the array at the index
    if (cellContents[index - 1] == null) {
        cellContents.push(lastRowContents);
    }
    else {
        cellContents[index - 1] = lastRowContents;
    }

    //prevent the last textbox (at index 1) from being deleted. Prevent the index from decrementing as well
    if (lastRow > 1) {
        table.deleteRow(lastRow);
        index--;
    }
}

function ejSort() {
    //We need to sort the visible strings, so we should only sort the array between 0 and index.
    //Everything else is ignored
    //Will make a local array initialized as empty.
    //Will iterate through the strings in the visible text boxes and push them into the local array.
    //Then, we will sort the local array. After sorted, we will iterate through the local array, replacing contents
    //in global array with contents in local array while also updating the textbox values with the values from
    //the now sorted array

    var tempArray = [];
    var table = document.getElementById("assign3Table");
    var i;

    for (i = 0; i < index; i++) {
        tempArray.push(table.rows[i + 1].cells[0].childNodes[0].value);
    }
    tempArray.sort();
    for (i = 0; i < index; i++) {
        cellContents[i] = tempArray[i];
        table.rows[i + 1].cells[0].childNodes[0].value = cellContents[i];
    }
}

function ejTextboxCount(cell2, textbox) {
    cell2.innerText = textbox.value.length;
}


