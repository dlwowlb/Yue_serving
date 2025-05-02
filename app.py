# app.py
from flask import Flask, request, jsonify, send_file
import subprocess, os, json

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health():
    return "ok", 200

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # 1) 클라이언트가 보낸 파일 객체 가져오기
        genre_file = request.files['genre_txt']
        lyrics_file = request.files['lyrics_txt']

        # 2) 컨테이너 내에 저장할 임시 경로
        genre_path  = '/tmp/genre.txt'
        lyrics_path = '/tmp/lyrics.txt'

        # 3) 파일 저장
        genre_file.save(genre_path)
        lyrics_file.save(lyrics_path)

        # 4) infer.py 실행
        #    
        cmd = [
            'python','-u', 'infer.py',
            '--genre_txt', genre_path,
            '--lyrics_txt', lyrics_path,
            '--output_dir', '/tmp/output'
        ]
        subprocess.run(cmd, check=True)

        # 5) infer.py가 쓴 결과 JSON 불러오기
        '''
        result_path = '/tmp/output/result.json' 
        with open(result_path, 'r') as f:
            result = json.load(f)

        return jsonify(result), 200
        '''

        audio_path = '/tmp/output/result.mp3'
        return send_file(audio_path,
                         mimetype='audio/mpeg',
                         as_attachment=True,
                         download_name='result.mp3')

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    port = int(os.environ.get("AIP_HTTP_PORT", 8080))
    app.run(host="0.0.0.0", port=port)




'''# app.py
from flask import Flask, request, jsonify
import subprocess, json, os

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health():
    return "ok", 200

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json() or {}
    try:
        # 요청 데이터를 임시 파일에 저장
        with open('input.json', 'w') as f:
            json.dump(data, f)
        # infer.py 실행
        subprocess.run([
            'python', 'infer.py',
            '--input', 'input.json',
            '--output', 'output.json'
        ], check=True)
        # 출력 결과 로드
        with open('output.json', 'r') as f:
            result = json.load(f)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    port = int(os.environ.get("AIP_HTTP_PORT", 8080))
    app.run(host="0.0.0.0", port=port)
'''