filenames = ['intra.h', 'intra.c', 'input.txt', 'run.py']

result = [filename for filename in filenames if filename.endswith('.h') or filename.endswith('.c')]

print(result)
