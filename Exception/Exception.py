
from mypack.voting import Voter


def myfun():
    try:
        v=Voter("dewang",17)
    except Exception as e:
        print(e)
    print("Done")
myfun()
