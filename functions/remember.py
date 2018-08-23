def parse_remember_request(msg, conn):
    command = str(msg.clean_content)[len('/remember '):]
    serv_id = str(msg.server.id)
    cursor = conn.cursor()
    if command.startswith('add'):
        trash, memory_id, content = command.split(' ', 2)
        cursor.execute('''
        INSERT INTO Memory(id, serv_id, text)
        VALUES(%s, %s, %s)
        ''', (memory_id, serv_id, content))
        conn.commit()
        return 'I will remember that!'
    elif command.startswith('update'):
        trash, memory_id, content = command.split(' ', 2)
        cursor.execute('''
                UPDATE Memory
                SET text = %s
                WHERE id = %s
                AND serv_id = %s
                ''', (content, memory_id, serv_id))
        conn.commit()
        return 'I\'ll update my memory!'
    else:
        cursor.execute('''
        SELECT text FROM Memory
        WHERE serv_id = %s
        AND LOWER(id) = LOWER(%s)
        ''', (serv_id, command))
        for i in cursor:  # will only ever have one result
            return '\n' + i[0] + '\n'
        return 'I don\'t recall that.'  # returns this if nothing in cursor
