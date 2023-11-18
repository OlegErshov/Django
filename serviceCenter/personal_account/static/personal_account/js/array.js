// app.js

function findLatestDate() {
    var dates = {
      "date1": document.getElementById('date1').value,
      "date2": document.getElementById('date2').value,
      "date3": document.getElementById('date3').value,
      // Add more dates if needed
    };
  
    var latestDate = getLatestDate(dates);
    document.getElementById('result').innerText = "The latest date is: " + latestDate.toLocaleDateString();
  }
  
  function getLatestDate(dateObject) {
    var latestDate;
  
    for (var key in dateObject) {
      var currentDate = new Date(dateObject[key].split('.').reverse().join('-'));
  
      if (!latestDate || currentDate > latestDate) {
        latestDate = currentDate;
      }
    }
  
    return latestDate;
  }