import csv
from app.models import Company
from threading import *


def upload_user_data(file_name=None):
    if file_name:
        count = 0
        query_list = []
        for row in read_csv(file_name):
            name = row['name']
            domain = row['domain']
            try:
                year_founded = int(row['year founded'])
            except ValueError:
                year_founded = 0
            industry = row['industry']
            size_range = row['size range']
            locality = row['locality']
            country = row['country']
            linkedin_url = row['linkedin url']
            current_employee = int(row['current employee estimate'])
            total_employee = int(row['total employee estimate'])
            q = Company(name=name, domain=domain, year_founded=year_founded, industry=industry,
                        size=size_range, locality=locality, country=country, linkedin_url=linkedin_url,
                        current_employees=current_employee, total_employee=total_employee)
            query_list.append(q)
            count += 1
            if count == 10000:
                try:
                    Company.objects.bulk_create(query_list)
                except Exception as e:
                    print(str(e))
                    raise e
                count = 0
                query_list.clear()


def read_csv(file_name):
    with open(file_name, "r", encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            yield row


if __name__ == '__main__':
    upload_user_data('media\sample.csv')
