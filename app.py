from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)
app.static_folder = 'static'

def generate_password(length=8, include_lowercase=False, include_symbols=False, include_numbers=False, include_uppercase=False):
    characters = ""
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_symbols:
        characters += string.punctuation
    if include_numbers:
        characters += string.digits
    if include_uppercase:
        characters += string.ascii_uppercase
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    length = int(request.form['length'])
    include_lowercase = 'include_lowercase' in request.form
    include_symbols = 'include_symbols' in request.form
    include_numbers = 'include_numbers' in request.form
    include_uppercase = 'include_uppercase' in request.form
    password = generate_password(length, include_lowercase, include_symbols, include_numbers, include_uppercase)
    return render_template('index.html', password=password)

if __name__ == '__main__':
    app.run( debug=True)
