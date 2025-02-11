import base64



with open("bread_white.jpg", "rb") as file:
    data = file.read()
    # data = file
    # print(data)



# string = "Welcome to Sling Academy!"
# # Кодирование с помощью base64.b64encode() функции
# encoded_string = base64.b64encode(data.encode("utf-8")).decode("utf-8")
# print(encoded_string)

# отпра
import base64
encoded_string = base64.b64encode(data)
print(encoded_string)

# приём
decoded_string = base64.b64decode(encoded_string)
print(decoded_string)

# with open("bread_white1.jpg", "wb") as file:
#     file.write(decoded_string)





