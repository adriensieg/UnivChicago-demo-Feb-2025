async function validateInput() {
    let inputText = document.getElementById("inputBox").value;

    let response = await fetch("/validate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ input_text: inputText })
    });

    let data = await response.json();
    document.getElementById("outputBox").value = data.transformed_text;
}