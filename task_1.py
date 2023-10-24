import re


def input_error(func):
    def inner(*args, **kwargs):
        args = args[0]
        command = str(func).split()

        if command[1] in ('add_contact', 'change_contact'):
            try:
                if len(args) == 2:
                    try:
                        new_phone = re.sub(r"[0-9]", "", args[-1])
                        if len(new_phone) == 0:
                            try:
                                if len(args[-1]) != 10:
                                    return func(*args, **kwargs)
                                else:
                                    result = func(args, kwargs)
                                    return result
                            except:
                                return "The number should contain 10 digits."
                        else:
                            return func(*args, **kwargs)
                    except:
                        return "Pleae, enter correct phone number. It should contain only digits "
                else:
                    return func(*args, **kwargs)
            except:
                return "Please, give me name and phone"

        elif command[1] == 'show_phone':
            try:
                result = func(args, kwargs)
                return result
            except:
                return "Please, give me name"

    return inner
