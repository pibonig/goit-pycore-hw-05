from functools import wraps


def input_error(func):
    @wraps(func)
    def run(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            print('Give me name and phone please.')
        except KeyError:
            print('Contact does not exist.')
        except IndexError:
            print('Contact does not exist.')

    return run
