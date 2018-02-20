from DiPaolo import app

@app.route('/')
def home():
    return 'its work!'

