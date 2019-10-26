import datetime


def str_to_datetime(time_str):
    temptime = datetime.datetime.strptime(time_str, '%Y-%m-%dT%H:%M:%S.%fZ')
    return temptime + datetime.timedelta(hours=8)
