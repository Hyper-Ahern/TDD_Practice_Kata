class Game:

    def __init__(self):
        self.rolls = [0] * 21
        self.current_roll = 0

    def roll(self, pins):
        self.rolls[self.current_roll] = pins
        self.current_roll += 1

    def score(self):
        total_score = 0
        frame_index = 0
        for frame in range(0, 10):
            if self.is_strike(frame_index):
                total_score += self.strike_bonus(frame_index)
                frame_index += 1
            elif self.is_spare(frame_index):
                total_score += self.spare_bonus(frame_index)
                frame_index += 2
            else:
                total_score += self.sum_of_balls_in_frame(frame_index)
                frame_index += 2
        return total_score

    def sum_of_balls_in_frame(self, frame_index):
        return self.rolls[frame_index] + self.rolls[frame_index + 1]

    def spare_bonus(self, frame_index):
        return 10 + self.rolls[frame_index + 2]

    def strike_bonus(self, frame_index):
        return 10 + self.rolls[frame_index + 1] + self.rolls[frame_index + 2]

    # The next two methods return a true or false value based on an immediate evaluation on if the equations are true
    def is_spare(self, frame_index):
        return self.rolls[frame_index] + self.rolls[frame_index + 1] == 10

    def is_strike(self, frame_index):
        return self.rolls[frame_index] == 10
