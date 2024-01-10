from flask import Flask, jsonify

app = Flask(__name__)

# In-memory video data (you can replace this with a database)
videos = [
    {
        'id': 1,
        'title': 'Seasonal confectionery - Assorted cherry confectionery',
        'author': '李子柒 Liziqi',
        'time': '05:38',
        'format': 'youtube',
        'link': 'https://www.youtube.com/watch?v=2GNI02rlF_M',
    },
    {
        'id': 2,
        'title': 'Azerbaijan. Take another look. Culture',
        'author': 'Dars Films',
        'time': '00:30',
        'format': 'youtube',
        'link': 'https://www.youtube.com/watch?v=vj6pAesIZBE',
    },
]

# Define a route to get all videos
@app.route('/videos', methods=['GET'])
def get_videos():
    return jsonify({'videos': videos})

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
