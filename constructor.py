"""
Utility for math model construction and export to model-files by pickle
"""

import pickle
from servoclass import Servo


def main():
    print("Hello")
    command = ""
    while command != "E":
        print("[CS]=Create Servo model or \n[LS]=Load Servo model or")
        print("[CD]=Create demo or \n[LD]=Load demo or")
        command = input("[E]xit?")
        if command == "CD":
            export_model(3.1415956)
            print("done")
        elif command == "LD":
            obj = load_model()
            print(obj)
            print("done")
        elif command == "CS":
            servomotor = Servo()
            servomotor.set_limits(0, 180)
            servomotor.set_angle(90)
            export_model(servomotor)
            print("done")
        elif command == "LS":
            servomotor = load_model()
            print(str(servomotor.get_angle()))
            print("done")


def export_model(obj):
    with open("models/dog.pickle", "wb") as f:
        pickle.dump(obj, f)


def load_model():
    with open("models/dog.pickle", "rb") as f:
        obj = pickle.load(f)
    return obj


if __name__ == "__main__":
    main()
