import sys


def read_file(filename):
    with open(filename) as file:
        return file.readlines()


def write_file(filename, data):
    with open(filename, 'w') as file:
        file.writelines(data)


def transcode(input, filename):
    output = []
    job_name = ''
    
    switch = False
    for char in filename:
        if char == '.':
            switch = True
        
        elif not char.isalnum():
            char = '-'
        
        if switch == False:
            job_name += char
    
    output.append('apiVersion: batch/v1\n')
    output.append('kind: Job\n')
    output.append('metadata:\n')
    output.append(f'  name: {job_name}\n')
    output.append('spec:\n')
    output.append('  template:\n')
    output.append('    spec:\n')
    output.append('      restartPolicy: Never\n')
    output.append('      containers:\n')
    output.append(f'        - name: {job_name}\n')
    output.append('          image: rayproject/ray:2.9.0\n')
    output.append('          command: ["python", "-c"]\n')
    output.append('          securityContext:\n')
    output.append('            allowPrivilegeEscalation: false\n')
    output.append('            capabilities:\n')
    output.append('              drop:\n')
    output.append('                - "ALL"\n')
    output.append('            runAsNonRoot: true\n')
    output.append('            seccompProfile:\n')
    output.append('              type: RuntimeDefault\n')
    output.append('          args:\n')
    output.append(f'            - |\n')
    
    for line in input:
        if line[0] == ' ':
            output.append('            ' + line)
        
        else:
            output.append('              ' + line)
    
    return output


if __name__ == '__main__':
    input = read_file(sys.argv[1])
    output = transcode(input, sys.argv[1])
    
    output_filename = ''
    
    for char in sys.argv[1]:
        if char == '.':
            output_filename += '.yaml'
            break
        
        else:
            output_filename += char
    
    write_file(output_filename, output)
