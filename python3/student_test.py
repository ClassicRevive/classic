from ds_student import Student

def main():

    s1 = Student(15334499, 'Jones', 'Zoe', "CA1")
    s1.add_mark('CA103', 71)
    s1.add_mark('CA106', 65)
    s1.add_mark('CA115', 84)
    s1.add_mark('CA116', 85)
    s1.add_mark('CA117', 70)
    s1.add_mark('CA169', 68)
    s1.add_mark('CA170', 74)
    s1.add_mark('CA172', 90)
    s1.add_mark('MS121', 50)

    s2 = Student(15667755, "Brent", "Tom", "ca1")
    s2.add_mark('CA103', 55)
    s2.add_mark('CA106', 35)
    s2.add_mark('CA115', 70)
    s2.add_mark('CA116', 64)
    s2.add_mark('CA117', 66)
    s2.add_mark('CA169', 50)
    s2.add_mark('CA170', 55)
    s2.add_mark('CA172', 60)
    s2.add_mark('MS121', 35)

    s3 = Student(15112277, 'Brody', 'Joe', "ca1")
    s3.add_mark('CA103', 35)
    s3.add_mark('CA106', 35)
    s3.add_mark('CA115', 60)
    s3.add_mark('CA116', 60)
    s3.add_mark('CA117', 60)
    s3.add_mark('CA169', 60)
    s3.add_mark('CA170', 60)
    s3.add_mark('CA172', 60)
    s3.add_mark('MS121', 60)

    s4 = Student(19329261, 'Oluwasanya', 'Joseph', "DS1")
    s4.add_mark('MS130', 92)
    s4.add_mark('MS129', 92)
    s4.add_mark('CA115', 76)
    s4.add_mark('MS117', 86)
    s4.add_mark('CA116', 100)
    s4.add_mark('CA117', 100)
    s4.add_mark('CA119', 74)
    s4.add_mark('MS104', 90)
    s4.add_mark('MS103', 94)

    print(s1)
    print(s2)
    print(s3)
    print(s4)

if __name__ == '__main__':
    main()