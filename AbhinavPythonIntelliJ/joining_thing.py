####join method###
menu=[["egg","bacon"],
  ["egg","sausage","bacon"],
  ["egg","spam"],
  ["egg","bacon","spam"],
  ["egg","bacon","sausage","spam"],
  ["spam","sausage","spam","bacon"],
  ["spam","egg","spam","bacon","spam"]
]

# for meal in menu:
#     for index in range(len(meal)-1,-1,-1):
#         if meal[index]=="spam":
#             del meal[index]
#     print(meal)

flowers=["daffodil","evening primrose","hydrangea","iris","lavender","sunflower","tiger lily"]
seperator=" | "
print(seperator.join(flowers))
print(", ".join(flowers))
