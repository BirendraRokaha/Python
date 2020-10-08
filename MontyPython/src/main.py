'''
Monty python is a html site generator using python.
'''

# This function is used to create a basic html template.

def create_index():
        title = input('enter the page title: ')
        if title == '':
            title = 'Home Page'
        with open('index.html', mode = 'w') as home:
            home.write('<html>\n')
            home.write('<head>\n')
            home.write(f'<title>{title}</title>\n')
            home.write('</head>\n')
            home.write('<body>\n')
            home.write('Body Here.\n')
            home.write('</body>\n')
            home.write('</html>\n')



# Main program area

if __name__ == '__main__':
    create_index()
