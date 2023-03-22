from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        rooms = []
        credits = []
        tasks = []
        for i in range(1, 50):
            room = request.form.get(f'room_{i}')
            task = request.form.get(f'task_{i}')
            credit = request.form.get(f'credit_{i}')
            if room and task and credit:
                rooms.append(int(room))
                tasks.append(task)
                credits.append(int(credit))

        new_credits = []
        c_32 = [2,7,12,18] # s_o -> K&Q Slipt bed : 20
        c_37 = [1]  # s_o -> Double : 25 
        c_27 = [3,4,5,6,8,9,10,11,13,14,15,16,17] # s_o -> standard : 15

        for i in range(len(rooms)):
            if int(str(rooms[i])[-2::]) in c_32 and (tasks[i] == 'Departure Clean' or tasks[i] == 'StayoverFullLinen'):
                new_credits.append(32)
            elif int(str(rooms[i])[-2::]) in c_37 and (tasks[i] == 'Departure Clean' or tasks[i] == 'StayoverFullLinen'):
                new_credits.append(37)
            elif int(str(rooms[i])[-2::]) in c_27 and (tasks[i] == 'Departure Clean' or tasks[i] == 'StayoverFullLinen'):
                new_credits.append(27)
            elif int(str(rooms[i])[-2::]) in c_32 and tasks[i] == 'Stay over':
                new_credits.append(20)
            elif int(str(rooms[i])[-2::]) in c_37 and tasks[i] == 'Stay over':
                new_credits.append(25)
            elif int(str(rooms[i])[-2::]) in c_27 and tasks[i] == 'Stay over':
                new_credits.append(15)

        before_credits = sum(credits)
        after_credits = sum(new_credits)
        minutes_to_hr = str(after_credits / 60)

        return render_template('index.html', credits=True, before_credits=before_credits, after_credits=after_credits, minutes_to_hr=minutes_to_hr)
    else:
        return render_template('index.html', credits=False)

if __name__ == '__main__':
    app.run(debug=True)
