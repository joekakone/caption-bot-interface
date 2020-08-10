# coding : utf-8


'''Caption Bot : API for Caption Model'''


import os
import json
import requests
from PIL import Image
import gradio as gr


URL = 'http://192.168.43.141/api/caption'
FILE_PATH = 'temp.png'


def request(image):
	image = Image.fromarray(image)
	# save file 
	image.save(FILE_PATH)
	files = {
		'file': open(FILE_PATH, 'rb')
		}
	try:
		# send req to sever
		r = requests.post(URL, files=files)
		pred = json.loads(r.content.decode('utf-8'))
		output = 'Two boys are playing in the grass.'
	except Exception as e: # something turns wrong !
		print('Error', e)
		output = 'Sorry, something turns wrong ! Please try later.'

	# remove file
	os.remove(FILE_PATH)

	return output


# launch
gr.Interface(
	fn=request,
	inputs=gr.inputs.Image(label='Image to annote'),
	outputs=gr.outputs.Textbox(label='Annotation'),
	title="Caption Bot*",
	description="Upload an image - AI will describe the content of the image you uploaded - We can understand every image.",
	server_name='0.0.0.0'
	).launch()
