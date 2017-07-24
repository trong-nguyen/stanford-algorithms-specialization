'''
API: 
upload: python THIS_SCRIPT.PY PATH_TO_UPLOAD_IMAGE.EXT
delete: python THIS_SCRIPT.PY deletehash:HASH_RETURNED_FROM_UPLOAD_OPERATION
'''

import sys, os
from imgurpython import ImgurClient

client_id = 'ed62bfd5d976723'
client_secret = '24cec99a0c126ed4a03b6b87202eba6a12d380f0'

client = ImgurClient(client_id, client_secret)

# Authorization flow, pin example (see docs for other auth types)
# authorization_url = client.get_auth_url('pin')
# ... redirect user to `authorization_url`, obtain pin (or code or token) ...

# use this to get the tokens
# paste into an already logged-in browser environment
authorization_url = 'https://api.imgur.com/oauth2/authorize?client_id={}&response_type=token'.format(client_id)
# https://api.imgur.com/oauth2/authorize?client_id=ed62bfd5d976723&response_type=token
# https://imgur.com/#access_token=65167e1a63044a79ba36c654072d06ef7210de3d&expires_in=2419200&token_type=bearer&refresh_token=ae9b6c0e8c53e598dabc622276ea6e6b98773d2d&account_username=Trong2Nguyen&account_id=39273572
if __name__ == '__main__':
	# credentials = client.authorize('41298c9258', 'pin')
	# ed39d04da58826c2c91a45f66ad813eeed67d6eb
	# credentials = client.authorize('PIN OBTAINED', 'token')
	credentials = {
		'access_token': '65167e1a63044a79ba36c654072d06ef7210de3d',
		'refresh_token': 'ae9b6c0e8c53e598dabc622276ea6e6b98773d2d'
	}
	client.set_user_auth(credentials['access_token'], credentials['refresh_token'])


	file = sys.argv[1]
	filename = os.path.basename(file)
	name = os.path.splitext(filename)[0]

	if 'deletehash' in name:
		image_hash = name.split(':')[1]
		result = client.delete_image(image_hash)
		print 'Deleting {}'.format(image_hash)
	else:
		response = client.upload_from_path(file, config={'name':name}, anon=False)
		print '![Imgur]({})'.format(response['link'])
		print 'deletehash:{}'.format(response['deletehash'])

		