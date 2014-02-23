class pypline:
    def __init__(self, iter):
        self.iter = iter
        self.args = []
        self.kwargs = {}

    def __ror__(self, other):
        return self.iter(other, *self.args, **self.kwargs)

    def __or__(self, other):
        return self.iter(other, *self.args, **self.kwargs)

    def __call__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        return self

class pypline_conversion:
    def __init__(self, func):
        self.func = func
        self.args = []
        self.kwargs = {}

    def __or__(self, other):
        return (x for x in other if self.func(x, *self.args, **self.kwargs))

    def __ror__(self, other):
        return (x for x in other if self.func(x, *self.args, **self.kwargs))

    def __call__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        return self


#region utilities

sort = pypline(sorted)
reverse = pypline(reversed)

@pypline
def display(iter, file=None):
    for item in iter:
        print(item, file=file)

#endregion
