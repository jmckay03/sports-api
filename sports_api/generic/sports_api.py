from . import generic_sports

@generic_sports.route("/url", methods=['GET'])
def hello():
  return 'hello world'