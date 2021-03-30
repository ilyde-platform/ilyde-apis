#!/usr/bin/env python
from apis_server import app


def main():
    app.run(port=8080, debug=False)


if __name__ == '__main__':
    main()
