

def str_list(l):
    return f"[{', '.join([str(e) for e in l])}]"

def str_dict(d):
    def format_value(value):
        if isinstance(value, list):
            return f"[{', '.join(map(str, value))}]"
        return str(value)

    return f"{{{' ,'.join([f'{str(k)} : {format_value(v)}' for k, v in d.items()])}}}"

