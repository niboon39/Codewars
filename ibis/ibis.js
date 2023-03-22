const fs = require('fs');
const parse = require('csv-parse/lib/sync');

function sumCredits(roomList) {
    return roomList.reduce((a, b) => a + b, 0);
}

function minutesToHours(minutes) {
    return (minutes / 60).toString();
}

const data = parse(fs.readFileSync('ibis.csv', 'utf-8'), {
    columns: true,
    skip_empty_lines: true
});

const room = data.map(row => row.Room);
const tasks = data.map(row => row.Task);
const credits = data.map(row => parseInt(row.Credits, 10));

let newCredits = [];
let roomCredits = [];
const c32 = [2, 7, 12, 18];
const c37 = [1];
const c27 = [3, 4, 5, 6, 8, 9, 10, 11, 13, 14, 15, 16, 17];

for (let r = 0; r < room.length; r++) {
    const roomNumber = parseInt(room[r].slice(-2), 10);
    const task = tasks[r];

    if (c32.includes(roomNumber) && (task === 'Departure Clean' || task === 'StayoverFullLinen')) {
        newCredits.push(
