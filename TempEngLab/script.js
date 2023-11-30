// Define a template using Mustache.js
var template = `
    <ul>
        {{#data}}
        <li>
            Subject: {{subject}}, Number: {{number}}, Title: {{title}}, Professor: {{professor}},
            Days: {{days}}, Time: {{time}}, Location: {{location}}, Room: {{room}}
        </li>
        <br> <!-- Add a line break after each list item -->
        {{/data}}
    </ul>
`;

// Get the 'output' div element
var output = document.getElementById("output");

// Fetch JSON data from the file
fetch("data.json")
  .then(function (response) {
    return response.json();
  })
  .then(function (data) {
    // Render the data using the template
    var rendered = Mustache.render(template, { data: data });
    output.innerHTML = rendered;
  })
  .catch(function (error) {
    console.error("Error:", error);
  });
