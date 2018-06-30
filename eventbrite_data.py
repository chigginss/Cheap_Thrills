""" Data from Eventbrite's API """


# data = "https://www.eventbriteapi.com/v3/events/17920884849/?token=ANNKEY"
# price = free
# sanfrancisco.within=50mi

# https://www.eventbriteapi.com/v3/events/search/q=free-events-in-san-francisco/?token=GN4T6AHNFWXAD6BRF4WZ
# url = https://www.eventbriteapi.com/v3/events/search/?q=free+events+in+san+francisco&token=ZAKXWP2CDSBC2SS7RVYQ

# https://www.eventbriteapi.com/v3/events/search/?location.address=san+francisco&location.within=30mi&price=free&start_date.keyword=next_month&token=ZAKXWP2CDSBC2SS7RVYQ

#free events bay area month of July

url = "https://www.eventbriteapi.com/v3/events/search/?location.address=san+francisco&location.within=30mi&price=free&start_date.keyword=next_month&token={mytoken}".format(mytoken=mytoken)