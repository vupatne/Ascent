from config.dbQueries import selectqueryfunc, insertqueryfunc
from random import randint
from datetime import datetime


def getuserByPhone(phone):
    sql_query = """select id, userid,firstname, lastname, email, phone, address, reference, 
                        idpassword,createddate, modifieddate
                        from users where phone = %s and isactive = 'A' order by id"""
    data_tuple = (phone, )
    return selectqueryfunc(sql_query, data_tuple)

def getuserByPhoneWithoutFlag(phone):
    sql_query = """select id, userid,firstname, lastname, email, phone, address, reference, 
                        idpassword,createddate, modifieddate
                        from users where phone = %s order by id"""
    data_tuple = (phone, )
    return selectqueryfunc(sql_query, data_tuple)

def getuserByUserId(userid):
    sql_query = """select id, userid,firstname, lastname, email, phone, address, reference, 
                        idpassword,createddate, modifieddate
                        from users where userid = %s and isactive = 'A' order by id"""
    data_tuple = (userid, )
    return selectqueryfunc(sql_query, data_tuple)


def add_user(firstname, lastname, email, phone, address, reference, idpassword):
    existFlag = True
    randNo = 1
    while (existFlag):
        randNo = randint(100000, 999999)
        existFlag = getuserByUserId(randNo)

    createddate = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    insert_query = """insert into users(userid, firstname, lastname, email, phone, address, reference, 
                        idpassword,createddate, isactive) 
                    values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    data_tuple = (randNo, firstname, lastname, email, phone, address, reference, idpassword, createddate, 'A')
    insertqueryfunc(insert_query, data_tuple)


def getuserByPhoneAndPassword(phone, password):
    sql_query = """select id, userid, firstname, lastname, email, phone, address, reference, 
                        idpassword,createddate, modifieddate
                        from users where phone =%s and idpassword= %s and isactive = 'A' order by id"""
    data_tuple = (phone, password)
    return selectqueryfunc(sql_query, data_tuple)

def setPasswordforUser(userid, password):
    insert_query = """update users set idpassword = %s where userid =%s"""
    data_tuple = (password, userid)
    insertqueryfunc(insert_query, data_tuple)

def setUserActiveReject(idd, flagg):
    insert_query = """update users set isactive = %s where id =%s"""
    data_tuple = (flagg, idd)
    insertqueryfunc(insert_query, data_tuple)


def getAllPendingUsers():
    sql_query = """select id, userid, firstname, lastname, email, phone, address, reference, 
                        idpassword,createddate, modifieddate
                        from users where isactive = 'P' and id > %s order by id"""
    data_tuple = (0,)
    return selectqueryfunc(sql_query, data_tuple)