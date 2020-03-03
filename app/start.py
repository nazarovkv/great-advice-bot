import http.server as server


def start_server():
    PORT = 8000
    Handler = server.CGIHTTPRequestHandler
    httpd = server.HTTPServer(("", PORT), Handler)
    print("Serving at port", PORT)
    httpd.serve_forever()


if __name__ == '__main__':
    start_server()
