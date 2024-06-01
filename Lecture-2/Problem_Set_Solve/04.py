x = input("File name: ")

if x.strip().lower().endswith(".gif"):
    print("image/gif")

elif x.strip().lower().endswith(".jpg"):
    print("image/jpeg")

elif x.strip().lower().endswith(".jpeg"):
    print("image/jpeg")

elif x.strip().lower().endswith(".png"):
    print("image/png")

elif x.strip().lower().endswith(".pdf"):
    print("application/pdf")

elif x.strip().lower().endswith(".txt"):
    print("text/plain")

elif x.strip().lower().endswith(".zip"):
    print("application/zip")

else:
    print("application/octet-stream")

