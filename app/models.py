import datetime


def _get_time(as_integer=False):
    curr_datetime = datetime.datetime.now()
    response = curr_datetime.isoformat()
    print("as_integer {}".format(as_integer))
    if as_integer:
        response = curr_datetime.timestamp()
    return {
        "now": str(response)
    }
