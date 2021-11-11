"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart's maximum.
"""
user_age = int(input("How old are you?"))
min_heart_rate = (220 - user_age) * 0.65
max_heart_rate = (220 - user_age) * 0.85
print(f'When you exercise to strengthen your heart, you should keep your heart rate between {min_heart_rate:.0f} and {max_heart_rate:.0f} beats per minute.')
