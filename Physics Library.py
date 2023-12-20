class PhysicsFormulas:
    @staticmethod
    def displacement(initial_position, final_position):
        """
        Calculate displacement.
        """
        return final_position - initial_position

    @staticmethod
    def average_velocity(displacement, time_interval):
        """
        Calculate average velocity.
        """
        return displacement / time_interval

    @staticmethod
    def acceleration(initial_velocity, final_velocity, time_interval):
        """
        Calculate acceleration.
        """
        return (final_velocity - initial_velocity) / time_interval

    @staticmethod
    def kinematic_equation(initial_velocity, acceleration, time_interval):
        """
        Calculate final velocity using the kinematic equation.
        """
        return initial_velocity + acceleration * time_interval

    @staticmethod
    def kinetic_energy(mass, velocity):
        """
        Calculate kinetic energy.
        """
        return 0.5 * mass * velocity**2

    @staticmethod
    def potential_energy(mass, gravity, height):
        """
        Calculate potential energy.
        """
        return mass * gravity * height


if __name__ == "__main__":
    physics = PhysicsFormulas()

    initial_position = 0
    final_position = 10
    displacement = physics.displacement(initial_position, final_position)

    initial_velocity = 2
    final_velocity = 8
    time_interval = 4
    acceleration = physics.acceleration(initial_velocity, final_velocity, time_interval)

    print(f"Displacement: {displacement}")
    print(f"Acceleration: {acceleration}")