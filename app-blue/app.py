from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/blue-app')  # Add this route
def blue_app():
    return render_template('index.html')

@app.route('/validate', methods=['POST'])
def validate():
    data = request.json
    input_text = data.get("input_text", "")
    
    print(f"Received: {input_text}")  # Log to console

    transformed_text = input_text.upper()  # Convert to uppercase

    return jsonify({"transformed_text": transformed_text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

