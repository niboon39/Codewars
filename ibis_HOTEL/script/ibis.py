import pandas as pd 


def sum_credicts(room_list):
    return sum(room_list)

def minutes_2_hours(minutes):
    return str(minutes / 60)
    
if __name__ == "__main__":

    data = pd.read_csv("ibis.csv" )

    room = [i for i in data.Room]
    Tasks = [j for j in data.Task]
    credits = [k for k in data.Credits]

    new_credits = []
    room_credits = []
    c_32 = [2,7,12,18] # s_o -> K&Q Slipt bed : 20
    c_37 = [1]  # s_o -> Double : 25 
    c_27 = [3,4,5,6,8,9,10,11,13,14,15,16,17] # s_o -> standard : 15
    # print(int(str(room[0])[1::]))

    '''  NEW Credits  '''

    for r in range(len(room)):
        # print(room[r] ,int(str(room[r])[-2::]) , Tasks[r])
        # Check out & Full service 
        if (int(str(room[r])[-2::]) in c_32) and (Tasks[r] == 'Departure Clean'  or Tasks[r] == 'StayoverFullLinen'):
            new_credits.append(32)
            room_credits.append(room[r])
        elif (int(str(room[r])[-2::]) in c_37) and (Tasks[r] == 'Departure Clean' or Tasks[r] == 'StayoverFullLinen') :
            new_credits.append(37)
            room_credits.append(room[r])
        elif (int(str(room[r])[-2::]) in c_27) and (Tasks[r] == 'Departure Clean'or Tasks[r] == 'StayoverFullLinen'):
            new_credits.append(27)
            room_credits.append(room[r])
        # Stay over
        elif int(str(room[r])[-2::]) in c_32 and Tasks[r] ==  'Stay over':
            room_credits.append(room[r])
            new_credits.append(20)
        elif int(str(room[r])[-2::]) in c_37 and Tasks[r] ==  'Stay over':
            room_credits.append(room[r])
            new_credits.append(25)
        elif int(str(room[r])[-2::]) in c_27 and Tasks[r] ==  'Stay over':
            room_credits.append(room[r])
            new_credits.append(15)
        else:
            print(f'Fail : {room[r]} , {Tasks[r]}  ')
        
    # print(new_credits , len(new_credits))
    # print(room_credits)

    print(f"Before credits  : {sum_credicts(credits)}")
    print(f"After  credits  : {sum_credicts(new_credits)}")
    print(f"Minues to hours : {minutes_2_hours(sum_credicts(new_credits))} hr")