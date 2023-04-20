# NAME: Lauren Magura
# Program Purpose: This program uses PYTHON SETS to display PVCC
#   REQUIRED courses & TECHNICAL ELECTIVE courses for:
#   --CSC certificate in Computer & Network Support Technologies:
#     --required courses
#     --plus 3 technical electives
#   --AAS degree in Information Technology:
#     ---required courses
#     ---plus 4 technical electives

# create sets for  CERTIIFICATE, Computer & Network Support Technologies
network_req = {'CSC 110', 'ETR 164', 'ITN 101',}

network_elect = {'CSC 201', 'CSC 202', 'CSC 205', 
        'ETR 113', 'ETR 149', 'ETR 203', 'ETR 290', 
        'ITN 106', 'ITN 120', 'ITN 151', 'ITN 170', 'ITN 260', 'ITN 290', 
        'ITP 120', 'ITP 132', 'ITP 200', 'ITP 220', 'ITP 290', 
        'MTH 131', 'MTH 161', 'MTH 162', 'MTH 263', }

#create sets for ASSOCIATE degree, Information Technology degree:
info_req = { 'CSC 110',  'ENG 111',  'ENG 112',  'ETR 149',  'ETR 164',  'ITD 110',
                 'ITD 132',  'ITE 182',  'ITE 215',  'ITN 101',  'ITN 106',  'ITN 111',
                 'ITP 120',  'MTH 131',}

info_elect ={'ITN 170', 'ITN 208', 'ITN 260', 'ITN 261',
                       'ITN 276', 'ITN 277', 'ITP 132', 'ITP 136', 'ITP 150', 'ITP 220',}

dash_line = "------------------------------------------------------"
output_file = "output.txt"

def main():
    global file_name
    # Open the file for writing
    with open(file_name, 'w') as f:
        f.write("**************Piedmont Virginia Community College********************\n")
        
        process_network_courses()
        f.write("\nREQUIRED COURSES FOR CSC CERTIFICATE IN COMPUTER & NETWORK SUPPORT TECHNOLOGIES:\n")
        f.write(dash_line + "\n")
        f.write("Number of Required Courses: {}\n".format(num_net_req))
        f.write("Total Credit Hours: {}\n".format(tot_net))
        f.write("All Required Courses:\n")
        f.write("----------------------\n")
        f.write('\n'.join(all_net_courses))
        
        f.write("\nTECHNICAL ELECTIVE COURSES FOR CSC CERTIFICATE IN COMPUTER & NETWORK SUPPORT TECHNOLOGIES:\n")
        f.write(dash_line + "\n")
        f.write("Number of Technical Elective Courses: {}\n".format(num_net_elect))
        f.write("Total Credit Hours: {}\n".format(tot_net_elect))
        f.write("All Technical Elective Courses:\n")
        f.write("----------------------\n")
        f.write('\n'.join(network_elect))
        
        process_info_courses()
        f.write("\nREQUIRED COURSES FOR AAS DEGREE IN INFORMATION TECHNOLOGY:\n")
        f.write(dash_line + "\n")
        f.write("Number of Required Courses: {}\n".format(num_info_req))
        f.write("Total Credit Hours: {}\n".format(tot_info))
        f.write("All Required Courses:\n")
        f.write("----------------------\n")
        f.write('\n'.join(all_info_courses))
        
        f.write("\nTECHNICAL ELECTIVE COURSES FOR AAS DEGREE IN INFORMATION TECHNOLOGY:\n")
        f.write(dash_line + "\n")
        f.write("Number of Technical Elective Courses: {}\n".format(num_info_elect))
        f.write("Total Credit Hours: {}\n".format(tot_info_elect))
        f.write("All Technical Elective Courses:\n")
        f.write("----------------------\n")
        f.write('\n'.join(info_elect))
        
        process_courses_in_both()
        f.write("\nTECHNICAL ELECTIVE COURSES THAT APPLY TO BOTH THE CSC CERTIFICATE AND THE AAS DEGREE:\n")
        f.write(dash_line + "\n")
        f.write("Number of Technical Elective Courses: {}\n".format(num_both_elect))
        f.write("Total Credit Hours: {}\n".format(tot_both_elect))
        f.write("All Technical Elective Courses:\n")
        f.write("----------------------\n")
        f.write('\n'.join(elect_both))
    
    print("Output written to file:", file_name)


def process_network_courses(file):
    global network_elect  # this set must be global since it is CHANGED in this function
    global num_net_req, num_net_elect, tot_net, all_net_courses
    temp_set = set()  # create a new empty set

    for course in network_elect:
        asterisk_course = "*" + course  # insert an asterisk in front of ELECTIVE course name
        temp_set.add(asterisk_course)  # then add the new course name to the temporary set

    network_elect.clear()  # remove all courses from set of elective courses
    network_elect = temp_set.copy()  # COPY all the courses from the temporary set back into the elective set

    num_net_req = len(network_req)
    num_net_elect = len(network_elect)
    tot_net = num_net_req + num_net_elect
    all_net_courses = network_req.union(network)
