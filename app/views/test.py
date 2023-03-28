from views import bp

@bp.route('/testing')
def testing_endpoint():
    return "I think our test was successful :)"

@bp.route("/")
def index():
    return "Hello, World!"