import csv
import subprocess

p = subprocess.Popen(["pip", "freeze", "--local"], stdout=subprocess.PIPE)
p.wait()


def find_home_page(details):
    for line in details:
        line = line.decode("utf-8")
        if 'Home-page:' in line:
            return line.strip().split('Home-page: ')[1]


def find_supported_pythons(details):
    supported_pythons = []
    for line in details:
        line = line.decode("utf-8")
        if "Programming Language :: Python " in line:
            try:
              supported_python = line.strip().split("Programming Language :: Python :: ")[1]
            except IndexError:
              pass
            else:
              try:
                supported_pythons.append(str(float(supported_python)))
              except ValueError:
                pass
    return supported_pythons


def find_supported_djangos(details):
    supported_djangos = []
    for line in details:
        line = line.decode("utf-8")
        if "Framework :: Django" in line:
            try:
              supported_django = line.strip().split("Framework :: Django :: ")[1]
            except IndexError:
              pass
            else:
              try:
                supported_djangos.append(str(float(supported_django)))
              except ValueError:
                pass
    return supported_djangos


with open('result.csv', 'w+') as csvfile:
    writer = csv.writer(csvfile)
    for line in p.stdout.readlines():
        dependency, version = line.decode("utf-8").strip().split("==")
        p2 = subprocess.Popen(
            ["pip", "show", "--verbose", dependency], stdout=subprocess.PIPE
        )
        p2.wait()
        details = p2.stdout.readlines()
        home_page = find_home_page(details)
        supported_pythons = find_supported_pythons(details)
        supported_djangos = find_supported_djangos(details)
        print([dependency, version, ', '.join(supported_pythons), ', '.join(supported_djangos), home_page])
        writer.writerow([dependency, version, ', '.join(supported_pythons), ', '.join(supported_djangos), home_page])

