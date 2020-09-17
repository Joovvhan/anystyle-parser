import json

with open('temp.json') as f:
    json_data = json.load(f)

with open('reference.csv', 'w') as f:
    for data in json_data:

        et_al = False

        citation_num = data['citation-number'][0]
        data.pop('citation-number', None)

        try:
            title = data['title'][0].replace('- ', '')
            title = '"' + title + '"'
            data.pop('title', None)
        except:
            print(f'{citation_num} Title is missing')

        author_list = list()
        for dict in data['author']:
            try:
                author = f"{dict['given']} {dict['family']}"
                author_list.append(author)
            except:
                if 'others' in dict:
                    et_al = True
        
        data.pop('author', None)
            
        author_string = ', '.join(author_list).replace('- ', '')

        if et_al:
            author_string += ', et al.'
        
        author_string = '"' + author_string + '"'
            
        date = data['date'][0]
        data.pop('date', None)

        notes = ''

        for key in data:
            try:
                notes += data[key][0] + ' '
            except TypeError:
                pass

        notes = ('"' + notes.strip() + '"').replace('- ', '')

        print('\n'.join([citation_num, title, author_string, date, notes]))
        print()

        # print()

        f.write(', '.join([citation_num, title, author_string, date, notes]) + '\n')