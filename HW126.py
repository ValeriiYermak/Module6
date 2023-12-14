import base64


def encode_data_to_base64(data):
    
    encoded_data = []
    for pair in data:

        encoded_pair = base64.b64encode(pair.encode("utf-8"))
        decoded_pair = encoded_pair.decode("utf-8")
        new_encoded_pair = f"{decoded_pair}"
        encoded_data.append(new_encoded_pair)
    return encoded_data



