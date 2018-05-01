def minutes_to_hours(minutes):
	return minutes / 60.0


def seconds_to_hours(seconds):
	return seconds / 3600.0

def time_to_hours(seconds, minutes=0):
	return minutes / 60.0 + seconds / 3600.0


print(minutes_to_hours(3507))
print(seconds_to_hours(3507))
print(time_to_hours(3507, 40))
