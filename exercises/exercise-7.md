# Exercise 7

1. Implement two new commands into Calc App: `load` and `save`

2. The `load` command loads a file named `history.txt` into the history object. If the file does not exist, do not throw an error, just set the history entry list to blank.

3. The `save` command saves the list of history entries to a file named `history.txt`. The save command should replace any existing history file.

4. Use the `with open` syntax for loading and saving the file. Do not use `safe_open`.

5. For writing content to a file, review the code below:

```python
colors = ["red", "green", "blue"]

with open("newcolors.txt", "w") as colors_file:
    for color in colors:
        colors_file.write(f"{color}\n")
```

6. Think about code organization as you implement the solution.

7. Ensure it works!