from flask import Flask

app = Flask(__name__)

# URLとメソッドの指定
@app.route("/", methods=["GET"])
def get_articles():
    title = "Qiita Title"
    url = "https://qiita.com/"

    # JSON形式でレスポンス
    return {
        "title": title,
        "url": url,
    }

if __name__ == '__main__':
    app.debug = True
    app.run()