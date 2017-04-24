from pprint import pprint

def keys_as_vals(xs):
    return dict(zip(xs, xs))

mappings = {
    "cuisine": keys_as_vals(["italian", "british", "indian", "spanish", "french"]),
    "location": keys_as_vals(["paris", "bombay", "london", "madrid", "rome"]),
    "people": keys_as_vals(["two", "four", "six", "eight"]),
    "price": keys_as_vals(["cheap", "moderate", "expensive"])
}

def process_datum(datum):
    yield "A: ADD root cuisine"
    yield "A: ADD root location"
    yield "A: ADD root people"
    yield "A: ADD root price"        
    for line in datum.split("\n"):
        one, two = line.split("\t")
        agent = "A: MSG " + two
        user = "U: MSG " + one[one.index(" ") + 1:]
        yield user
        for (feature_name, word_maps) in mappings.items():
            for (words, feature_value) in word_maps.items():
                if user.find(words) != -1:
                    yield "A: ADD " + feature_name + " " + feature_value
        yield agent
        # It would be more natural if we didn't have to add the following.
        # But then, if the user is silent and we don't change the workspace,
        # the system's prediction won't change.
        if agent.find("look into some options") != -1:
            yield "A: ADD root ready"        

def process_data(data):
    for datum in data:
        yield "\n".join(process_datum(datum))

def main():
    f = open("../data/dialog-babi-task1/dialog-babi-task1-API-calls-dev.txt")
    data = f.read().strip().split("\n\n")
    output =  "\n\n".join(process_data(data))
    f = open("../data/dialog-babi-task1/dialog-babi-task1-API-calls-dev-workspace.txt", "w")
    f.write(output)
    f.close()

main()
