import numpy as np  # numpy library used to create exponential distribution
lambda_interarrival = input('Enter value of lambda (customer per time unit):')
myu_service = input(
    'Enter value of myu (no of customers serviced per time unit):')
_throughput = input(
    'Enter throughput value (simulation length in terms of no of people served):')
_warm_up = input(
    'Enter warm up throughput value (initial no of people served):')
replications = input('Enter number of replications:')


_lambda = int(lambda_interarrival)  # changing input string into integer
_myu = int(myu_service)   # changing input string into integer
throughput = int(_throughput)   # changing input string into integer
warm_up = int(_warm_up)   # changing input string into integer
num_of_replications = int(replications)   # changing input string into integer
'''



'''

# creating an empty list to store wait time obtained from every replication
avg_wait_per_replication = []
total_wait = 0

for x in range(num_of_replications):  # running simulation for no of replication times

    expo_interarrival_time = []  # an empty list to store exponential interarrival time
    expo_service_time = []  # an empty list to store exponential service time

    # empty arrival time list of size equals to throughput value
    arrival_time = [None] * throughput
    # empty service start time list of size equals to throughput value
    service_start_time = [None] * throughput
    # empty service finish time list of size equals to throughput value
    service_finish_time = [None] * throughput
    # empty wait time list of size equals to throughput value
    wait = [None] * throughput
    total_wait_per_replication = 0

    arrival_time[0] = 0  # system starts empty and idel
    service_start_time[0] = 0  # system starts empty and idel

    for i in range(throughput):
        # generating exponential interarrival times
        expo_interarrival_time.append(np.random.exponential(1 / _lambda))
        # generating exponential service times
        expo_service_time.append(np.random.exponential(1 / _myu))

    # first customer finish service after service time plus initial start time
    service_finish_time[0] = expo_service_time[0]

    for i in range(throughput - 1):
        # arrival time for a customer is equal to arrival time of previous plus interarrival time
        arrival_time[i + 1] = arrival_time[i] + expo_interarrival_time[i]
        # service time of a customer is either service finish of previous one or arrival of his own, which ever is biogger
        service_start_time[i +
                           1] = max(arrival_time[i + 1], service_finish_time[i])
        # service finish time of a customer is start time plus expo service time for him
        service_finish_time[i + 1] = service_start_time[i +
                                                        1] + expo_service_time[i + 1]

    for i in range(throughput):
        # wait for a customer is service start time minus arrival time
        wait[i] = service_start_time[i] - arrival_time[i]

    # eliminating warm up from calculation
    wait_after_warm_up = wait[num_of_replications:]

    for i in range(len(wait_after_warm_up)):
        # calculate total cumulative wait
        total_wait_per_replication += wait_after_warm_up[i]

    # calculate average wait for each replication
    avg_wait_per_replication.append(
        total_wait_per_replication / len(wait_after_warm_up))
    num_in_queue = []
    num_in_queue.append(0)
    for i in range(len(arrival_time) - 1):
        num_in_queue.append(
            min(list(map(lambda x: x / arrival_time[i + 1], service_finish_time[:i + 1]))))

for i in range(len(avg_wait_per_replication)):
    total_wait += avg_wait_per_replication[i]
# find average for all replications
average_wait = total_wait / len(avg_wait_per_replication)

print('\nAverage wait:', average_wait, 'time unit')
