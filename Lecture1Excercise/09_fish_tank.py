length = int(input())
width = int(input())
height = int(input())
percent = float(input()) / 100

volume_in_liters = (length * width * height) / 1000
needed_liters = volume_in_liters - (volume_in_liters * percent)

print(needed_liters)