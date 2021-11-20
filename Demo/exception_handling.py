d = {"key": "value", "key1": 1, "key2": 2}
l = [1, 2, 3]

try:
    bad_val = d['badkey']
except:
    print("an exception has been thrown")

try:
    bad_val = d['badkey']
except KeyError:
    print("A key error was thrown")

try:
    bad_val = d['badkey']
except KeyError as ke:
    print("Error was caused by: " + str(ke))

try:
    val = l[3]
except KeyError:
    print("A Key Error Occurred")
except Exception as e:
    print("An unknown error occured: " + str(e))
