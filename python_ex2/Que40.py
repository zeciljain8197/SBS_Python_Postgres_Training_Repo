s = """
Greeting {0},

This is mail is to inform you that your pre-season tickets for the F1 2022 season have beeen
booked under the name of Mr/Mrs {0}

Please reply with you confirmation so as to confirm that you have received this mail and 
are informed about you ticket bookings.

The following circuit tickets have been booked by you-
1. {1}
2. {2}
3. {3}

Kindly reply on this email for any further information - "noreply.public@f1.com"
"""

res = s.format('Zecil Jain', 'Monaco', 'Spa-Belgium', 'Abu Dhabi')
print(res)