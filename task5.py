from flask import Flask, jsonify

app = Flask(__name__)


videos = [
    {
        'id': 1,
        'title': 'video11',
        'author': '--',
        'time': '--',
        'format': 'mp4',
        'link': 'https://github.com/nn/repo/raw/main/video11.mp4',
    },
    {
        'id': 2,
        'title': 'Video22',
        'author': '..',
        'time': '--',
        'format': 'mkv',
        'link': 'https://github.com/mme/repo/raw/main/video22.mkv',
    },
]

# Define a route to get all videos
@app.route('/videos', methods=['GET'])
def get_videos():
    return jsonify({'videos': videos})

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
