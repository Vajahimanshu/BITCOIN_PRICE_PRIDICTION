async function predictPrice() {
    const dateInput = document.getElementById('dateInput').value;
    const response = await fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ date: dateInput }),
    });
    const result = await response.json();
    document.getElementById('result').innerText = `Predicted Price: $${result.price.toFixed(2)}`;
}
