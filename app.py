from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Render the main HTML file

@app.route('/process-command', methods=['POST'])
def process_command():
    data = request.get_json()
    command = data.get('command', '').lower()
    
    # Example simple command processing
    try:
        if 'add' in command:
            numbers = [int(s) for s in command.split() if s.isdigit()]
            result = sum(numbers)
        elif 'subtract' in command:
            numbers = [int(s) for s in command.split() if s.isdigit()]
            result = numbers[0] - sum(numbers[1:])
        else:
            return jsonify({'result': 'Command not recognized'})
    except Exception as e:
        return jsonify({'result': f'Error: {e}'})

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
