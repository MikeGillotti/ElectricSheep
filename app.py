import glob
import pathlib
import os
import openai
import time
import math
import random
import tkinter.font as font
from tkinter import simpledialog
from tkinter import *
from PIL import ImageTk, Image
from io import BytesIO
from urllib.request import urlopen

root = Tk()
root.title("Electric Sheep")
display_image = Label()
text_label = Label()
#openai.organization = simpledialog.askstring(title="OpenAI ORG ID", prompt="Please enter organization ID")
OPENAI_API_KEY = simpledialog.askstring(title="Authorization", prompt="Please enter API Key")
openai.api_key = OPENAI_API_KEY
openai.Model.list()
root.geometry("500x500")


def generate_image():
	global display_image
	global prompt_text
	global displayed_image
	global generated_image
	global text_label

	display_image.grid_forget()
	text_label.grid_forget()

	response = openai.Image.create(
		prompt=prompt_text.get(),
		n=1,
		size="256x256",
		response_format="url"

	)
	
	image_url = response['data'][0]['url']
	url = urlopen(image_url)
	raw_data = url.read()
	url.close()
	generated_image = Image.open(BytesIO(raw_data))
	displayed_image = ImageTk.PhotoImage(generated_image)
	display_image = Label(root, image=displayed_image)
	display_image.grid(row=2, column=0, columnspan=2)
	text_label = Label(root, text=prompt_text.get())
	text_label.grid(row=1, column=0, columnspan=2)


prompt_text = Entry(root)
prompt_text.grid(row=0, column=0)

prompt_button = Button(root, text="Dream", command=generate_image)
prompt_button.grid(row=0, column=1)


root.mainloop()
