import pickle


class Storage:
    def __init__(self, filename):
        self._filename = f"{filename}.pkl"

    def save_to_disk(self, records_dict):
        try:
            with open(self._filename, "wb") as file:
                pickle.dump(records_dict, file)
        except Exception as e:
            pass

    def read_from_disk(self):
        try:
            with open(self._filename, "rb") as file:
                loaded_records = pickle.load(file)
            return loaded_records
        except FileNotFoundError:
            return {}
        except Exception as e:
            return {}
