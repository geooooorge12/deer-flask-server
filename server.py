from flask import Flask, request, jsonify
import os
import datetime

app = Flask(__name__)

# 저장 폴더 생성
os.makedirs("received_detections", exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_detection():
    data = request.get_json()

    # 파일명은 타임스탬프로 자동 저장
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    filepath = f"received_detections/detection_{timestamp}.json"

    with open(filepath, 'w') as f:
        f.write(request.data.decode())

    print(f"✅ 감지 정보 저장됨 → {filepath}")
    return jsonify({"status": "success", "message": "data received"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
