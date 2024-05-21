class Compass:
    def __init__(self):
        self.directions = ['N', 'E', 'S', 'W']
        self.current_direction_index = 0  

    def rotate_left(self):
        self.current_direction_index = (self.current_direction_index - 1) % len(self.directions)
        print(f"Rotated left. Current direction: {self.directions[self.current_direction_index]}")

    def rotate_right(self):
        self.current_direction_index = (self.current_direction_index + 1) % len(self.directions)
        print(f"Rotated right. Current direction: {self.directions[self.current_direction_index]}")

    def get_current_direction(self):
        return self.directions[self.current_direction_index]

if __name__ == "__main__":
    compass = Compass()
    print(f"Initial direction: {compass.get_current_direction()}")
    
    
    compass.rotate_right()
    compass.rotate_right()
    compass.rotate_left()
    compass.rotate_left()
    compass.rotate_left()
