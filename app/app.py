from flask import Flask, jsonify
app = Flask(__name__)

@app.get('/')
def home():
    return 'Flask is running (AI_MODEL_TESTING)! testing 1'

@app.get('/health')
def health():
    return jsonify({'status': 'ok'})
