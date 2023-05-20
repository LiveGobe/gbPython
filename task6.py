ticket_number = input("Введите номер билета: ")

if len(ticket_number) != 6:
    print("Некорректный номер билета")
else:
    first_half_sum = int(ticket_number[0]) + int(ticket_number[1]) + int(ticket_number[2])
    second_half_sum = int(ticket_number[3]) + int(ticket_number[4]) + int(ticket_number[5])

    if first_half_sum == second_half_sum:
        print("yes")
    else:
        print("no")