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

def main():
    filename = input("Enter filename")
    with open("filename", "r") as f:
        f.write("********************Piedmont Virginia Community College********************")
        process_network_courses()
        display_network_courses(f)
        f.seek(0)  # reset the file pointer
        courses = load_courses(f)
        display_info_courses(courses)

        process_info_courses()
        display_info_courses(f)

        process_courses_in_both()
        display_courses_in_both(f)

    print("The course data has been written to the file 'pvcc_courses.txt'.")


def process_network_courses():
    global network_elect #this set must be global since it is CHANGED in this function
    global num_net_req, num_net_elect, tot_net, all_net_courses
    temp_set = set() #then add the new course to the temporary set

    for course in network_elect:
        asterisk_course = "*" + course #insert an asterisk in front of ELECTIVE course name
        temp_set.add(asterisk_course) # then add the new course name to a temporary set

    network_elect.clear() #remove all courses from set of elective courses
    network_elect = temp_set.copy() #COPY all the courses from the temporary set back into the elective set

    num_net_req = len(network_req)
    num_net_elect = len(network_elect)
    tot_net = num_net_req + num_net_elect
    all_net_courses = network_req.union(network_elect) #UNION: create a new set with ALL network courses

def display_network_courses(file):
    file.write("Courses offered by the Network department:\n")
    with open("network_courses.txt", "w") as f:
        f.write("CERTIFICATE: Computer & Network Support Technology\n")
        f.write(dash_line + "\n")
        f.write("Number of required courses    : " + str(num_net_req) + "\n")
        f.write("Number of elective courses    : " + str(num_net_elect) + "\n")
        f.write("Total number of Cert. courses : " + str(tot_net) + "\n")
        f.write(dash_line + "\n")
        f.write("All Certificate courses: \n")
        num = 1
        for course in all_net_courses:
            f.write(course + " ")
            num += 1
            if num % 5 == 0:
                f.write(course + "\n")
        f.write("\nNOTES:\n")
        f.write("  *Asterisk indicates ELECTIVE course\n")
        f.write("  Student choose 3 technical elective course\n")
        f.write(dash_line + "\n")


def process_info_courses():
    #student: add code for processing info course here
    print("here")

def display_info_courses(f):
    f.write("\n\nCourse Information:\n\n")
    for course in courses:
        f.write(f"Course Name: {course['name']}\n")
        f.write(f"Course Number: {course['number']}\n")
        f.write(f"Description: {course['description']}\n")
        f.write("\n")
    #student: add code for printin info course here
    print("now here")

def process_courses_in_both():
    both_req = network_req.intersection(info_reg)
    print(dash_line)
    print("REQUIRED courses in both programs:")
    num = 1
    for course in both_req:  #Display 5 courses per line
        print(course, end = " ")
        num += 1
        if num % 5 == 0:
            print()
    #student: add code for elective in both courses here

main()
