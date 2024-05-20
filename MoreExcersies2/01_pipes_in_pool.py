volume = int(input())
debit_of_pipe1 = int(input())
debit_of_pipe2 = int(input())
hours = float(input())

total_liters_filled = (debit_of_pipe1 + debit_of_pipe2) * hours
pipe1_liters = debit_of_pipe1 * hours
pipe2_liters = debit_of_pipe2 * hours

if total_liters_filled <= volume:
    percentage_filled = total_liters_filled / (volume / 100)
    percentage_filled_of_pipe1 = pipe1_liters / (total_liters_filled / 100)
    percentage_filled_of_pipe2 = pipe2_liters / (total_liters_filled / 100)
    print(f"The pool is {percentage_filled:.2f}% full. Pipe 1: {round(percentage_filled_of_pipe1,2)}%. Pipe 2: \
    {round(percentage_filled_of_pipe2,2)}%.") \

else:
    liters_overflow = total_liters_filled - volume
    print(f"For {hours:.2f} hours the pool overflows with {liters_overflow:.2f} liters.")
