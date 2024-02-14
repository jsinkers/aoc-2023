import re
from itertools import combinations
import sympy as sp

def part_1(lines, min_p=7, max_p=27):
    # parse input "px py pz @ vx vy vz"
    # velocities are distance/nanosecond
    hailstones = []
    for line in lines:
        position, velocity = line.split('@')
        position = position.split(',')
        position = [int(x) for x in position]
        velocity = velocity.split(',')
        velocity = [int(x) for x in velocity]
        hailstones.append((position, velocity))
    
    # solve analytically
    x1, y1, z1, x2, y2, z2, t1, t2, vx1, vy1, vz1, vx2, vy2, vz2 = sp.symbols('x1 y1 z1 x2 y2 z2 t1 t2 vx1 vy1 vz1 vx2 vy2 vz2')
    pos_x = x1 + t1*vx1
    pos_y = y1 + t1*vy1
    f1 = sp.Eq(x1 + t1 * vx1, x2 + t2 * vx2)
    f2 = sp.Eq(y1 + t1 * vy1, y2 + t2 * vy2)
    soln = sp.solve((f1, f2), (t1, t2))
    print(soln)
    

    # determine intersection by solving for equation of 2 lines
    combs = combinations(hailstones, 2)
    num_combs = sum(1 for ignore in combinations(hailstones, 2))
    print(num_combs)
    num_inside = 0
    for i, (h1, h2) in enumerate(combs):
        if i % 1000 == 0:
            print(f"{i}: {num_inside}")

        p1, v1 = h1
        p2, v2 = h2

        mapping = {x1: p1[0], y1: p1[1], vx1: v1[0], vy1: v1[1], x2: p2[0], y2: p2[1], vx2: v2[0], vy2: v2[1]}
        int1 = soln[t1].subs(mapping)
        int2 = soln[t2].subs(mapping)
        if int1 == sp.zoo or int2 == sp.zoo:
            #print("No intersection")
            continue
        elif int1 < 0 or int2 < 0:
            #print("Intersection in past")
            continue
        else:
            int_x = pos_x.evalf(subs={x1: p1[0], y1: p1[1], vx1: v1[0], vy1: v1[1], t1: int1})
            int_y = pos_y.evalf(subs={x1: p1[0], y1: p1[1], vx1: v1[0], vy1: v1[1], t1: int1})
            #print(f"Intersection at {int_x:.2f}, {int_y:.2f}")
            if min_p <= int_x <= max_p and min_p <= int_y <= max_p:
                #print("Intersection within bounds")
                num_inside += 1

    return num_inside
    
def part_2(lines):
    # parse input "px py pz @ vx vy vz"
    # velocities are distance/nanosecond
    hailstones = []
    for line in lines:
        position, velocity = line.split('@')
        position = position.split(',')
        position = [int(x) for x in position]
        velocity = velocity.split(',')
        velocity = [int(x) for x in velocity]
        hailstones.append((position, velocity))
    
    # unknowns: rx, ry, rz, ru, rv, rw, t
    rx, ry, rz, ru, rv, rw = sp.symbols('rx ry rz ru rv rw')
    t_symbols = []
    equations = []
    for i, hailstone in enumerate(hailstones[:3]):
        print(i)
        pos, vel = hailstone
        x, y, z = pos
        u, v, w = vel
        t = sp.Symbol(f"t{i}")
        t_symbols.append(t)
        eqx = sp.Eq(x + t * u, rx + t * ru)
        eqy = sp.Eq(y + t * v, ry + t * rv)
        eqz = sp.Eq(z + t * w, rz + t * rw)
        equations.append(eqx)
        equations.append(eqy)
        equations.append(eqz)

    soln = sp.solve(equations, (rx, ry, rz, ru, rv, rw) + tuple(t_symbols))
    return sum(soln[0][:3])

if __name__ == '__main__':
    with open('test.txt', 'r') as f:
        test_lines = f.readlines()

    with open('input.txt', 'r') as f:
        input_lines = f.readlines()
    
    print("Part 1 ======================")
    test_vals = part_1(test_lines)
    print(f"Test output: {test_vals}")
    #input_vals = part_1(input_lines, min_p=200000000000000, max_p=400000000000000)
    #print(f"Real output: {input_vals}")

    print("Part 2 ======================")
    test_vals = part_2(test_lines)
    print(f"Test output: {test_vals}")
    input_vals = part_2(input_lines)
    print(f"Real output: {input_vals}")