def try_again():
    answer = input("Do you want to try again? [Y/N]: ")
    if answer == "Y":
        start()
    elif answer == "N":
        exit()
    else:
        try_again()

def SRTF(process_num):
    arrival_time = []
    process_burst_time = []
    ctr = 1

    for _ in range(process_num):
        try:
            
            input_burst_time = int(input(f"Enter Burst time for P{ctr}: "))
            input_arrival_time = int(input(f"Enter Arrival time P{ctr}: "))
            print('\n')

            if input_burst_time <= 0 or input_arrival_time < 0:
                raise ValueError()

            arrival_time.append(input_arrival_time)
            process_burst_time.append(input_burst_time)
            ctr += 1

        except ValueError:
            print("Burst time must be a positive integer and Arrival Time must be a positive integer or zero")
            exit()

    remaining_time = process_burst_time.copy()
    completed = [False] * process_num
    current_time = 0

    print("-"*55)
    print("Process\tCompletion Time\tTurnaround Time\tWaiting Time")

    turnaround_time_list = []
    waiting_time_list = []
    completion_time_list = []

    while not all(completed):
        min_remaining_time = float('inf')
        shortest_job = None

        for i in range(process_num):
            if not completed[i] and arrival_time[i] <= current_time and process_burst_time[i] < min_remaining_time:
                min_remaining_time = process_burst_time[i]
                shortest_job = i

        if shortest_job is None:
            current_time += 1
            continue

        remaining_time[shortest_job] -= 1
        current_time += 1

        if remaining_time[shortest_job] == 0:
            completed[shortest_job] = True
            turnaround_time = current_time - arrival_time[shortest_job]
            waiting_time = turnaround_time - process_burst_time[shortest_job]
            completion_time = current_time

            turnaround_time_list.append(turnaround_time)
            waiting_time_list.append(waiting_time)
            completion_time_list.append(completion_time)

            print(f"P{shortest_job+1}\t\t{completion_time}\t\t{turnaround_time}\t\t{waiting_time}")

    average_turnaround_time = sum(turnaround_time_list)/len(turnaround_time_list)
    average_waiting_time = sum(waiting_time_list)/len(waiting_time_list)
    average_completion_time = sum(completion_time_list)/len(completion_time_list)
    
    print(f"Average\t\t{round(average_completion_time, 3)}\t\t{round(average_turnaround_time, 3)}\t\t{round(average_waiting_time, 3)}")

    print("-"*55)

    try_again()


def start():
    try:
        process_num = int(input("How many processes: "))

    except ValueError:
        print("Input is not a valid number of processes")
        exit()

    print('\n')
    SRTF(process_num)


start()
