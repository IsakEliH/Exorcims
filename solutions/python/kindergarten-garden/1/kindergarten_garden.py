class Garden:
    def __init__(
        self, garden: str,
        diagram: dict[str: str] = {
            "G": "Grass",
            "C": "Clover",
            "R": "Radishes",
            "V": "Violets",
        },
        students: list[str] = [
            "Alice",
            "Bob",
            "Charlie",
            "David",
            "Eve",
            "Fred",
            "Ginny",
            "Harriet",
            "Ileana",
            "Joseph",
            "Kincaid",
            "Larry",
        ],
    ):
        self.garden = garden.split("\n")
        self.diagram = diagram
        self.students = sorted(students)

    def plants(self, student_name):
        index = self.students.index(student_name) * 2

        top= self.garden[0]
        bottom = self.garden[-1]

        top_row = top[index: index + 2]
        bottom_row = bottom[index: index + 2]
        

        combined = list(top_row + bottom_row)
        final_list = []

        for i in combined:
            final_list.append(self.diagram[i])

        return final_list
