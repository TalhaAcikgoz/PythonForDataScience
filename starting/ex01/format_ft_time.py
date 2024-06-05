import datetime, time

t = time.time()
st = "{:e}".format(t)
ts = (datetime.datetime.now() - datetime.datetime(1970, 1, 1))
ts = ts.total_seconds()
ts = "{:,}".format(ts)
print(f"Seconds since January 1, 1970: {ts} or {st} in scientific notation.")

dt = datetime.datetime.now()
print(dt.strftime("%B"), dt.strftime("%d"), dt.strftime("%Y"))