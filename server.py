from flask import Flask, jsonify
import os
import json

app = Flask(__name__)

@app.route('/')
def home():
    directory = 'json_files'
    try:
        files = [f for f in os.listdir(directory) if f.endswith('.json')]
        return jsonify({"message": "JSON 목록입니다.", "files": files})
    except FileNotFoundError:
        return jsonify({"error": "json_files 폴더가 없습니다."}), 404

@app.route('/files')
def list_files():
    directory = 'json_files'
    try:
        files = [f for f in os.listdir(directory) if f.endswith('.json')]
        return jsonify(files)
    except FileNotFoundError:
        return jsonify({"error": "Directory not found"}), 404
