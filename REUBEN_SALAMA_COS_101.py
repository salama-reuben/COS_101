def calculate_force(mass,acceleration):
    """calculate force using F=m*acceleration"""
    return mass*acceleration

def calculate_power(work,time):
    """calculate power using p=w /t."""
    return work / time

def calculate_centripetal_force(mass,velocity,radius):
     """calculate centripetal force."""
     return (mass*velocity**2)/radius

 def calculate_torque(r, F):
      """calculate torque."""
      return r * F

 def calculate_kinetic_energy(m, v):
    """calculate kinetic energy."""
    return 0.5 * m * v**2

def main():
    print("welcome to physics 101!")
    print("enter 'a' to calculate force or 'e' to calculate kinetic energy.")
    user_input= input("your choice:").strip().lower()

    if user_input =='a':
        mass= float(input("enter mass (kg):"))
        acceleration= float(input("enter acceleration(m/s^2):"))
        force = calculate_force(mass, acceleration)
        print(f"the calculated force is {force}N.")

        var = user_input == 'e'
        mass = float(input("enter mass (kg):"))
        velocity = float(input("enter velocity (m/s):"))
        kinetic_energy= calculate_kinetic_energy(mass, velocity)
        print(f"the calculated kinetic energy is {kinetic_energy}J.")

    else:
        print("invalid input.please enter 'a' or 'e'.")



