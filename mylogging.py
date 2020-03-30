from datetime import datetime


def file_logged(file_path, qmark='"'):
    def logged(fun):
        def decorated(*args, **kwargs):
            call_t = datetime.now()
            fres = fun(*args, **kwargs)
            with open(file_path, "a", encoding="utf-8") as log_file:
                print(call_t,
                      _call_str(fun.__name__, args, kwargs, qmark),
                      "->", _quoted_val(fres, qmark),
                      file=log_file)
            return fres
        return decorated
    return logged


def _call_str(name, args, kwargs, qmark):
    params = [_quoted_val(arg, qmark) for arg in args]
    params.extend(
        "=".join([p_name, _quoted_val(p_val, qmark)])
        for p_name, p_val in kwargs.items()
    )
    return "{0}({1})".format(name, ", ".join(params))


def _quoted_val(param, qmark):
    if isinstance(param, str):
        return _quoted_str(param, qmark)
    else:
        return str(param)


def _quoted_str(s, qmark):
    return "".join([qmark, s.replace(qmark, "\\" + qmark), qmark])
