class PID:
    def __init__(self, kp, ki, kd):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.last_error = 0
        self.integral = 0
    
    def update(self, error, dt):
        # Calculate the derivative term
        derivative = (error - self.last_error) / dt
        
        # Calculate the integral term
        self.integral += error * dt
        
        # Calculate the output value
        output = self.kp * error + self.ki * self.integral + self.kd * derivative
        
        # Update the last error value
        self.last_error = error
        
        return output
