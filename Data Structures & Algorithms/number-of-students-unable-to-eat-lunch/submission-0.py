class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count_hungry = 0

        while students and count_hungry < len(students):
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                count_hungry = 0
            else:
                students.append(students.pop(0))
                count_hungry += 1
        
        return count_hungry