const form = document.querySelector("form");
const calculateButton = document.querySelector("input[type='submit']");
calculateButton.addEventListener("click", function(event) {
  event.preventDefault();
  
  const grade1 = Number(document.getElementById("grade1").value);
  const grade2 = Number(document.getElementById("grade2").value);
  const grade3 = Number(document.getElementById("grade3").value);
  const grade4 = Number(document.getElementById("grade4").value);
  const grade5 = Number(document.getElementById("grade5").value);
  const grade6 = Number(document.getElementById("grade6").value);
  const grade7 = Number(document.getElementById("grade7").value);

  const hour1 = Number(document.getElementById("hour1").value);
  const hour2 = Number(document.getElementById("hour2").value);
  const hour3 = Number(document.getElementById("hour3").value);
  const hour4 = Number(document.getElementById("hour4").value);
  const hour5 = Number(document.getElementById("hour5").value);
  const hour6 = Number(document.getElementById("hour6").value);
  const hour7 = Number(document.getElementById("hour7").value);


  const totalHours = 18 ;
  const totalPoints = (grade1 * hour1) + (grade2 * hour2) + (grade3 * hour3) + (grade4 * hour4) + (grade5 * hour5) + (grade6 * hour6) + (grade7 * hour7);
  const gpa = (totalPoints / totalHours).toFixed(2);


  const resultDiv = document.getElementById("result");
  resultDiv.textContent = `Your GPA is: ${gpa}`;
});

          

const calculateAvgButton = document.getElementById("calculate-avg-btn");
const avgResultDiv = document.getElementById("avg-result");

calculateAvgButton.addEventListener("click", function(event) {
  event.preventDefault();

  const num1 = Number(document.getElementById("num1").value);
  const num2 = Number(document.getElementById("num2").value);

  const average = (num1 + num2 ) / 2;

  avgResultDiv.textContent = `Your total GPA is: ${average.toFixed(2)}`;
});
