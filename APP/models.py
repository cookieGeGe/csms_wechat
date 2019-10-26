# coding: utf-8
from APP.functions import db
from APP.model_serializ import BaseModel


class Account(BaseModel):
    __tablename__ = 'account'

    id = db.Column(db.Integer, primary_key=True)
    dnumber = db.Column(db.String(255))
    dtypeid = db.Column(db.ForeignKey('electricbox.id', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    position = db.Column(db.String(255))
    project = db.Column(db.String(255))
    status = db.Column(db.Integer)
    remark = db.Column(db.String(255))
    collectionid = db.Column(db.String(255))
    breaknum = db.Column(db.Integer)
    fatherid = db.Column(db.Integer)
    haschild = db.Column(db.Integer)
    user = db.Column(db.String(255))
    gateway = db.Column(db.String(255))
    atemp = db.Column(db.String(255), server_default=db.FetchedValue())
    arc = db.Column(db.String(255), server_default=db.FetchedValue())
    groupnum = db.Column(db.String(255))

    electricbox = db.relationship('Electricbox', primaryjoin='Account.dtypeid == Electricbox.id', backref='accounts')

    _default_fields = [
        "id", "dnumber", "dtypeid", "position", "project", "status", "remark", "collectionid", "breaknum", "fatherid",
        "haschild", "user"
    ]
    _hidden_fields = []
    _readonly_fields = []


class Alarm(BaseModel):
    __tablename__ = 'alarm'

    id = db.Column(db.Integer, primary_key=True)
    collectionid = db.Column(db.String(255))
    alarmtype = db.Column(db.Integer)
    alarmtime = db.Column(db.DateTime)
    info = db.Column(db.String(255))
    status = db.Column(db.Integer)
    dealtime = db.Column(db.DateTime)
    deal = db.Column(db.Integer)
    dealinfo = db.Column(db.String(255))
    temp = db.Column(db.String(255), server_default=db.FetchedValue())
    cur = db.Column(db.String(255), server_default=db.FetchedValue())
    arc = db.Column(db.Integer, server_default=db.FetchedValue())
    smo = db.Column(db.Integer, server_default=db.FetchedValue())
    temp0 = db.Column(db.String(255), server_default=db.FetchedValue())
    temp1 = db.Column(db.String(255), server_default=db.FetchedValue())
    temp2 = db.Column(db.String(255), server_default=db.FetchedValue())
    temp3 = db.Column(db.String(255), server_default=db.FetchedValue())
    temp4 = db.Column(db.String(255), server_default=db.FetchedValue())
    temp5 = db.Column(db.String(255), server_default=db.FetchedValue())
    temp6 = db.Column(db.String(255), server_default=db.FetchedValue())
    temp7 = db.Column(db.String(255), server_default=db.FetchedValue())
    avoltage = db.Column(db.String(255), server_default=db.FetchedValue())
    bvoltage = db.Column(db.String(255), server_default=db.FetchedValue())
    cvoltage = db.Column(db.String(255), server_default=db.FetchedValue())
    acurrent = db.Column(db.String(255), server_default=db.FetchedValue())
    bcurrent = db.Column(db.String(255), server_default=db.FetchedValue())
    ccurrent = db.Column(db.String(255), server_default=db.FetchedValue())
    tpower = db.Column(db.String(255), server_default=db.FetchedValue())
    tempwarn = db.Column(db.String(255), server_default=db.FetchedValue())
    curwarn = db.Column(db.String(255), server_default=db.FetchedValue())
    alarmid = db.Column(db.ForeignKey('alarminfo.id', ondelete='CASCADE', onupdate='CASCADE'), index=True)

    alarminfo = db.relationship('Alarminfo', primaryjoin='Alarm.alarmid == Alarminfo.id', backref='alarms')

    _default_fields = [
        "id", "collectionid", "alarmtype", "alarmtime", "info", "status", "dealtime", "deal", "dealinfo", "temp", "cur",
        "arc", "smo"
    ]
    _hidden_fields = []
    _readonly_fields = []


class Alarminfo(BaseModel):
    __tablename__ = 'alarminfo'

    id = db.Column(db.Integer, primary_key=True)
    collectionid = db.Column(db.String(255))
    alarmtype = db.Column(db.Integer)
    alarmtime = db.Column(db.DateTime)
    info = db.Column(db.String(255))
    status = db.Column(db.Integer)
    dealtime = db.Column(db.DateTime)
    deal = db.Column(db.Integer)
    dealinfo = db.Column(db.String(255))
    temp = db.Column(db.String(255), server_default=db.FetchedValue())
    cur = db.Column(db.String(255), server_default=db.FetchedValue())
    smo = db.Column(db.Integer, server_default=db.FetchedValue())
    endtime = db.Column(db.DateTime)

    _default_fields = [
        "id", "collectionid", "alarmtype", "alarmtime", "info", "status", "dealtime", "deal", "dealinfo", "temp", "cur",
        "smo", "endtime"
    ]
    _hidden_fields = []
    _readonly_fields = []


class Arg(BaseModel):
    __tablename__ = 'args'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True)
    value = db.Column(db.String(255))

    _default_fields = [
        "id", "name", "value"
    ]
    _hidden_fields = []
    _readonly_fields = []


class Electricbox(BaseModel):
    __tablename__ = 'electricbox'

    id = db.Column(db.Integer, primary_key=True)
    fatherid = db.Column(db.Integer)
    name = db.Column(db.String(50))
    protection = db.Column(db.String(50))
    current = db.Column(db.String(50))
    voltage = db.Column(db.String(50))
    frequency = db.Column(db.String(50))
    qlicense = db.Column(db.String(255))
    pspecif = db.Column(db.String(255))
    pstandard = db.Column(db.String(255))
    tup = db.Column(db.String(255))
    tdown = db.Column(db.String(255))
    cup = db.Column(db.String(255))
    cdown = db.Column(db.String(50))
    haschild = db.Column(db.Integer)
    boxdesc = db.Column(db.String(255))
    imgurl = db.Column(db.String(255))

    _default_fields = [
        "id", "fatherid", "name", "protection", "current", "voltage", "frequency", "qlicense", "pspecif", "pstandard",
        "tup", "tdown", "cup", "cdown", "haschild", "boxdesc"
    ]
    _hidden_fields = []
    _readonly_fields = []


class Gateway(BaseModel):
    __tablename__ = 'gateway'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    deviceid = db.Column(db.Integer)
    ip = db.Column(db.String(255))
    port = db.Column(db.String(255))
    description = db.Column(db.String(255))

    _default_fields = [
        "id", "name", "deviceid", "ip", "port", "description"
    ]
    _hidden_fields = []
    _readonly_fields = []


class Log(BaseModel):
    __tablename__ = 'log'

    id = db.Column(db.Integer, primary_key=True)
    info = db.Column(db.String(255))
    userid = db.Column(db.ForeignKey('user.id', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    otype = db.Column(db.String(255))
    otime = db.Column(db.DateTime)

    user = db.relationship('User', primaryjoin='Log.userid == User.id', backref='logs')

    _default_fields = [
        "id", "info", "userid", "otype", "otime"
    ]
    _hidden_fields = []
    _readonly_fields = []


class Protect(BaseModel):
    __tablename__ = 'protect'

    id = db.Column(db.Integer, primary_key=True)
    deviceid = db.Column(db.ForeignKey('account.id', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    week = db.Column(db.DateTime)
    hm = db.Column(db.DateTime)
    month = db.Column(db.DateTime)

    account = db.relationship('Account', primaryjoin='Protect.deviceid == Account.id', backref='protects')

    _default_fields = [
        "id", "deviceid", "week", "hm", "month"
    ]
    _hidden_fields = []
    _readonly_fields = []


class Protectlog(BaseModel):
    __tablename__ = 'protectlog'

    id = db.Column(db.Integer, primary_key=True)
    deviceid = db.Column(db.ForeignKey('account.id', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    ptype = db.Column(db.Integer)
    person = db.Column(db.String(255))
    pltime = db.Column(db.DateTime)
    remark = db.Column(db.String(255))
    status = db.Column(db.Integer)
    itime = db.Column(db.DateTime)

    account = db.relationship('Account', primaryjoin='Protectlog.deviceid == Account.id', backref='protectlogs')

    _default_fields = [
        "id", "deviceid", "ptype", "person", "pltime", "remark", "status", "itime"
    ]
    _hidden_fields = []
    _readonly_fields = []


class Rawdatum(BaseModel):
    __tablename__ = 'rawdata'
    __table_args__ = (
        db.Index('temp_rc', 'id', 'temp', 'rc'),
        db.Index('collectionid_s', 'id', 'collectionid', 'month', 'year', 'day')
    )

    id = db.Column(db.Integer, primary_key=True)
    collectionid = db.Column(db.String(255))
    temp = db.Column(db.String(255))
    rc = db.Column(db.String(255))
    total = db.Column(db.String(255))
    arc = db.Column(db.Integer, server_default=db.FetchedValue())
    smoke = db.Column(db.Integer)
    workstatus = db.Column(db.Integer)
    rtime = db.Column(db.DateTime)
    month = db.Column(db.String(255))
    year = db.Column(db.String(255))
    day = db.Column(db.String(255))
    temp0 = db.Column(db.String(255), server_default=db.FetchedValue())
    temp1 = db.Column(db.String(255), server_default=db.FetchedValue())
    temp2 = db.Column(db.String(255), server_default=db.FetchedValue())
    temp3 = db.Column(db.String(255), server_default=db.FetchedValue())
    temp4 = db.Column(db.String(255), server_default=db.FetchedValue())
    temp5 = db.Column(db.String(255), server_default=db.FetchedValue())
    temp6 = db.Column(db.String(255), server_default=db.FetchedValue())
    temp7 = db.Column(db.String(255), server_default=db.FetchedValue())
    avoltage = db.Column(db.String(255), server_default=db.FetchedValue())
    bvoltage = db.Column(db.String(255), server_default=db.FetchedValue())
    cvoltage = db.Column(db.String(255), server_default=db.FetchedValue())
    acurrent = db.Column(db.String(255), server_default=db.FetchedValue())
    bcurrent = db.Column(db.String(255), server_default=db.FetchedValue())
    ccurrent = db.Column(db.String(255), server_default=db.FetchedValue())
    tpower = db.Column(db.String(255), server_default=db.FetchedValue())
    tempwarn = db.Column(db.String(255), server_default=db.FetchedValue())
    curwarn = db.Column(db.String(255), server_default=db.FetchedValue())

    _default_fields = [
        "id", "collectionid", "temp", "rc", "total", "arc", "smoke", "workstatus", "rtime", "month", "year", "day"
    ]
    _hidden_fields = []
    _readonly_fields = []


class SaveOneDay(BaseModel):
    __tablename__ = 'save_one_day'
    __table_args__ = (
        db.Index('collectionid', 'id', 'month', 'day', 'year', 'collectionid'),
    )

    id = db.Column(db.Integer, primary_key=True)
    start = db.Column(db.String(255))
    end = db.Column(db.String(255))
    temp = db.Column(db.String(255))
    current = db.Column(db.String(255))
    smoke = db.Column(db.Integer)
    temp0 = db.Column(db.String(255), server_default=db.FetchedValue())
    temp1 = db.Column(db.String(255), server_default=db.FetchedValue())
    temp2 = db.Column(db.String(255), server_default=db.FetchedValue())
    temp3 = db.Column(db.String(255), server_default=db.FetchedValue())
    temp4 = db.Column(db.String(255), server_default=db.FetchedValue())
    temp5 = db.Column(db.String(255), server_default=db.FetchedValue())
    temp6 = db.Column(db.String(255), server_default=db.FetchedValue())
    temp7 = db.Column(db.String(255), server_default=db.FetchedValue())
    avoltage = db.Column(db.String(255), server_default=db.FetchedValue())
    bvoltage = db.Column(db.String(255), server_default=db.FetchedValue())
    cvoltage = db.Column(db.String(255), server_default=db.FetchedValue())
    acurrent = db.Column(db.String(255), server_default=db.FetchedValue())
    bcurrent = db.Column(db.String(255), server_default=db.FetchedValue())
    ccurrent = db.Column(db.String(255), server_default=db.FetchedValue())
    tpower = db.Column(db.String(255), server_default=db.FetchedValue())
    tempwarn = db.Column(db.String(255), server_default=db.FetchedValue())
    curwarn = db.Column(db.String(255), server_default=db.FetchedValue())
    time = db.Column(db.DateTime)
    month = db.Column(db.String(255))
    day = db.Column(db.String(255))
    year = db.Column(db.String(255))
    collectionid = db.Column(db.String(255))

    _default_fields = [
        "id", "start", "end", "temp", "current", "smoke", "time", "month", "day", "year", "collectionid"
    ]
    _hidden_fields = []
    _readonly_fields = []


class User(BaseModel):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    loginname = db.Column(db.String(50))
    username = db.Column(db.String(50))
    password = db.Column(db.String(255))
    phone = db.Column(db.String(20))
    email = db.Column(db.String(50))
    address = db.Column(db.String(255))
    avatar = db.Column(db.String(255))
    description = db.Column(db.String(255))
    type = db.Column(db.Integer)
    status = db.Column(db.Integer)

    _default_fields = [
        "id", "loginname", "username", "password", "phone", "email", "address", "avatar", "description", "type",
        "status"
    ]
    _hidden_fields = []
    _readonly_fields = []
