first_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха',
           'была', '+5', 'градусов']
second_list = []
for numb in first_list:
    if numb.isdigit():
        second_list.extend(['"', f'{int(numb):02}', '"'])
    elif (numb.startswith('+') or numb.startswith('-')) and numb[1:].isdigit():
        second_list.extend(['"', f'{numb[0]}{int(numb[1:]):02}', '"'])
    else:
        second_list.append(numb)
out_info = ' '.join(second_list)
print(out_info)
