from flask import Flask, jsonify, send_from_directory

app = Flask(__name__)

@app.route('/video/<name_video>')
def get_video(name_video):
    return send_from_directory('src\\videos', name_video)

@app.route('/image/<name_image>')
def get_image(name_image):
    return send_from_directory('src\\images', name_image)

@app.route('/audio/<name_audio>')
def get_audio(name_audio):
    return send_from_directory('src\\audios', name_audio)








if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)