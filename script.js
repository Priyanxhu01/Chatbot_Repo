// Select the necessary DOM elements
const chatBox = document.getElementById('chat-box');
const userInput = document.getElementById('user-input');
const sendBtn = document.getElementById('send-btn');

// Function to append messages to the chat-box
function appendMessage(sender, message) {
    const messageContainer = document.createElement('div');
    messageContainer.classList.add('message', sender);

    const messageText = document.createElement('p');
    messageText.textContent = message;

    messageContainer.appendChild(messageText);
    chatBox.appendChild(messageContainer);

    // Scroll to the bottom of the chat-box to see the latest message
    chatBox.scrollTop = chatBox.scrollHeight;
}

// Function to handle sending a message
function sendMessage() {
    const userMessage = userInput.value.trim();

    if (userMessage === '') return;  // If input is empty, do nothing

    // Append user's message to the chat-box
    appendMessage('user', userMessage);

    // Clear the input field
    userInput.value = '';

    // Simulate bot response after a delay
    setTimeout(() => {
        const botResponses = getBotResponses(userMessage);
        
        // Loop through each response and append to the chat box with a delay between each response
        botResponses.forEach((response, index) => {
            setTimeout(() => {
                appendMessage('bot', response);
            }, 1000 * (index + 1));  // Delays each reply by an additional second
        });
    }, 500);
}

// Function to generate bot responses (4 responses each time)
function getBotResponses(userMessage) {
    const responses = [
        "I'm here to assist you!",
        "You can ask me anything.",
        "Is there anything else you need help with?",
        "Let me know how I can assist you."
    ];

    // The bot will return the predefined 4 responses regardless of user input
    return responses;
}

// Add an event listener to the Send button
sendBtn.addEventListener('click', sendMessage);

// Optionally, send message when Enter key is pressed
userInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        sendMessage();
    }
});
