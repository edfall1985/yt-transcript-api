from flask import Flask, request, jsonify
from youtube_transcript_api import YouTubeTranscriptApi
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Biar bisa diakses dari tool lain seperti Make/Reqbin

@app.route("/", methods=["GET"])
def home():
    return "YouTube Transcript API aktif!"

@app.route("/transcript", methods=["POST"])
def get_transcript():
    try:
        data = request.get_json()
        video_id = data.get("video_id")

        if not video_id:
            return jsonify({"error": "Video ID tidak ditemukan"}), 400

        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        full_text = " ".join([entry['text'] for entry in transcript])
        return jsonify({"transcript": full_text})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
