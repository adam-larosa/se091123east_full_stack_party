from config import app


@app.route( '/cats' )
def cats():
    return 'all the cats'
