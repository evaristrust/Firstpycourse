import pytz, datetime
# Going to check the time in moscow
# it requires that you have already installed the pytz libraries
# # pip3 install pytz using cmd
# country = "Africa/Bujumbura"
# time_to_display = pytz.timezone(country)
# print("The local time in {0} is: {1}".format(country, datetime.datetime.now(tz=time_to_display)))
# print("The UTC time is: {}".format(datetime.datetime.utcnow()))
#
# # checking which country/city you can use
#
# for y in pytz.all_timezones:
#     print(y)
#
# for x in pytz.country_names:
#     print(x, ": ", pytz.country_names[x])
#
# for w in sorted(pytz.country_names):
#     print("{}: {}: {}".format(w, pytz.country_names[w], pytz.country_timezones.get(w))) # get used to avoid error
#
#     # The above example can be done using if
#
# for t in sorted(pytz.country_names):
#     print("{}: {}".format(t, pytz.country_names[t]), end=": ")
#     if t in pytz.country_timezones:
#         print(pytz.country_timezones[t])
#     else:
#         print("There is no timezone defined")
#
# # The results are the same! right?
#
# # now that i want to display the places and their local time
# for t in sorted(pytz.country_names):
#     print("{}: {}".format(t, pytz.country_names[t]), end=": ")
#     if t in pytz.country_timezones:
#         for zone in sorted(pytz.country_timezones[t]):
#             time_to_display = pytz.timezone(zone)
#             local_time = datetime.datetime.now(tz=time_to_display)
#             print("\t\t{}: {}".format(zone, local_time))
#     else:
#         print("There is no timezone defined")

# we are going to localize time and timezones
my_local_time = datetime.datetime.now()
my_utc_time = datetime.datetime.utcnow()

localize_local = pytz.utc.localize(my_utc_time).astimezone() # this is ain't giving my local time!
localize_utc = pytz.utc.localize(my_utc_time)

print("My local time is {}, with {} timezone".format(localize_local, localize_local.tzinfo))
print("My UTC time is {}, with {} timezone".format(localize_utc, localize_utc.tzinfo))

print("**" * 40)
#
# def astimezone(self, tz=None):
#
#     if tz is None:
#         tz = self._local_timezone()
#     elif not isinstance(tz, tzinfo):
#         raise TypeError("tz argument must be an instance of tzinfo")
#
#     mytz = self.tzinfo # code from sami!
#     if mytz is None:
#         mytz = self._local_timezone()
#         myoffset = mytz.utcoffset(self)
#     else:
#         myoffset = mytz.utcoffset(self)
#         if myoffset is None:
#             mytz = self.replace(tzinfo=None)._local_timezone()
#             myoffset = mytz.utcoffset(self)
#
#     if tz is mytz:
#         return self
#
#     # Convert self to UTC, and attach the new time zone object.
#     utc = (self - myoffset).replace(tzinfo=tz)
#
#     # Convert from UTC to tz's local time.
#     return tz.fromutc(utc)
