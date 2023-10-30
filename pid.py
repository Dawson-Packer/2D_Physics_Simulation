class PID:
    def __init__(self):
        """
        @brief PID controller for robot movement.
        """
        self.p_value = 0.0
        self.d_value = 0.0
        self.i_value = 0.0
        self.cross_track_error = 0.0
        self.previous_cross_track_error = 0.0

    def correct_heading(self):
        """
        @brief Function to correct the heading of the robot.
        @return Returns the change in heading necessary to correct the robot for this iteration.
        """
        self.p_value = self.cross_track_error
        self.d_value = (self.cross_track_error - self.previous_cross_track_error) / (1)
        self.i_value += self.cross_track_error * (1)

        proportion_coeff = 1.250
        derivate_coeff = 0.200
        integral_coeff = 1.000

        correction = (proportion_coeff * self.p_value) + (derivate_coeff * self.d_value)\
             # + (integral_coeff * self.i_value)
        self.previous_cross_track_error = self.cross_track_error
        return correction
