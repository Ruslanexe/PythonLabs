from Lab9.Figures import Circle, Triangle, Cylinder, Cone, Sphere

sasha = Circle("Sasha", "2D", 3, True)
print(sasha.print_circle())
anton = Triangle("Anton", "2D", 1, False)
print(anton.print_triangle())
anya = Cylinder("Anya", "3D", 9, 3.12)
print(anya.print_cylinder())
illya = Cone("Illya", "3D", 3, True)
print(illya.print_cone())
tanya = Sphere("Tanya", "3D", 1, True)
