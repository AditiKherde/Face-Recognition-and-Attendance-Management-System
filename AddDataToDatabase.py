
ref = db.reference('Students')

data = {
    "852741":
        {
            "name": "Emily Blunt",
            "major": "Econmics",
            "starting_year": 2018,
            "total_attendance": 12,
            "standing": "B",
            "year": 1,
            "last_attendance_time": "2022-12-11 00:54:34"

        },
    "963852":
        {
            "name": "Elon Musk ",
            "major": "Physics",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"

        },
    "EN21CS304007":
        {
            "name": "Aditi Kherde",
            "major": "Computer Science",
            "starting_year": 2021,
            "total_attendance": 20,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2024-04-10 07:55:10"
        }
}
for key, value in data.items():  # unzip dictionary in python (this is jason format which is same as dictionary saves values in key value pair)
    ref.child(key).set(value)
