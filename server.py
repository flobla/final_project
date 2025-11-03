""" Server, running on port 5000, Serving index.html, Calling sentiment_analyzer """
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    """Call sentiment_analyzer and display result.""" 
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    scores_list = [f"'{key}': {value}" for key, value in response.items()]
    scores_string = ", ".join(scores_list)
    return "For the given statement, the system response is "+scores_string+"."

@app.route("/")
def render_index_page():
    """Serve index.html"""
    return render_template('index.html')

# Main, start app on port 5000
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
