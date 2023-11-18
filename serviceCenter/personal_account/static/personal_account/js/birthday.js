
var birthDate = NaN;
var today = new Date;
while (isNaN(birthDate) || birthDate > today) {
    var prom = prompt("Enter tour birth date:");
    birthDate = new Date(prom);
}
if (prom !== null) {
    var age = today.getFullYear() - birthDate.getFullYear();
    if (age >= 18) {
        var weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
        var dayOfWeek = weekdays[birthDate.getDay()];
        alert("You are an adult. The day of the week for your birth date is: " + dayOfWeek);
    } else {
        alert("You are a minor. Parental consent is required to use this website.");
    }
}