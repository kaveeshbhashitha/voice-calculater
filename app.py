from flask import Flask, render_template, request, jsonify
import math 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/process-command', methods=['POST'])
def process_command():
    data = request.get_json()
    command = data.get('command', '').lower() 
    
    try:
        if 'add' in command:
            # Add numbers in the command
            numbers = [float(s) for s in command.split() if s.replace('.', '').isdigit()]
            result = sum(numbers)
        
        elif 'subtract' in command:
            # Subtract numbers in the command
            numbers = [float(s) for s in command.split() if s.replace('.', '').isdigit()]
            result = numbers[0] - sum(numbers[1:])
        
        elif 'multiply' in command or 'times' in command:
            # Multiply numbers in the command
            numbers = [float(s) for s in command.split() if s.replace('.', '').isdigit()]
            result = math.prod(numbers)
        
        elif 'divide' in command:
            # Divide two numbers
            numbers = [float(s) for s in command.split() if s.replace('.', '').isdigit()]
            if len(numbers) == 2 and numbers[1] != 0:
                result = numbers[0] / numbers[1]
            else:
                return jsonify({'result': 'Error: Cannot divide by zero or invalid input.'})
        
        elif 'mod' in command or 'remainder' in command:
            # Modulo operation
            numbers = [int(s) for s in command.split() if s.isdigit()]
            if len(numbers) == 2:
                result = numbers[0] % numbers[1]
            else:
                return jsonify({'result': 'Error: Please provide exactly two numbers for modulo.'})
        
        elif 'power' in command or 'raise' in command:
            # Power operation 
            numbers = [float(s) for s in command.split() if s.replace('.', '').isdigit()]
            if len(numbers) == 2:
                result = math.pow(numbers[0], numbers[1])
            else:
                return jsonify({'result': 'Error: Please provide a base and an exponent.'})
        
        elif 'square root' in command:
            # Square root operation
            numbers = [float(s) for s in command.split() if s.replace('.', '').isdigit()]
            if len(numbers) == 1 and numbers[0] >= 0:
                result = math.sqrt(numbers[0])
            else:
                return jsonify({'result': 'Error: Square root requires one non-negative number.'})
        
        else:
            # Command not recognized
            return jsonify({'result': 'Command not recognized. Try add, subtract, multiply, divide, mod, power, or square root.'})
    
    except Exception as e:
        return jsonify({'result': f'Error: {e}'})
    
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
