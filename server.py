'''
    This is the server module for the Emotion Analysis Web App
'''

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def emotion_analyzer():
    '''
        Flask app route for Emotion Detection
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    emotions = emotion_detector(text_to_analyze)

    dominant = emotions.get("dominant_emotion")

    if dominant is None:
        return "Invalid Text! Please try again!"

    items = [f"'{k}': {v}" for k, v in emotions.items() if k != "dominant_emotion"]
    response = ", ".join(items[:-1]) + " and " + items[-1]

    return f"For the given statement, the system response is {response}.\
         The dominant emotion is {dominant}"


@app.route("/")
def render_index_page():
    '''
        Flask app route for main page
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
