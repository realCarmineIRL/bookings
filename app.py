import os
from project import create_app

ENVIRONMENT = os.environ.get('ENVIRONMENT')

app = create_app(ENVIRONMENT)

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, host="0.0.0.0", port=5000)