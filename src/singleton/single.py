# Single.py

class Single:
    class __single__:
        def __init__(self, arg):
            self.val = arg
    instance = None
    def __init__(self, arg):
        if not Single.instance:
            Single.instance = Single.__single__(arg)
        else:
            Single.instance.val = arg
    def getValue(self):
        return Single.instance.val
