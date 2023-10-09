def valid_flt(prompt: str):
    """
    Validates and returns float from input.
    :param prompt: input instruction
    :return: float value
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("!!! ERROR: ENTER NUMERIC VALUE ONLY !!!")
