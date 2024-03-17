document.addEventListener("DOMContentLoaded", function(event) {

    const lines = ["Hello,", "My name is Chris Duplessis", "I am an independent Web Design Artist  ", "Working as a freelance in Toronto!"];

    let currentIndex = 0;
    const delay = 2000; // Delay in milliseconds

    function typeText() {
        if (currentIndex < lines.length) {
            const lineElement = document.querySelector('.line');
            lineElement.textContent = ""; // Clear previous text
            const line = lines[currentIndex];
            let index = 0;
            const typingInterval = setInterval(function() {
                if (index < line.length) {
                    lineElement.textContent += line[index];
                    index++;
                } else {
                    clearInterval(typingInterval);
                    setTimeout(function() {
                        eraseText();
                    }, delay);
                }
            }, 100); // Typing speed in milliseconds
            currentIndex++;
        } else {
            currentIndex = 0; // Reset index to repeat lines
            setTimeout(typeText, delay); // Start typing again after delay
        }
    }

    function eraseText() {
        const lineElement = document.querySelector('.line');
        let text = lineElement.textContent;
        const eraseInterval = setInterval(function() {
            if (text.length > 0) {
                text = text.slice(0, -1);
                lineElement.textContent = text;
            } else {
                clearInterval(eraseInterval);
                typeText(); // Type the next line after erasing
            }
        }, 50); // Erasing speed in milliseconds
    }

    typeText(); // Start the typing effect
});

