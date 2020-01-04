import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/views/Login'
import Main from '@/views/Main'

import Company from '@/views/company/Company'
import CompanyView from '@/views/company/CompanyView'

import Project from '@/views/project/Project'
import ProjectView from '@/views/project/ProjectView'

import Labor from '@/views/labor/Labor'
import LaborView from '@/views/labor/LaborView'

import Help from '@/views/help/Help'
import helpView from '@/views/help/helpView'
import HelpPdf from '@/views/help/viewPDF'
import guarantee from '@/views/guarantee/guarantee'
import guaranteeView from '@/views/guarantee/guaranteeView'

import bank from '@/views/bank/bank'
import bankView from '@/views/bank/bankView'

import wage from '@/views/wage/wage'
import wageView from '@/views/wage/wageView'

import Attend from '@/views/attend/Attend'
import AttendView from '@/views/attend/AttendView'
import AttendInfo from '@/components/attend/AttendInfo'


import Search from '@/components/areas/Search'

Vue.use(Router);

export default new Router({
  // mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Login',
      component: resolve => require(['@/views/Login'], resolve)
    },
    {
      path: '/Main',
      name: 'Main',
      component: resolve => require(['@/views/Main'], resolve)
    },
    {
      path: '/Search',
      name: 'Search',
      component: resolve => require(['@/components/areas/Search'], resolve)
    },
    {
      path: '/Company',
      name: 'Company',
      component: resolve => require(['@/views/company/Company'], resolve)
    },
    {
      path: '/Project',
      name: 'Project',
      component: resolve => require(['@/views/project/Project'], resolve)
    },
    {
      path: '/Labor',
      name: 'Labor',
      component: resolve => require(['@/views/labor/Labor'], resolve)
    },
    {
      path: '/CompanyView',
      name: 'CompanyView',
      component: resolve => require(['@/views/company/CompanyView'], resolve)
    },
    {
      path: '/ProjectView',
      name: 'ProjectView',
      component: resolve => require(['@/views/project/ProjectView'], resolve)
    },
    {
      path: '/LaborView',
      name: 'LaborView',
      component: resolve => require(['@/views/labor/LaborView'], resolve)
    },

    {
      path: '/Help',
      name: 'Help',
      component: resolve => require(['@/views/help/Help'], resolve)
    },
    {
      path: '/helpView',
      name: 'helpView',
      component: resolve => require(['@/views/help/helpView'], resolve)
    },
    {
      path: '/Guarantee',
      name: 'Guarantee',
      component: resolve => require(['@/views/guarantee/guarantee'], resolve)
    },
    {
      path: '/GuaView',
      name: 'GuaView',
      component: resolve => require(['@/views/guarantee/guaranteeView'], resolve)
    },
    {
      path: '/bank',
      name: 'bank',
      component: resolve => require(['@/views/bank/bank'], resolve)
    },
    {
      path: '/bankView',
      name: 'bankView',
      component: resolve => require(['@/views/bank/bankView'], resolve)
    },
    {
      path: '/wage',
      name: 'wage',
      component: resolve => require(['@/views/wage/wage'], resolve)
    },
    {
      path: '/salaryView',
      name: 'salaryView',
      component: resolve => require(['@/views/wage/wageView'], resolve)
    },
    {
      path: '/Attend',
      name: 'Attend',
      component: resolve => require(['@/views/attend/Attend'], resolve)
    },
    {
      path: '/AttendView',
      name: 'AttendView',
      component: resolve => require(['@/views/attend/AttendView'], resolve)
    },
    {
      path: '/AttendInfo',
      name: 'AttendInfo',
      component: resolve => require(['@/components/attend/AttendInfo'], resolve)
    },
    {
      path: '/HelpPdf',
      name: 'HelpPdf',
      component: resolve => require(['@/views/help/viewPDF'], resolve)
    },
  ]
})
