import re
#f = open("raw.txt", "r", encoding="utf-8")
#text = f.read()
#print(text)
with open("raw.txt", "r", encoding="utf-8") as f:
    all_lines = " ".join(f.readlines())

company_name = re.search(r"ДУБЛИКАТ\n(.+)\n", all_lines).group(1)
bin_number = re.search(r"БИН (\d+)", all_lines).group(1)
items = re.findall(r"\d+\.\n([^\n]+)\n([\d, ]+) x ([\d, ]+)\n([\d, ]+)", all_lines)
date = re.search(r"\d+\.\d+\.\d+ \d+\:\d+\:\d+", all_lines).group(0)
address = re.search(r"г\.[^\n]+", all_lines).group(0)
overall_cost = re.search(r"ИТОГО:\n([^\n]+)", all_lines).group(1)

def f(s):
    s=s.replace(" ","")
    s=s.replace(",",".")
    return float(s)

check_sum=0

print('Name of the company: {}'.format(company_name))
print(f'BIN number: {bin_number}')
for index, item in enumerate(items):
    print(f'{index+1}) {item[0]}')
    print(f'\t{item[1]} * {item[2]} = {item[3]}')
    check_sum+=f(item[3])

print(f'Date: {date}')
print(f'Address: {address}')
print(f'Overall: {overall_cost}')

print(f'Our sum: {check_sum}')
