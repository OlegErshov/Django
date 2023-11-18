function toggleFontSize() {
    var fontSizeField = document.getElementById('font-size-field');
    fontSizeField.style.display = document.getElementById('font-size-checkbox').checked ? 'block' : 'none';
}

function toggleTextColor() {
    var textColorField = document.getElementById('text-color-field');
    textColorField.style.display = document.getElementById('text-color-checkbox').checked ? 'block' : 'none';
}

function toggleBackgroundColor() {
    var backgroundColorField = document.getElementById('background-color-field');
    backgroundColorField.style.display = document.getElementById('background-color-checkbox').checked ? 'block' : 'none';
}


var form = document.getElementById("form");
form.addEventListener("submit", function (event) {
    event.preventDefault();

    var formData = new FormData(form);

    if (document.getElementById("font-size-checkbox").checked) {
        var fontSize = formData.get("fontSize");
        var paragraphs = document.querySelectorAll(".temp_text");
        for (var i = 0; i < paragraphs.length; i++) {
            paragraphs[i].style.fontSize = fontSize + "px";
        }
    }

    if (document.getElementById("text-color-checkbox").checked) {
        var textColor = formData.get("textColor");
        var paragraphs = document.querySelectorAll(".temp_text");
        for (var i = 0; i < paragraphs.length; i++) {
            paragraphs[i].style.color = textColor;
        }
    }

    if (document.getElementById("background-color-checkbox").checked) {
        var backgroundColor = formData.get("backgroundColor");
        document.body.style.background = backgroundColor;
    }

});