import hashlib

image = '1319447.jpeg'

with open(image, 'rb') as f:
    file_data = f.read()
    image_hash = hashlib.sha3_256(file_data).hexdigest()
    print('Hash code of image is: ', image_hash)
