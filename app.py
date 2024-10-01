from flask import Flask, render_template, request
import time
app = Flask(__name__)
sample_text = """The quick brown fox jumps over the lazy dog. A typing speed test is a good way to measure your accuracy and speed."""

@app.route('/')
def index():
    return render_template('index.html', sample_text=sample_text)

@app.route('/result', methods=['POST'])
def result():
    user_input = request.form['user_input']
    start_time = float(request.form['start_time']) / 1000  # Convert milliseconds to seconds
    end_time = time.time()
    total_time = end_time - start_time
    total_words = len(user_input.split())
    wpm = total_words / (total_time / 60)
    correct_chars = sum(1 for i, j in zip(user_input, sample_text) if i == j)
    accuracy = (correct_chars / len(sample_text)) * 100
    return render_template('result.html', total_time=total_time, wpm=wpm, accuracy=accuracy, sample_text=sample_text, user_input=user_input)

if __name__ == '__main__':
    app.run(debug=True)
