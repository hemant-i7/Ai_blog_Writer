from flask import Flask, render_template, request
import openai
import os

# Set up OpenAI API credentials
openai.api_key = "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"


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('main.html')


@app.route('/limitations')
def limit():
    return render_template('limitations.html')


@app.route('/paraphrase', methods=['GET', 'POST'])
def paraphrase():
    if request.method == 'POST':
        original_text = request.form['original_text']
        # Use AI model to summarize text
        model_engine = "text-davinci-002"
        completions = openai.Completion.create(
            engine=model_engine,
            prompt=original_text,
            max_tokens=100,
        )

        # Get the response
        message = completions.choices[0].text.strip()

        paraphrase_text = message
        return render_template('paraphrase.html', paraphrase_text=paraphrase_text)
    else:
        return render_template('paraphrase.html')


@app.route('/summarize', methods=['GET', 'POST'])
def summarize():
    if request.method == 'POST':
        original_text = request.form['original_text']
        # Use AI model to summarize text
        model_engine = "text-davinci-002"
        completions = openai.Completion.create(
            engine=model_engine,
            prompt=original_text,
            max_tokens=100,
        )

        # Get the response
        message = completions.choices[0].text.strip()

        summarized_text = message
        return render_template('summarize.html', summarized_text=summarized_text)
    else:
        return render_template('summarize.html')


@app.route('/write_content', methods=['GET', 'POST'])
def write_content():
    if request.method == 'POST':
        topic = request.form['topic']
        # Use AI model to generate new content based on topic

        model_engine = "text-davinci-002"
        completions = openai.Completion.create(
            engine=model_engine,
            prompt=topic,
            max_tokens=100,
        )

        # Get the response
        message = completions.choices[0].text.strip()

        generated_content = message
        return render_template('write_content.html', generated_content=generated_content)
    else:
        return render_template('write_content.html')


if __name__ == '__main__':
    app.run(debug=True)
