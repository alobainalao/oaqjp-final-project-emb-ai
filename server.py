''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection import emotion_detection as emt

# Instantiate Flask application
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the function and store the response
    emotions = emt.emotion_detector(text_to_analyze)

    dominant_emotion = emotions["dominant_emotion"]
    last_emotion = emotions["sadness"]

    # Check if the label is None, indicating an error or invalid input
    if last_emotion is None:
        return "Invalid text! Try again."
    else:
        emotion_values = ", ".join(f"'{key}': {value}" for key, value in emotions.items() if key not in ['sadness', 'dominant_emotion'])
        # Return a formatted string
        return "For the given statement, the system response is {} and 'sadness':{}. The dominant emotion is {}.".format(emotion_values, last_emotion, dominant_emotion)

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
