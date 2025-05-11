from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return '서버가 정상적으로 작동 중입니다.'

@app.route('/files')
def list_files():
    directory = 'json_files'  # 실제 JSON 파일이 있는 디렉터리 이름에 맞게 수정
    try:
        files = [f for f in os.listdir(directory) if f.endswith('.json')]
        return jsonify(files)
    except FileNotFoundError:
        return jsonify({"error": "Directory not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
