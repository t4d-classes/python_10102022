from contextlib import contextmanager

@contextmanager
def safe_open(*args, **kwargs):

  try:
    file_handle = open(*args, **kwargs)
  except IOError as exc:
    yield None, exc # an error opening the file
  else:
    try:
      print("yield to caller to read file")
      yield file_handle, None # success
      print("resume caller done reading file")
    finally:
      if file_handle:
        print("close file handle")
        file_handle.close()


with safe_open("files/colors.txt", "r") as (colors_file, exc):
  if exc:
    print(exc)
  else:
    for color in colors_file:
        print(color.rstrip())

