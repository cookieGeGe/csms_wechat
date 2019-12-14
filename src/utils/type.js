/**
 * Created by 16288 on 2019/11/23.
 */

//管理员用户类型
export function getAdmintype(val) {
  const vals=parseInt(val);
  switch (vals){
    case 0: return '超级管理员'; break;
    case 1: return '管理员'; break;
  }
}

/*  企业    */
//类型
export const companyTypeArr=[
  {text:'企业类型',value:8},
  {text:'施工企业',value:0},
  {text:'监理单位',value:1},
  {text:'勘察设计',value:2},
  {text:'劳务公司',value:3},
  {text:'房地产开发',value:4},
  {text:'政府及事业单位',value:5},
  {text:'其他业主单位',value:6},
  {text:'其他',value:7},
];
export function companyType(data){
  switch (parseInt(data)){
    case 0:return '施工企业';break;
    case 1:return '监理单位';break;
    case 2:return '勘察设计';break;
    case 3:return '劳务公司';break;
    case 4:return '房地产开发';break;
    case 5:return '政府及事业单位';break;
    case 6:return '其他业主单位';break;
    case 7:return '其他';break;
  }
}

//不良状态
export const companyBadArr=[
  {text:'企业状态',value:0},
  {text:'正常',value:1},
  {text:'风险',value:2},
  {text:'黑名单',value:3},
];
export function companyBad(data) {
  switch (parseInt(data)){
    case 0:return '全部';break;
    case 1:return '正常';break;
    case 2:return '风险';break;
    case 3:return '黑名单';break;
  }
}

//联系方式

export function contact(data) {
  if(JSON.stringify(data)==='[]') return;
  var Phone='';
  var space='&nbsp;';
  for (var i=0;i<data.length;i++){
    Phone+=data[i].name+space+(data[i].projectname||"暂无所在项目")+space+data[i].phone+space+data[i].post+'<br/>';
  }
  return Phone;
}


/*  项目    */
//类型
export const projectTypeArr=[
  {text:'项目类型',value:4},
  {text:'政府投资',value:0},
  {text:'民营开发',value:1},
  {text:'国企分包',value:2},
  {text:'其他',value:3},
];
export function projectType(data) {
  switch (parseInt(data)) {
    case 0:return '政府投资'; break;
    case 1:return '民营开发';break;
    case 2:return '国企分包'; break;
    case 3:return '其他'; break;
  }
}

//发放情况
export function projectStatus(data) {
  switch (parseInt(data)) {
    case 0:return '全额到'; break;
    case 1:return '部分到';break;
    case 2:return '未发放'; break;
  }
}

//不良状态
export const projectBadArr=[
  {text:'项目状态',value:4},
  {text:'正常',value:0},
  {text:'常态监管',value:1},
  {text:'重点',value:2},
  {text:'严重',value:3},
];
export function projectBad(data) {
  switch (data) {
    case 0:return '正常'; break;
    case 1:return '常态监管'; break;
    case 2:return '重点';break;
    case 3:return '严重'; break;
  }
}



/*  劳工    */
//性别
export const laborSexArr=[
  {text:'性别',value:2},
  {text:'女',value:0},
  {text:'男',value:1},
];
export function laborSex(data) {
  switch (parseInt(data)) {
    case 1:return '男'; break;
    case 0:return '女';break;
  }
}

//工种
export const laborJobArr=[
  {text:'工种',value:5},
  {text:'钢筋工',value:0},
  {text:'架子工',value:1},
  {text:'模板工',value:2},
  {text:'通风工',value:3},
  {text:'机械设备安装工',value:4},
];
export function laborJob(data) {
  switch (parseInt(data)) {
    case 0:return '钢筋工'; break;
    case 1:return '架子工'; break;
    case 2:return '模板工';break;
    case 3:return '通风工'; break;
    case 4:return '机械设备安装工'; break;
    //case 5:return '工种'; break;
  }
}


// 年龄
export const laborAgeArr=[
  {text:'年龄',value:6},
  {text:'18以下',value:0},
  {text:'18-30',value:1},
  {text:'30-39',value:2},
  {text:'40-49',value:3},
  {text:'50-55',value:4},
  {text:'55以上',value:5},
];

// 教育程度
export const laborEduArr=[
  {text:'学历',value:7},
  {text:'无',value:0},
  {text:'小学',value:1},
  {text:'初中',value:2},
  {text:'高中',value:3},
  {text:'大学',value:4},
  {text:'硕士',value:5},
  {text:'博士',value:6},
];

//不良
export function laborIsbadrecord(data) {
  switch (parseInt(data)) {
    case 0:return '正常'; break;
    case 1:return '不良'; break;
    case 2:return '黑名单'; break;
  }
}



/*    保函       */
// 保函类型
export const guaranteeTypeArr=[
  {text:'全部',value:9},
  {text:'投标',value:0},
  {text:'履约',value:1},
  {text:'预付款',value:2},
  {text:'农民工工资支付',value:3},
  {text:'业主支付',value:4},
  {text:'质量',value:5},
  {text:'资本金',value:6},
  {text:'房屋质量',value:7},
  {text:'其他',value:8},
];
export function guarantype(data) {
  switch (parseInt(data)){
    case 0:return '投标'; break;
    case 1:return '履约'; break;
    case 2:return '预付款';break;
    case 3:return '农民工工资支付'; break;
    case 4:return '业主支付'; break;
    case 5:return '质量'; break;
    case 6:return '资本金'; break;
    case 7:return '房屋质量'; break;
    case 8:return '其他'; break;
  }
}


///获取缩略图
export function getMinImage(url){
    var imgSrcArr=url.split('.');
    var imgName=imgSrcArr[0];
    var imgType=imgSrcArr[1];
    var min_image=imgName+'_min'+'.'+imgType;
    return min_image
}


