document.getElementById('urlForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    const originalUrl = document.getElementById('originalUrl').value;
    const resultDiv = document.getElementById('result');

    try {
        const response = await fetch('/shorten', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ url: originalUrl }),
        });

        if (!response.ok) {
            throw new Error('Failed to shorten URL');
        }

        const data = await response.json();
        resultDiv.innerHTML = `
            <p>Your shortened URL: <a id="shortUrl" href="${data.short_url}" target="_blank">${data.short_url}</a></p>
            <button onclick="copyToClipboard('${data.short_url}')">Copy</button>
        `;
    } catch (error) {
        resultDiv.innerHTML = `<p>Error: ${error.message}</p>`;
    }
});

function copyToClipboard(text) {
    navigator.clipboard.writeText(text).then(() => {
        alert('Copied to clipboard!');
    });
}