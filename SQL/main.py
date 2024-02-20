import pyodbc

def insert_data(table,id , name , lastname , age):
    with cnx as con : 
        sql_insert = """
                    INSERT INTO `%s`(`member_ID`, `member_name`, `member_lastname`, `member_age`) 
                     VALUES ( %d , '%s' , '%s' , %d)
                    """
        con.execute(sql_insert % (str(table),int(id) , str(name) , str(lastname) , int(age)))
    cnx.close()

def select_data (table):
    with cnx as show: 
        sql_show = """
                   SELECT * FROM `%s`
                """
        cur = show.cursor()
        cur.execute(sql_show %(str(table)))

        for rows in cur.fetchall() : 
            print(rows)
    cnx.close()

def delete_data(*args):
    '''
    Add the operator at the last parameter.
    Command : column1 = value1 , column2 = value2 , ..... , Name of the table , Operator (Optional)
    '''
    with cnx as dele : 

        size = len(args)
        Operator = args[size-1]
        ListOfOperator = ['NOT','not','AND','and','OR','or']
        if size >= 2 : 
            if (args[size-1] in ListOfOperator)   : 
                arguments = size - 2
            else:
                arguments = size - 1 

            dele_data = """
                        DELETE FROM `{table}` WHERE
                        """.format(table = args[arguments]) 
            
            if Operator in ListOfOperator: 
                for i in range(arguments):  
                    if i == arguments-1:
                        dele_data += args[i] 
                    else:
                        dele_data+= args[i] + f' {Operator} '
            else:
                dele_data+=args[0]

            print(dele_data)
            dele.execute(dele_data)
        else:
            print(" Check the parameters. \n You have to add target , table or operators.")


if __name__ == '__main__':

    config = {
                'user': '',
                'password': '',
                'server': '127.0.0.1',
                'database': 'pythondb',
                'uid' : 'root',
                'driver' : 'MySQL ODBC 8.3 Unicode Driver'
                }
    cnx = pyodbc.connect(**config)


    # insert_data(6145 , 'Mcdonal' , 'Kfc' , 69)
    delete_data('member_id = 6138'  )
    # select_data('tbl_member')