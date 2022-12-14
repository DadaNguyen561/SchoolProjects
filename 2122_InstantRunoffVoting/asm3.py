# COMP 1026 â€“ Assignment 3

# Dada Nguyen

# Write a program using data structures, functions and reading data from a file to simulate a preferential voting system.


# to read the input + create list
def read_file(file_name):
    with open(file_name, 'r') as fh:
        lines = fh.readlines()

    votes = []
    for line in lines:
        format_line = line.strip('\n')
        candidates = format_line.split(',')
        votes.append(candidates)

    return votes


# update vote
def updateVotes(votes, eliminatedCan):
    for vote in votes:
        if eliminatedCan in vote:
            vote.remove(eliminatedCan)
            vote.append('')


# elimination order
def elimOrder(votes):
    my_dict = dict()
    for vote in votes:
        firstPlace = vote[0]
        if firstPlace != '':
            if firstPlace not in my_dict:  # first time
                my_dict[firstPlace] = 1
            else:  # subsequent time.
                my_dict[firstPlace] += 1

    least_voted_num = min(my_dict.values())
    can_least_voted_num = []
    for key, value in my_dict.items():
        if value == least_voted_num:
            can_least_voted_num.append(key)

    for i in range(0, len(can_least_voted_num)):
        can_least_voted_num[i] = int(can_least_voted_num[i])
    return str(max(can_least_voted_num))


# to find the winner
def winner(votes):
    my_dict = dict()
    for vote in votes:
        count = vote[0]

        # to count vote
        if count != '':
            if count not in my_dict:  # first time
                my_dict[count] = 1
            else:  # subsequent time.
                my_dict[count] += 1

    # to find winner in the first-place vote
    for k, v in my_dict.items():
        totalVote = sum(my_dict.values())
        percentVotes = v / totalVote
        if percentVotes > 0.5:

            losers = []
            for elmt in my_dict:
                if elmt != k:
                    losers.append(elmt)

            for i in range(0, len(losers)):
                losers[i] = int(losers[i])
            losers.sort()

            for i in range(0, len(losers)):  # need to convert it back from integer to a string
                losers[i] = str(losers[i])

            losers.append(k)  # put back the winner to the last position of the list
            return losers


# main function
def main():
    file_name = input('Enter the name of the file: ')
    votes = read_file(file_name)
    elimination_list = []

    w = None
    while w is None:
        w = winner(votes)
        if w is None:
            e = elimOrder(votes)
            elimination_list.append(e)
            updateVotes(votes, e)

    final_list = elimination_list + w
    pretty = (', '.join(final_list))
    print("Elimination order:", pretty)

main()