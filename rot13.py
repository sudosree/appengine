import codecs
from escaping import escape_fun

def translate(text):
	new_text=codecs.encode(text,'rot_13')
	new=escape_fun(new_text)
	return new

#print translate('</textarea>')
