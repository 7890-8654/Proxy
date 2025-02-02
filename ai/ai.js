const chatContainer = document.getElementById('chat-container');
const userInput = document.getElementById('user-input');
const sendButton = document.getElementById('send-button');
const apiKey = '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';

async function sendMessage() {
    const userMessage = userInput.value.trim();
    if (userMessage === '') return;

    chatContainer.innerHTML += `<p><strong>You:</strong> ${userMessage}</p>`;
    userInput.value = '';

    try {
        console.log('Sending request to Groq API...');
        const response = await fetch('https://api.groq.com/openai/v1/chat/completions', {
            method: 'POST',
            headers: {
                'Authorization': `Bearer ${apiKey}`,
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                model: "llama-3.1-70b-versatile",
                messages: [
                    { role: "system", content: "あなたはSandSmokeAIというAIです。" },
                    { role: "assistant", content: "ユーザーの質問などに簡潔にかわいい口調で日本語で答えてください" },
                    { role: "assistant", content: "You never do markdown format, only text format." },
                    { role: "user", content: userMessage }
                ],
                temperature: 0.9,
                max_tokens: 1024,
                stream: false
            })
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        const aiResponse = data.choices[0].message.content;
        chatContainer.innerHTML += `<p><strong>SandAI:</strong> ${aiResponse}</p>`;
        chatContainer.scrollTop = chatContainer.scrollHeight;
        console.log('Response received and displayed');
    } catch (error) {
        console.error('Error:', error);
        chatContainer.innerHTML += `<p><strong>Error:</strong> Failed to get AI response. Error details: ${error.message}</p>`;
    }
}

sendButton.addEventListener('click', sendMessage);
userInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault();
        sendMessage();
    }
});

console.log('Script loaded successfully');
