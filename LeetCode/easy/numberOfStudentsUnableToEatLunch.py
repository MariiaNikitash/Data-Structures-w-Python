class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        roundStudents = squareStudents = 0
        for s in students:
            if s == 0:
                squareStudents += 1
            else:
                roundStudents += 1

        for sandwich in sandwiches:
            if sandwich == 0:
                if squareStudents == 0:
                    break
                else:
                    squareStudents -= 1
            elif sandwich == 1:
                if roundStudents == 0:
                    break
                else:
                    roundStudents -= 1
        return roundStudents + squareStudents