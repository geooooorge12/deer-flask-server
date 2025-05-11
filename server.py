from flask import Flask, jsonify, request
import os
import json
import datetime

app = Flask(__name__)

# 저장 디렉토리
JSON_DIR = "json_files"
os.makedirs(JSON_DIR, exist_ok=True)

@app.route('/')
def home():
    try:
        files = [f for f in os.listdir(JSON_DIR) if f.endswith('.json')]
        return jsonify({"message": "JSON 목록입니다.", "files": files})
    except FileNotFoundError:
        return jsonify({"error": f"{JSON_DIR} 폴더가 없습니다."}), 404

@app.route('/files', methods=['GET'])
def list_files():
    try:
        files = [f for f in os.listdir(JSON_DIR) if f.endswith('.json')]
        return jsonify(files)
    except FileNotFoundError:
        return jsonify({"error": "Directory not found"}), 404

@app.route('/files/<filename>', methods=['GET'])
def get_file(filename):
    filepath = os.path.join(JSON_DIR, filename)
    if not os.path.isfile(filepath):
        return jsonify({"error": "File not found"}), 404

    with open(filepath, "r") as f:
        data = json.load(f)
    return jsonify(data)

@app.route('/upload', methods=['POST'])
def upload_json():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No JSON received"}), 400

    timestamp = data.get("timestamp", datetime.datetime.now().strftime("%Y%m%d_%H%M%S_%f"))
    filename = f"detection_{timestamp}.json"
    filepath = os.path.join(JSON_DIR, filename)

    try:
        with open(filepath, "w") as f:
            json.dump(data, f, indent=2)
        return jsonify({"status": "success", "file": filename}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
