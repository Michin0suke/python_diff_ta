import base64

input_file = open('input.txt', 'r')
output_file = open('output.txt', 'w')

text_arr = input_file.readlines()
text = ''.join(text_arr)
encoded = base64.b64encode(text.encode())
output_file.write(str(encoded))