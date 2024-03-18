<?php
// Check if the form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Retrieve form data
    $name = $_POST["name"];
    $email = $_POST["email"];
    $bio = $_POST["bio"];
    
    // Display submitted data (you can save it to a database or send it via email instead)
    echo "<h2>Submitted Profile</h2>";
    echo "Name: " . $name . "<br>";
    echo "Email: " . $email . "<br>";
    echo "Bio: " . $bio . "<br>";
}
?>
