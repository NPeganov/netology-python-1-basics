def box(width, length, height):
    if width and length and height == 15:
        print('box 1')
    elif width or length or height > 200:
        print('ski packaging')
    elif 15 < width or length or height < 50:
        print('box 2')
    else:
        print('box 3')

if __name__ == '__main__':
    width = int(input('Enter the width (sm): '))
    length = int(input('Enter the length (sm): '))
    height = int(input('Enter the height (sm): '))
    box(width, length, height)
