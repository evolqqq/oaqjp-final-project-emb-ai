from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    scores = response
    detected = response['dominant_emotion']

    scores_str = ", ".join(f"{emotion}: {score:.2f}" for emotion, score in scores.items() if emotion != 'dominant_emotion')
    
    return f"The given text was analyzed and has detected emotions of {scores_str} with the dominant emotion being {detected}."

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)