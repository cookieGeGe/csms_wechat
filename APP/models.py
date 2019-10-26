# coding: utf-8
from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.schema import FetchedValue
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class TbApi(db.Model):
    __tablename__ = 'tb_api'

    ID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(255))
    Description = db.Column(db.String(255))
    PID = db.Column(db.ForeignKey('tb_permission.ID', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    Type = db.Column(db.Integer)

    tb_permission = db.relationship('TbPermission', primaryjoin='TbApi.PID == TbPermission.ID', backref='tb_apis')


class TbArea(db.Model):
    __tablename__ = 'tb_area'

    ID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(50))
    FatherID = db.Column(db.Integer)
    HasChild = db.Column(db.Integer)


class TbAttendance(db.Model):
    __tablename__ = 'tb_attendance'

    id = db.Column(db.Integer, primary_key=True)
    laborid = db.Column(db.Integer)
    year = db.Column(db.String(255))
    amin = db.Column(db.String(255))
    amout = db.Column(db.String(255))
    pmin = db.Column(db.String(255))
    pmout = db.Column(db.String(255))
    projectid = db.Column(db.Integer)
    month = db.Column(db.String(255))
    day = db.Column(db.String(255))


class TbBadrecord(db.Model):
    __tablename__ = 'tb_badrecord'

    ID = db.Column(db.Integer, primary_key=True)
    Type = db.Column(db.Integer)
    Description = db.Column(db.String(255))
    RecordTime = db.Column(db.DateTime)


class TbBank(db.Model):
    __tablename__ = 'tb_bank'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    description = db.Column(db.String(255))


class TbCguarantee(db.Model):
    __tablename__ = 'tb_cguarantee'

    ID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(255))
    IDCard = db.Column(db.String(255))
    Address = db.Column(db.String(255))
    Phone = db.Column(db.String(255))
    Area = db.Column(db.String(255))
    Pvalue = db.Column(db.String(255))
    Proportion = db.Column(db.String(255))
    Paddress = db.Column(db.String(255))
    IDimg = db.Column(db.String(255))
    Pimg = db.Column(db.String(255))
    GID = db.Column(db.Integer, server_default=db.FetchedValue())
    Description = db.Column(db.String(255))


class TbClas(db.Model):
    __tablename__ = 'tb_class'

    ID = db.Column(db.Integer, primary_key=True)
    CompanyID = db.Column(db.ForeignKey('tb_company.ID'), index=True)
    ClassName = db.Column(db.String(50))
    ProjectID = db.Column(db.Integer)

    tb_company = db.relationship('TbCompany', primaryjoin='TbClas.CompanyID == TbCompany.ID', backref='tb_class')


class TbCompany(db.Model):
    __tablename__ = 'tb_company'

    ID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(255))
    Legal = db.Column(db.String(255))
    Address = db.Column(db.String(255))
    Phone = db.Column(db.String(4096))
    License = db.Column(db.String(255))
    OtherPic = db.Column(db.String(255))
    BadRecord = db.Column(db.String(255))
    Type = db.Column(db.Integer)
    Description = db.Column(db.String(255))
    ProvinceID = db.Column(db.Integer)
    CityID = db.Column(db.Integer)
    DistrictID = db.Column(db.Integer)
    HasBadRecord = db.Column(db.Integer)
    url = db.Column(db.String(255))
    otherinfo = db.Column(db.String(4096))


class TbCompanyBadrecord(db.Model):
    __tablename__ = 'tb_company_badrecord'

    ID = db.Column(db.Integer, primary_key=True)
    CompanyID = db.Column(db.ForeignKey('tb_company.ID'), index=True)
    BadrecordID = db.Column(db.ForeignKey('tb_otherfile.id'), index=True)

    tb_otherfile = db.relationship('TbOtherfile', primaryjoin='TbCompanyBadrecord.BadrecordID == TbOtherfile.id', backref='tb_company_badrecords')
    tb_company = db.relationship('TbCompany', primaryjoin='TbCompanyBadrecord.CompanyID == TbCompany.ID', backref='tb_company_badrecords')


class TbGuarantee(db.Model):
    __tablename__ = 'tb_guarantee'

    ID = db.Column(db.Integer, primary_key=True)
    CompanyID = db.Column(db.String(255), index=True)
    Capital = db.Column(db.String(255))
    Nature = db.Column(db.String(255))
    Name = db.Column(db.String(255))
    Number = db.Column(db.String(255))
    Amount = db.Column(db.String(255))
    Kind = db.Column(db.String(255))
    ProjectID = db.Column(db.String(255), index=True)
    SignTime = db.Column(db.DateTime)
    Category = db.Column(db.Integer)
    Deadline = db.Column(db.String(255))
    Expiretime = db.Column(db.DateTime)
    Totalrate = db.Column(db.String(255))
    Total = db.Column(db.String(255))
    RealAC = db.Column(db.String(255))
    Marginratio = db.Column(db.String(255))
    Margin = db.Column(db.String(255))
    Bene = db.Column(db.String(255))
    PID = db.Column(db.Integer)
    CID = db.Column(db.Integer)
    DID = db.Column(db.Integer)
    Description = db.Column(db.String(255))
    Duration = db.Column(db.DateTime)
    GuaCompany = db.Column(db.String(255))
    Address = db.Column(db.String(4096))


class TbLaborBadrecord(db.Model):
    __tablename__ = 'tb_labor_badrecord'

    ID = db.Column(db.Integer, primary_key=True)
    LaborID = db.Column(db.ForeignKey('tb_laborinfo.ID'), index=True)
    BadRecordID = db.Column(db.ForeignKey('tb_otherfile.id'), index=True)

    tb_otherfile = db.relationship('TbOtherfile', primaryjoin='TbLaborBadrecord.BadRecordID == TbOtherfile.id', backref='tb_labor_badrecords')
    tb_laborinfo = db.relationship('TbLaborinfo', primaryjoin='TbLaborBadrecord.LaborID == TbLaborinfo.ID', backref='tb_labor_badrecords')


class TbLaborinfo(db.Model):
    __tablename__ = 'tb_laborinfo'

    ID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(50))
    Age = db.Column(db.Integer)
    Sex = db.Column(db.Integer)
    Birthday = db.Column(db.DateTime)
    Address = db.Column(db.String(255))
    Nationality = db.Column(db.String(25))
    IDCard = db.Column(db.String(25))
    Phone = db.Column(db.String(20))
    CompanyID = db.Column(db.ForeignKey('tb_company.ID'), index=True)
    JobType = db.Column(db.Integer)
    ClassID = db.Column(db.ForeignKey('tb_class.ID'), index=True)
    Identity = db.Column(db.Integer)
    DepartureDate = db.Column(db.DateTime)
    EntryDate = db.Column(db.DateTime)
    Hardhatnum = db.Column(db.String(50))
    CloseupPhoto = db.Column(db.String(255))
    Education = db.Column(db.String(50))
    CreateTime = db.Column(db.DateTime)
    ProjectID = db.Column(db.Integer)
    IsPM = db.Column(db.Integer)
    IssueAuth = db.Column(db.String(255))
    Political = db.Column(db.String(255))
    Train = db.Column(db.String(255))
    EmerCon = db.Column(db.String(255))
    IDP = db.Column(db.String(255))
    IDB = db.Column(db.String(255))
    PID = db.Column(db.Integer)
    CID = db.Column(db.Integer)
    DID = db.Column(db.Integer)
    SVP = db.Column(db.DateTime)
    EVP = db.Column(db.DateTime)
    IsLeader = db.Column(db.Integer)
    Superiors = db.Column(db.Integer)
    Remark = db.Column(db.String(255))
    BadRecord = db.Column(db.Integer, server_default=db.FetchedValue())
    Isbadrecord = db.Column(db.Integer, server_default=db.FetchedValue())
    FeeStand = db.Column(db.String(255))
    Avatar = db.Column(db.String(255))
    isFeeStand = db.Column(db.String(255))

    tb_clas = db.relationship('TbClas', primaryjoin='TbLaborinfo.ClassID == TbClas.ID', backref='tb_laborinfos')
    tb_company = db.relationship('TbCompany', primaryjoin='TbLaborinfo.CompanyID == TbCompany.ID', backref='tb_laborinfos')


class TbOtherfile(db.Model):
    __tablename__ = 'tb_otherfile'

    id = db.Column(db.Integer, primary_key=True)
    companyid = db.Column(db.Integer)
    filename = db.Column(db.String(255))
    filepath = db.Column(db.String(255))
    type = db.Column(db.Integer, server_default=db.FetchedValue())


class TbPerUrl(db.Model):
    __tablename__ = 'tb_per_url'

    ID = db.Column(db.Integer, primary_key=True)
    PID = db.Column(db.Integer)
    url = db.Column(db.String(255))
    name = db.Column(db.String(255))


class TbPermission(db.Model):
    __tablename__ = 'tb_permission'

    ID = db.Column(db.Integer, primary_key=True)
    PerName = db.Column(db.String(255))
    Permission = db.Column(db.String(255))


class TbPicGroup(db.Model):
    __tablename__ = 'tb_pic_group'

    ID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(255))
    Type = db.Column(db.Integer)
    GUrl = db.Column(db.String(255))
    CID = db.Column(db.Integer)
    Ptype = db.Column(db.Integer)


class TbPic(db.Model):
    __tablename__ = 'tb_pics'

    ID = db.Column(db.Integer, primary_key=True)
    GroupID = db.Column(db.Integer)
    Purl = db.Column(db.String(255))
    Name = db.Column(db.String(255))
    Ptype = db.Column(db.Integer)
    Type = db.Column(db.String(255))
    ProgressID = db.Column(db.Integer, server_default=db.FetchedValue())


class TbProClas(db.Model):
    __tablename__ = 'tb_pro_class'

    ID = db.Column(db.Integer, primary_key=True)
    ProjectID = db.Column(db.ForeignKey('tb_project.ID'), index=True)
    ClassID = db.Column(db.ForeignKey('tb_class.ID'), index=True)

    tb_clas = db.relationship('TbClas', primaryjoin='TbProClas.ClassID == TbClas.ID', backref='tb_pro_class')
    tb_project = db.relationship('TbProject', primaryjoin='TbProClas.ProjectID == TbProject.ID', backref='tb_pro_class')


class TbProgres(db.Model):
    __tablename__ = 'tb_progress'

    ID = db.Column(db.Integer, primary_key=True, nullable=False)
    ProjectID = db.Column(db.ForeignKey('tb_project.ID'), index=True)
    Status = db.Column(db.Integer)
    UploadTime = db.Column(db.DateTime)
    Person = db.Column(db.String(512))
    Remark = db.Column(db.String(255))
    RType = db.Column(db.Integer)
    Contract = db.Column(db.Integer)
    Content = db.Column(db.String(512))
    RealName = db.Column(db.Integer)
    Attend = db.Column(db.Integer)
    Wage = db.Column(db.Integer)
    Rights = db.Column(db.Integer)
    Lwage = db.Column(db.Integer)
    LAB = db.Column(db.Integer)
    PAB = db.Column(db.Integer)
    Arrears = db.Column(db.Integer)
    LPayCert = db.Column(db.Integer)
    PPay = db.Column(db.String(255), server_default=db.FetchedValue())
    LPay = db.Column(db.String(255), server_default=db.FetchedValue())
    Total = db.Column(db.String(255), server_default=db.FetchedValue())
    Percent = db.Column(db.String(255), primary_key=True, nullable=False)
    year = db.Column(db.String(255))
    month = db.Column(db.String(255))

    tb_project = db.relationship('TbProject', primaryjoin='TbProgres.ProjectID == TbProject.ID', backref='tb_progress')


class TbProject(db.Model):
    __tablename__ = 'tb_project'

    ID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(255))
    Type = db.Column(db.Integer)
    GuaranType = db.Column(db.Integer)
    Price = db.Column(db.String(255))
    Duration = db.Column(db.String(255))
    GAmount = db.Column(db.String(255))
    PrinPical = db.Column(db.String(255))
    WagePercent = db.Column(db.String(50))
    StartTime = db.Column(db.DateTime)
    EndTime = db.Column(db.DateTime)
    Address = db.Column(db.String(255))
    Build = db.Column(db.Integer)
    Cons = db.Column(db.Integer)
    ConsManager = db.Column(db.String(255))
    OwnerManager = db.Column(db.String(255))
    LaborManager = db.Column(db.String(255), server_default=db.FetchedValue())
    Supervisor = db.Column(db.String(255), server_default=db.FetchedValue())
    Description = db.Column(db.String(255))
    Status = db.Column(db.Integer, server_default=db.FetchedValue())
    PID = db.Column(db.Integer, index=True)
    CID = db.Column(db.Integer)
    DID = db.Column(db.Integer)
    Total = db.Column(db.String(255), server_default=db.FetchedValue())
    TotalPay = db.Column(db.String(255), server_default=db.FetchedValue())
    Issue = db.Column(db.String(255), server_default=db.FetchedValue())
    TotalMonth = db.Column(db.Integer, server_default=db.FetchedValue())
    SubCompany = db.Column(db.String(2048), server_default=db.FetchedValue())
    Bank = db.Column(db.Integer)


class TbSalary(db.Model):
    __tablename__ = 'tb_salary'

    id = db.Column(db.Integer, primary_key=True)
    laborid = db.Column(db.Integer)
    status = db.Column(db.String(255))
    swipe = db.Column(db.String(255))
    manual = db.Column(db.String(255))
    type = db.Column(db.String(255))
    unit = db.Column(db.String(255))
    basicwage = db.Column(db.String(255))
    overtime = db.Column(db.String(255))
    subtotal = db.Column(db.String(255))
    reward = db.Column(db.String(255))
    deduction = db.Column(db.String(255))
    total = db.Column(db.String(255))
    projectname = db.Column(db.String(255))
    companyname = db.Column(db.String(255))
    year = db.Column(db.String(255))
    month = db.Column(db.String(255))


class TbTemplate(db.Model):
    __tablename__ = 'tb_template'

    ID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(255))
    Time = db.Column(db.DateTime)
    Description = db.Column(db.String(255))
    Type = db.Column(db.Integer)
    File = db.Column(db.String(255))
    Number = db.Column(db.String(255))


class TbUser(db.Model):
    __tablename__ = 'tb_user'

    ID = db.Column(db.Integer, primary_key=True)
    LoginName = db.Column(db.String(255))
    UserName = db.Column(db.String(255))
    Password = db.Column(db.String(255))
    Email = db.Column(db.String(50))
    Phone = db.Column(db.String(20))
    Description = db.Column(db.String(255))
    AdminType = db.Column(db.Integer)
    Avatar = db.Column(db.String(255))
    Status = db.Column(db.Integer)
    CompanyID = db.Column(db.Integer)
    permission = db.Column(db.Integer, server_default=db.FetchedValue())


class TbUserArea(db.Model):
    __tablename__ = 'tb_user_area'

    ID = db.Column(db.Integer, primary_key=True)
    UserID = db.Column(db.ForeignKey('tb_user.ID', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    AreaID = db.Column(db.ForeignKey('tb_area.ID', ondelete='CASCADE', onupdate='CASCADE'), index=True)

    tb_area = db.relationship('TbArea', primaryjoin='TbUserArea.AreaID == TbArea.ID', backref='tb_user_areas')
    tb_user = db.relationship('TbUser', primaryjoin='TbUserArea.UserID == TbUser.ID', backref='tb_user_areas')


class TbUserPer(db.Model):
    __tablename__ = 'tb_user_per'

    ID = db.Column(db.Integer, primary_key=True)
    UID = db.Column(db.ForeignKey('tb_user.ID', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    PID = db.Column(db.ForeignKey('tb_permission.ID', ondelete='CASCADE', onupdate='CASCADE'), index=True)

    tb_permission = db.relationship('TbPermission', primaryjoin='TbUserPer.PID == TbPermission.ID', backref='tb_user_pers')
    tb_user = db.relationship('TbUser', primaryjoin='TbUserPer.UID == TbUser.ID', backref='tb_user_pers')


class TbUserPro(db.Model):
    __tablename__ = 'tb_user_pro'

    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.ForeignKey('tb_user.ID', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    pid = db.Column(db.ForeignKey('tb_project.ID', ondelete='CASCADE', onupdate='CASCADE'), index=True)

    tb_project = db.relationship('TbProject', primaryjoin='TbUserPro.pid == TbProject.ID', backref='tb_user_pros')
    tb_user = db.relationship('TbUser', primaryjoin='TbUserPro.uid == TbUser.ID', backref='tb_user_pros')


class TbWage(db.Model):
    __tablename__ = 'tb_wage'

    ID = db.Column(db.Integer, primary_key=True)
    ProjectID = db.Column(db.Integer)
    Status = db.Column(db.Integer)
    WTime = db.Column(db.DateTime)
    RPay = db.Column(db.Float(20))
    year = db.Column(db.String(255))
    month = db.Column(db.String(255))
