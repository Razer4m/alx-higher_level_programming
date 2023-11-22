#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except (TypeError, ZeroDivisionError):
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None
    else:
        return result
    finally:
        print("Inside result: {}".format(result))
