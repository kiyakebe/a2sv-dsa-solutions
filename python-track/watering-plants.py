class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        watering_can = capacity
        n = len(plants)
        step_counter = 0
        for i in range(n):
            if(watering_can >= plants[i]):
                watering_can -= plants[i] # water the plant
                step_counter += 1
            else:
                # takes i step to get back to water
                step_counter += i
                watering_can = capacity # refil
                step_counter += i + 1 # get back to plant
                watering_can -= plants[i] # water the plant

        return step_counter