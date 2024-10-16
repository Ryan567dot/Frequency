import colours

random_list = ["White","Blue","Black","Green"]

frequency = colors.Counter(random_list)

print(dict(frequency))
{"White": 3, "Blue": 3, "Black": 1, "Green": 2}
