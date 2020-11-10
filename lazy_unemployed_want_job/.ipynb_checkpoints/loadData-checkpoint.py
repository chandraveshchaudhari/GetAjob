#######################################
# load Data


import yaml


def get_data():
    with open("config.yaml", 'r') as stream:
        try:
            parameters = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            raise exc

    # assert len(parameters['positions']) > 0
    # assert len(parameters['locations']) > 0
    assert parameters['LinkedIn']['username'] is not None
    return parameters

'''
output_filename = [f for f in parameters.get('output_filename', ['output.csv']) if f != None]
output_filename = output_filename[0] if len(output_filename) > 0 else 'output.csv'
blacklist = parameters.get('blacklist', [])
uploads = parameters.get('uploads', {})
for key in uploads.keys():
    assert uploads[key] != None
'''
##################################