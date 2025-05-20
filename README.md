# Yue_Music_serving

- [x] Hugging face serving
- [x] Docker push 할 때 sudo 없애기
- [ ] Vertex에는 /health 꼭 넣어야 함

# 도커 빌드 및 푸시
docker build -t docker.io/
docker push docker.io/

# Curl 요청(HF)
curl -X POST "https:// /predict"   -H "Authorization: Bearer hf_"   -F "genre_txt=@genre.txt"   -F "lyrics_txt=@lyrics.txt" -o result.mp3

(로컬) curl -X POST http://localhost:8080/predict -F "genre_txt=@genre.txt" -F "lyrics_txt=@lyrics.txt" -o result.mp3

