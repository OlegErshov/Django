function getRandomInt(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

function createTable(size) {
    const table = document.getElementById('myTable');
    table.innerHTML = '';

    for (let i = 0; i < size; i++) {
        const row = table.insertRow();
        for (let j = 0; j < size; j++) {
            const cell = row.insertCell();
            cell.textContent = getRandomInt(1, 100);
            cell.style.backgroundColor = '';
        }
    }
}

function highlightCell(cell) {
    const cellValue = parseInt(cell.textContent);
    if (cellValue % 2 === 0) {
        cell.style.backgroundColor = 'red';
    } else {
        cell.style.backgroundColor = 'cyan';
    }
}


function countRedCyanInRowCol(table, row, col) {
    let count = 0;

    for (let i = 0; i < table.rows.length; i++) {
        if (i === row && (table.rows[i].cells[col].style.backgroundColor === 'cyan' || table.rows[i].cells[col].style.backgroundColor === 'red')) {
            count++;
        }
    }
    return count;
}


function canSelectCell(table, row, col, n) {
    let selectedRedCyan = 0;

    for (let i = 0; i < table.rows.length; i++) {
        for (let j = 0; j < table.rows[i].cells.length; j++) {
            if ((i === row || j === col) && !(i === row && j === col)) {
                if (table.rows[i].cells[j].style.backgroundColor === 'cyan' || table.rows[i].cells[j].style.backgroundColor === 'red') {
                    selectedRedCyan++;
                    if ((i === row && Math.abs(j - col) <= 1) || (j === col && Math.abs(i - row) <= 1)) {
                        return false;
                    }
                }
            }
        }
    }

    return selectedRedCyan < n;
}



function selectCellsInRowCol(table, row, col, n) {
    const currentCell = table.rows[row].cells[col];

    if ((currentCell.style.backgroundColor === 'cyan' || currentCell.style.backgroundColor === 'red') && countRedCyanInRowCol(table, row, col) >= n) {
        currentCell.style.backgroundColor = '';
    } else if (canSelectCell(table, row, col, n)) {
        if (currentCell.textContent % 2 === 0) {
            currentCell.style.backgroundColor = 'red';
        } else {
            currentCell.style.backgroundColor = 'cyan';
        }
    }
}


function transposeTable() {
    const table = document.getElementById('myTable');
    const cellColors = [];

    for (let i = 0; i < table.rows.length; i++) {
        cellColors.push([]);
        for (let j = 0; j < table.rows[i].cells.length; j++) {
            cellColors[i][j] = table.rows[i].cells[j].style.backgroundColor;
        }
    }

    const newTable = [];
    for (let i = 0; i < table.rows.length; i++) {
        newTable.push([]);
        for (let j = 0; j < table.rows[i].cells.length; j++) {
            newTable[i][j] = table.rows[j].cells[i].textContent;
        }
    }

    table.innerHTML = '';
    for (let i = 0; i < newTable.length; i++) {
        const row = table.insertRow();
        for (let j = 0; j < newTable[i].length; j++) {
            const cell = row.insertCell();
            cell.textContent = newTable[i][j];
            cell.style.backgroundColor = cellColors[j][i];
        }
    }
}

function addRow() {
    const table = document.getElementById('myTable');
    const newRow = table.insertRow();

    for (let j = 0; j < table.rows[0].cells.length; j++) {
        const cell = newRow.insertCell();
        cell.textContent = getRandomInt(1, 100);
        cell.style.backgroundColor = '';
    }
}

function addColumn() {
    const table = document.getElementById('myTable');
    for (let i = 0; i < table.rows.length; i++) {
        const cell = table.rows[i].insertCell();
        cell.textContent = getRandomInt(1, 100);
        cell.style.backgroundColor = '';
    }
}

document.getElementById('myTable').addEventListener('click', function (event) {
    if (event.target.nodeName === 'TD') {
        const cell = event.target;
        const rowIndex = cell.parentNode.rowIndex;
        const cellIndex = cell.cellIndex;
        const maxCells = parseInt(document.getElementById('maxCells').value);
        selectCellsInRowCol(document.getElementById('myTable'), rowIndex, cellIndex, maxCells);
    }
});

function createNewTable() {
    const tableSize = parseInt(document.getElementById('tableSize').value);
    createTable(tableSize);
}

createNewTable();