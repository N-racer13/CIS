import time
import methods
import numpy as np
import assignment3
import ios


def test_closest_point_triangle():
    print("Starting test for closest point in triangle")
    print("-----------------------------------------------\n")

    found_error = False

    v1 = np.array([0, 0, 0])
    v2 = np.array([1, 0, 0])
    v3 = np.array([0, 1, 0])
    v4 = np.array([0, 0, 1])


    points = list()
    closest_points = list()
    points.append(np.array([0.3, 0.3, 10])) 
    closest_points.append(np.array([0.3, 0.3, 0]))
    points.append(np.array([0.3, 0.3, 0]))  
    closest_points.append(np.array([0.3, 0.3, 0]))
    points.append(np.array([-0.5, 0.5, 10]))  
    closest_points.append(np.array([0, 0.5, 0]))
    points.append(np.array([0.5, -0.5, 10]))
    closest_points.append(np.array([0.5, 0, 0]))
    points.append(np.array([1, 1, 0]))
    closest_points.append(np.array([0.5, 0.5, 0]))
    points.append(np.array([-0.5, -0.5, -10]))  
    closest_points.append(np.array([0, 0, 0]))
    for i in range(len(points)):
        if np.abs(np.mean(methods.ClosestPointTriangle(v1, v2, v3, points[i]) - closest_points[i])) > 0.0000001:
            print('Failed on point: ' + str(points[i]) + ' on first configuration z=0 plane triangle')
            found_error = True
        if np.abs(np.mean(methods.ClosestPointTriangle(v2, v1, v3, points[i]) - closest_points[i])) > 0.0000001:
            print('Failed on point: ' + str(points[i]) + ' on second configuration z=0 plane triangle') 
            found_error = True
        if np.abs(np.mean(methods.ClosestPointTriangle(v3, v2, v1, points[i]) - closest_points[i])) > 0.0000001:
            found_error = True
            print('Failed on point: ' + str(points[i]) + ' on third configuration z=0 plane triangle') 

   
    points = list()
    closest_points = list()
    points.append(np.array([10, 0.3, 0.3]))  
    closest_points.append(np.array([0, 0.3, 0.3]))
    points.append(np.array([0, 0.3, 0.3]))  
    closest_points.append(np.array([0, 0.3, 0.3]))
    points.append(np.array([10, 0.5, -0.5]))  
    closest_points.append(np.array([0, 0.5, 0]))
    points.append(np.array([10, -0.5, 0.5]))
    closest_points.append(np.array([0, 0, 0.5]))
    points.append(np.array([0, 1, 1]))
    closest_points.append(np.array([0, 0.5, 0.5]))
    points.append(np.array([-10, -0.5, -0.5]))  
    closest_points.append(np.array([0, 0, 0]))
    for i in range(len(points)):
        if np.abs(np.mean(methods.ClosestPointTriangle(v1, v3, v4, points[i]) - closest_points[i])) > 0.0000001:
            print('Failed on point: ' + str(points[i]) + ' on first configuration x=0 plane triangle')
            found_error = True
        if np.abs(np.mean(methods.ClosestPointTriangle(v3, v1, v4, points[i]) - closest_points[i])) > 0.0000001:
            print('Failed on point: ' + str(points[i]) + ' on second configuration x=0 plane triangle') 
            found_error = True
        if np.abs(np.mean(methods.ClosestPointTriangle(v4, v3, v1, points[i]) - closest_points[i])) > 0.0000001:
            found_error = True
            print('Failed on point: ' + str(points[i]) + ' on third configuration x=0 plane triangle') 
    
  
    points = list()
    closest_points = list()
    points.append(np.array([0.3, 10, 0.3])) 
    closest_points.append(np.array([0.3, 0, 0.3]))
    points.append(np.array([0.3, 0, 0.3]))  
    closest_points.append(np.array([0.3, 0, 0.3]))
    points.append(np.array([0.5, 10, -0.5]))  
    closest_points.append(np.array([0.5, 0, 0]))
    points.append(np.array([-0.5, 10, 0.5]))
    closest_points.append(np.array([0, 0, 0.5]))
    points.append(np.array([1, 0, 1]))
    closest_points.append(np.array([0.5, 0, 0.5]))
    points.append(np.array([-0.5, -10, -0.5]))  
    closest_points.append(np.array([0, 0, 0]))
    for i in range(len(points)):
        if np.abs(np.mean(methods.ClosestPointTriangle(v1, v2, v4, points[i]) - closest_points[i])) > 0.0000001:
            print('Failed on point: ' + str(points[i]) + ' on first configuration y=0 plane triangle')
            found_error = True
        if np.abs(np.mean(methods.ClosestPointTriangle(v2, v1, v4, points[i]) - closest_points[i])) > 0.0000001:
            print('Failed on point: ' + str(points[i]) + ' on second configuration y=0 plane triangle') 
            found_error = True
        if np.abs(np.mean(methods.ClosestPointTriangle(v4, v2, v1, points[i]) - closest_points[i])) > 0.0000001:
            found_error = True
            print('Failed on point: ' + str(points[i]) + ' on third configuration y=0 plane triangle')

    if not found_error:
        print('No errors were found.')
    print("-----------------------------------------------\n")


def test_procedure():
    print("Starting test for full procedure")
    print("-----------------------------------------------\n")
    chars = ['A', 'B', 'C', 'D', 'E', 'F']
    prefix = 'data/PA3-'
    ftype = '-Debug'
    body_a, tip_a, body_b, tip_b, vertices, triangles = assignment3.pre_process_objects()
    for char in chars:
        output_file_name = prefix+char+ftype+'-Output.txt'
        d_truth, c_truth = ios.loadoutput(output_file_name)
        start = time.time()
        d_linear, c_linear = assignment3.run_procedure(prefix, ftype, char, body_a, tip_a, body_b, vertices, triangles,
                                                     methods.ClosestPointLinearSearch)
        end = time.time()
        elapsed_brute = end-start
        start = end
        d_sphere, c_sphere = assignment3.run_procedure(prefix, ftype, char, body_a, tip_a, body_b, vertices, triangles,
                                                       methods.ClosestPointMeshBoundingSpheres)
        end = time.time()
        elapsed_sphere = end-start
        print("Statistics on debug dataset "+char)
        print("-----------------------------------------------")
        print("Error of c vectors using linear search:   " + str(np.mean(np.abs(c_truth-c_linear))))
        print("Error of c vectors using sphere method: " + str(np.mean(np.abs(c_truth-c_sphere))))
        print("Time elapsed using linear search: " + str(elapsed_sphere))
        print("Time elapsed using sphere method: " + str(elapsed_brute))
        print("-----------------------------------------------\n")


def main():
    test_closest_point_triangle()
    test_procedure()
    return


if __name__ == '__main__':
    main()
