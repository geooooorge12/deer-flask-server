from flask import Flask, request, jsonify
import os
import datetime

app = Flask(__name__)

# 📁 저장 폴더
os.makedirs("received_detections", exist_ok=True)

# 📨 감지 데이터 업로드 (POST)
@app.route('/upload', methods=['POST'])
def upload_detection():
    data = request.get_json()
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    filepath = f"received_detections/detection_{timestamp}.json"

    with open(filepath, 'w') as f:
        f.write(request.data.decode())

    print(f"✅ 감지 정보 저장됨 → {filepath}")
    return jsonify({"status": "success", "message": "data received"}), 200

# 📂 저장된 파일 목록 보기
@app.route('/files', methods=['GET'])
def list_files():
    files = os.listdir("received_detections")
    return jsonify(files)

# 📄 특정 JSON 파일 보기
@app.route('/files/<filename>', methods=['GET'])
def get_file(filename):
    filepath = os.path.join("received_detections", filename)
    if os.path.exists(filepath):
        with open(filepath, "r") as f:
            return f.read(), 200, {'Content-Type': 'application/json'}
    return jsonify({"error": "File not found"}), 404

# 🏁 앱 실행
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
