import datetime
import os
import six

from flask import current_app
from google.cloud import storage

credential_path = "/Users/kaushik/Documents/techevents-395404-0d385013fdc6.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

def upload_image_file(file, folder, content_id):
    if not file:
        return None
    file.format = 'png'
    date = datetime.datetime.utcnow().strftime('%Y-%m-%d-%H%M%S')
    filename = '{}-{}.{}'.format(content_id, date, 'png')
    
    client = storage.Client(project=current_app.config['PROJECT_ID'])
    bucket = client.bucket(current_app.config['CLOUD_STORAGE_BUCKET'])
    blob = bucket.blob(os.path.join(folder, filename))
    
    blob.upload_from_string(file.read(),
                           content_type=file.content_type)
    url = blob.public_url

    # url2 = 'https://storage.cloud.google.com/{}/{}'.format(bucket.name, blob.name)

    
    # print(blob.public_url + "vs" + url2)
    if isinstance(url, six.binary_type):
        url = url.decode('utf-8')
    return url
        