class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort()
        position, speed = zip(*cars)
        position = list(position)
        speed = list(speed)
        fleet_count = 0
        while len(position) > 0:
            starting_position = position[-1]
            top_speed = speed[-1]
            expected_arrival = (target - starting_position) / top_speed
            soonest_arrival = expected_arrival
            position.pop()
            speed.pop()

            while len(position) > 0 and soonest_arrival <= expected_arrival:
                starting_position = position[-1]
                current_speed = speed[-1]
                soonest_arrival = (target - starting_position) / current_speed
                if soonest_arrival <= expected_arrival:
                    position.pop()
                    speed.pop()


            fleet_count += 1

        return fleet_count
            