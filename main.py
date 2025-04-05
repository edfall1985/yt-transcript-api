from flask import Flask, request, jsonify
from youtube_transcript_api import YouTubeTranscriptApi

app = Flask(__name__)

@app.route("/", methods=["POST"])
def get_transcript():
    data = request.get_json()
    video_id = data.get("video_id")

    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        # Gabungkan semua teks menjadi satu
        full_text = " ".join([entry['text'] for entry in transcript])
        return jsonify({"transcript": full_text})

    except Exception as e:
        return jsonify({"error": str(e)}), 400

app.run(host="0.0.0.0", port=81)

