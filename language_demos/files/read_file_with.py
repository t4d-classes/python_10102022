
try:

  with open("files/colors.txt", "r") as colors_file:

    for color in colors_file:
        print(color.rstrip())

except IOError as exc:
  print(exc)

