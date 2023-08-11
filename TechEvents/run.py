from application import create_app
import ssl

app = create_app(config='config')

ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ssl_context.load_cert_chain('/Users/kaushik/cert.pem', '/Users/kaushik/key.pem')

app.run(host='0.0.0.0', port=8000,ssl_context=ssl_context) 