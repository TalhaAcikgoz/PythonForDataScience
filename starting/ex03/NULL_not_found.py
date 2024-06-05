def NULL_not_found(object: any) -> int:
    dick = {
        type(None) : "Nothing",
        type(float("NaN")) : "Cheese",
        type(0) : "Zero",
        "" : "Empty",
        type(False) : "Fake",
        str : "Type not Found"
        }
    if (object == ""):
        print(f"Empty: {type(object)}")
        return 1
    if dick[type(object)] is not None:
        if dick[type(object)] == "Type not Found":
            print(dick[type(object)])
            return 1
        print(f"{dick[type(object)]}: {type(object)}")
        return 1
    return 0
