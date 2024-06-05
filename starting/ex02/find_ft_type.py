
def all_thing_is_obj(object: any) -> int:
    print(f"{(type(object).__name__).capitalize()} : {type(object)}")
    return 42