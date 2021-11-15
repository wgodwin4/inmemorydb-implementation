def run_database(input_lines):
    def set(name, value):
        if undo:
            undo.append((name, database.get(name)))
        database[name] = value
    def unset(name):
        if undo:
            undo.append((name, database.get(name)))
        del database[name]
    def get(name):
        print (database.get(name, 'NULL'))
    def begin():
        undo.append('stop')
    def num_equal_to(value):
        print (database.values().count(value))
    def rollback():
        while undo:
            action = undo.pop()
            if action == 'stop':
                break
            name, value = action
            if value is None and name in database:
                del database[name]
            elif value is not None:
                database[name] = value
        else:
            print ("NO TRANSACTION")
    def commit():
        if undo:
            del undo[:]
        else:
            print ("NO TRANSACTION")

    undo = []
    database = {}
    commands = {'SET': set, 'UNSET': unset, 'GET': get, 'BEGIN': begin,
        'NUMEQUALTO': num_equal_to, 'ROLLBACK': rollback, 'COMMIT': commit}
    for line in input_lines:
        if line == 'END':
            break
        else:
            words = line.split()
            commands[words[0]](*words[1:])