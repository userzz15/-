
def add_h(func):
    def call_fun():
        start = "<h1>"
        text = func()
        end = "</h1>"
        return start + text + end
    return call_fun

@add_h
def get_str():
    return "hahaha"

if __name__ == "__main__":
    print(get_str())