

from calc_app.history import History
from .history_storage import HistoryStorage


class HistoryFileStorage(HistoryStorage):
    """ history file storage """

    def load(self, history: History) -> None:
        history.clear_entries()
        try:
            with open("history.txt", "r", encoding="UTF-8") as history_file:
                for history_line in history_file:
                    entry_parts = history_line.rstrip().rsplit("|")
                    history.append_entry(entry_parts[0], float(entry_parts[1]))
        except IOError:
            print("Unable to load file, cleared history.")

    def save(self, history: History) -> None:
        with open("history.txt", "w", encoding="UTF-8") as history_file:
            for entry in history:
                history_file.write(
                    f"{entry.command}"\
                    f"|{entry.operand}\n")
