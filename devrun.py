"""
FLask development server
"""
from application import APPLICATION

APPLICATION.run(host='0.0.0.0', port=8080, debug=True, threaded=True)
