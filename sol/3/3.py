from collections import defaultdict#, default_factory
import csv
from dataclasses import dataclass
from datetime import date


@dataclass
class Department:
    start_year: int
    end_year: int
    dep_id: int
    name: str
    income: dict
         
    def __hash__(self):
        return self.dep_id


@dataclass 
class Operation:
    operation_id: int
    year: int
    month: int
    day: int
    dep_id: int
    income: float


def read_departments(file_name: str):
    with open(file_name) as file:
        reader = csv.reader(file, delimiter=",")
        next(reader)
        for row in reader:
            yield row


def read_operations(file_name: str):
    with open(file_name) as file:
        reader = csv.reader(file, delimiter=",")
        next(reader)
        for row in reader:
            yield row   


if __name__ == '__main__':
    rows = list(read_departments("departments.csv"))
    departments = dict()
    for row in rows:
        departments[int(row[0])] = Department(start_year=int(row[1]),
                                      end_year=int(row[2]),
                                      dep_id=int(row[0]),
                                      name=row[-1],
                                      income={})
    operation_generator = read_operations("operations.csv")
    for row in operation_generator:
        try:
            op_date = date(year=int(row[1]), month=int(row[2]), day=int(row[3]))
            dep_id = int(row[-2])
            department = departments[dep_id]
            if department.start_year <= op_date.year <= department.end_year:
                if op_date.year not in departments[dep_id].income:
                    departments[dep_id].income[op_date.year] = {}
                if op_date.month not in departments[dep_id].income[op_date.year]:
                    departments[dep_id].income[op_date.year][op_date.month] = 0
                departments[dep_id].income[op_date.year][op_date.month] += float(row[-1])
        except Exception as e:
            continue
    ans = []
    for dep_id in departments:
        for year in departments[dep_id].income:
            for month in departments[dep_id].income[year]:
                ans.append((year, month, departments[dep_id].name, int(departments[dep_id].income[year][month])))
    ans.sort()
    for _ in ans:
        print(*_)

